"""
Módulo para leer datos del test ANT desde archivos Excel

Este módulo proporciona funciones para:
- Leer datos del Excel del test ANT
- Calcular puntuaciones directas por fila y totales
- Identificar explícitamente celdas seleccionadas y no seleccionadas
- Proporcionar estructuras de datos claras y accesibles para análisis posterior
"""
import pandas as pd


def leer_datos_excel(ruta_archivo):
    """
    Lee los datos del archivo Excel del test ANT
    
    Args:
        ruta_archivo: Ruta al archivo Excel
        
    Returns:
        dict: Diccionario con 'edad', 'sub_num', 'nombre_completo', 'nombre' y 'datos_ANT'
    """
    try:
        # Leer hoja 'info' para obtener la edad y sub_num
        df_info = pd.read_excel(ruta_archivo, sheet_name='info')
        edad = df_info['age'].iloc[0] if 'age' in df_info.columns else None
        
        # Extraer sub_num y procesarlo
        sub_num = df_info['sub_num'].iloc[0] if 'sub_num' in df_info.columns else None
        
        # Procesar nombre completo y nombre (primer token)
        # Verificar que sub_num es válido (no None, no NaN, no cadena vacía)
        import math
        if sub_num and not (isinstance(sub_num, float) and math.isnan(sub_num)):
            nombre_completo = str(sub_num).strip()
            # Obtener solo el primer token (antes del primer espacio)
            # Verificar que hay contenido antes de dividir
            if nombre_completo:
                tokens = nombre_completo.split()
                nombre = tokens[0] if tokens else nombre_completo
            else:
                nombre = nombre_completo
        else:
            nombre_completo = None
            nombre = None
        
        # Leer hoja 'ANT' con los datos del test
        # La primera fila contiene los encabezados
        df_ant = pd.read_excel(ruta_archivo, sheet_name='ANT', header=None)
        
        return {
            'edad': edad,
            'sub_num': sub_num,
            'nombre_completo': nombre_completo,
            'nombre': nombre,
            'datos_ANT': df_ant
        }
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        raise


def calcular_puntuaciones_directas(datos):
    """
    Calcula las puntuaciones directas del test ANT
    
    Estructura esperada del Excel (hoja 'ANT'):
    - Primera fila: encabezados (trial, block, congruency, cue, location, FixationTime, ITI, direction, response, correct, RT)
    - Siguientes filas: datos de cada ensayo
    
    Args:
        datos: Dict con 'edad' y 'datos_ANT'
        
    Returns:
        dict: Diccionario con todas las puntuaciones directas
    """
    df = datos['datos_ANT']
    
    # Leer la hoja ANT con encabezados
    # La primera fila contiene los encabezados
    df.columns = df.iloc[0]
    df = df[1:]  # Eliminar la fila de encabezados
    df = df.reset_index(drop=True)
    
    # Convertir columnas numéricas
    df['correct'] = pd.to_numeric(df['correct'], errors='coerce')
    df['RT'] = pd.to_numeric(df['RT'], errors='coerce')
    
    # Calcular número total de ensayos
    total_trials = len(df)
    
    # Calcular terciles para fatiga
    tercile_size = total_trials // 3
    first_third = df.iloc[:tercile_size]
    last_third = df.iloc[-tercile_size:]
    
    # Diccionario para almacenar las puntuaciones
    resultados = {
        'edad': datos['edad'],
        'sub_num': datos.get('sub_num'),
        'nombre_completo': datos.get('nombre_completo'),
        'nombre': datos.get('nombre'),
        'datos_ANT': df,
    }
    
    # === ÍNDICES DE PRECISIÓN ===
    
    # A (Aciertos): Porcentaje de respuestas correctas
    correct_responses = df['correct'].sum()
    resultados['PD_A'] = (correct_responses / total_trials) * 100
    
    # C (Comisiones): Número de errores por respuesta incorrecta
    # correct=0 pero response != NA (respondió pero mal)
    commissions = ((df['correct'] == 0) & (df['response'].notna())).sum()
    resultados['PD_C'] = commissions
    
    # O (Omisiones): Número de errores por falta de respuesta
    # response == NA (no respondió)
    omissions = df['response'].isna().sum()
    resultados['PD_O'] = omissions
    
    # F_A (Fatiga en precisión): Diferencia en precisión entre inicio y final
    # Porcentaje de aciertos del primer 1/3 - porcentaje de aciertos del último 1/3
    accuracy_first = (first_third['correct'].sum() / len(first_third)) * 100 if len(first_third) > 0 else 0
    accuracy_last = (last_third['correct'].sum() / len(last_third)) * 100 if len(last_third) > 0 else 0
    resultados['PD_F_A'] = accuracy_first - accuracy_last
    
    # === ÍNDICES DE VELOCIDAD ===
    
    # TR (Tiempo de Reacción): promedio del tiempo de respuesta en milisegundos
    # Solo considerar respuestas válidas (donde RT no es NaN)
    valid_rt = df['RT'].dropna()
    resultados['PD_TR'] = valid_rt.mean() if len(valid_rt) > 0 else 0

    # TR_A (Tiempo de Reacción en aciertos): promedio del TR en respuestas correctas
    correct_rt = df[df['correct'] == 1]['RT'].dropna()
    resultados['PD_TR_A'] = correct_rt.mean() if len(correct_rt) > 0 else 0

    # TR_C (Tiempo de Reacción en comisiones): promedio del TR en errores de comisión
    commission_rt = df[(df['correct'] == 0) & (df['response'].notna())]['RT'].dropna()
    resultados['PD_TR_C'] = commission_rt.mean() if len(commission_rt) > 0 else 0

    # TR_A_vs_C: diferencia entre TR en aciertos y TR en comisiones
    resultados['PD_TR_A_vs_C'] = resultados['PD_TR_A'] - resultados['PD_TR_C']
    
    # F_TR (Fatiga en velocidad): Diferencia en TR entre primer 1/3 y último 1/3
    tr_first = first_third['RT'].dropna()
    tr_last = last_third['RT'].dropna()
    tr_first_mean = tr_first.mean() if len(tr_first) > 0 else 0
    tr_last_mean = tr_last.mean() if len(tr_last) > 0 else 0
    resultados['PD_F_TR'] = tr_last_mean - tr_first_mean
    
    # === ÍNDICES DE REDES ATENCIONALES ===
    
    # TR_alerta: Eficiencia de la red de alerta
    # TR promedio de eventos con cue "double" - TR promedio de eventos con cue "nocue"
    df_double = df[df['cue'] == 'double']
    df_nocue = df[df['cue'] == 'nocue']
    
    tr_double_vals = df_double['RT'].dropna()
    tr_nocue_vals = df_nocue['RT'].dropna()
    
    tr_double = tr_double_vals.mean() if len(tr_double_vals) > 0 else 0
    tr_nocue = tr_nocue_vals.mean() if len(tr_nocue_vals) > 0 else 0
    
    resultados['PD_TR_doubleAst'] = tr_double
    resultados['PD_TR_noAst'] = tr_nocue
    resultados['PD_TR_alerta'] = tr_double - tr_nocue
    
    # TR_orientacion: Eficiencia de la red de orientación
    # TR promedio de eventos con cue "spatial" - TR promedio de eventos con cue "center"
    df_spatial = df[df['cue'] == 'spatial']
    df_center = df[df['cue'] == 'center']
    
    tr_spatial_vals = df_spatial['RT'].dropna()
    tr_center_vals = df_center['RT'].dropna()
    
    tr_spatial = tr_spatial_vals.mean() if len(tr_spatial_vals) > 0 else 0
    tr_center = tr_center_vals.mean() if len(tr_center_vals) > 0 else 0
    
    resultados['PD_TR_ladoAst'] = tr_spatial
    resultados['PD_TR_centroAst'] = tr_center
    resultados['PD_TR_orientacion'] = tr_spatial - tr_center
    
    # TR_ejecutivo: Eficiencia de la red ejecutiva
    # TR promedio de eventos con congruency "incongruent" - TR promedio de eventos con congruency "congruent"
    df_incongruent = df[df['congruency'] == 'incongruent']
    df_congruent = df[df['congruency'] == 'congruent']
    
    tr_incongruent_vals = df_incongruent['RT'].dropna()
    tr_congruent_vals = df_congruent['RT'].dropna()
    
    tr_incongruent = tr_incongruent_vals.mean() if len(tr_incongruent_vals) > 0 else 0
    tr_congruent = tr_congruent_vals.mean() if len(tr_congruent_vals) > 0 else 0
    
    resultados['PD_TR_congruente'] = tr_congruent
    resultados['PD_TR_incongruente'] = tr_incongruent
    resultados['PD_TR_ejecutivo'] = tr_incongruent - tr_congruent
    
    return resultados


# ============================================================================
# FUNCIONES DE UTILIDAD PARA CONSULTAR RESULTADOS
# ============================================================================

def obtener_resumen_indices(resultados):
    """
    Obtiene un resumen legible de todos los índices calculados
    
    Args:
        resultados: Dict devuelto por calcular_puntuaciones_directas
        
    Returns:
        str: Texto con resumen formateado de todos los índices
    """
    lineas = []
    lineas.append("=" * 70)
    lineas.append("RESUMEN DE ANT - Puntuaciones Directas")
    lineas.append("=" * 70)
    lineas.append("")
    
    # Índices
    lineas.append("Puntuaciones directas")
    lineas.append(f"  PD_A: {resultados['PD_A']}")
    lineas.append(f"  PD_C: {resultados['PD_C']}")
    lineas.append(f"  PD_O: {resultados['PD_O']}")
    lineas.append(f"  PD_F_A: {resultados['PD_F_A']}")
    lineas.append(f"  PD_TR: {resultados['PD_TR']}")
    lineas.append(f"  PD_TR_doubleAst: {resultados['PD_TR_doubleAst']}")
    lineas.append(f"  PD_TR_noAst: {resultados['PD_TR_noAst']}")
    lineas.append(f"  PD_TR_alerta: {resultados['PD_TR_alerta']}")
    lineas.append(f"  PD_TR_ladoAst: {resultados['PD_TR_ladoAst']}")
    lineas.append(f"  PD_TR_centroAst: {resultados['PD_TR_centroAst']}")
    lineas.append(f"  PD_TR_orientacion: {resultados['PD_TR_orientacion']}")
    lineas.append(f"  PD_TR_congruente: {resultados['PD_TR_congruente']}")
    lineas.append(f"  PD_TR_incongruente: {resultados['PD_TR_incongruente']}")
    lineas.append(f"  PD_TR_ejecutivo: {resultados['PD_TR_ejecutivo']}")
    lineas.append(f"  PD_F_TR: {resultados['PD_F_TR']}")

    
    return "\n".join(lineas)
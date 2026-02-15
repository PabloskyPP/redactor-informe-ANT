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
        # header=None porque no hay fila de encabezados, los datos empiezan en la primera fila
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
    
    Estructura esperada del Excel (hoja 'ANT):
    - Primera columna: nombre del índice (A, C, O, F_A, TR, TR_alerta, TR_orientacion, TR_ejecutivo, F_TR)
    - Segunda columna: valor del índice
    
    Args:
        datos: Dict con 'edad' y 'datos_ANT'
        
    Returns:
        dict: Diccionario con todas las puntuaciones directas
    """
    df = datos['datos_ANT']
    
    # La estructura es: primera columna = índices, segunda columna = valores
    if len(df.columns) < 2:
        raise ValueError("El Excel debe tener al menos 2 columnas (índice y valor)")
    
    # Definir las columnas para índice y valor
    col_indice = 0
    col_valor = 1
    
    # Diccionario para almacenar las puntuaciones por serie
    resultados = {
        'edad': datos['edad'],
        'sub_num': datos.get('sub_num'),
        'nombre_completo': datos.get('nombre_completo'),
        'nombre': datos.get('nombre'),
        'datos_ANT': df,
        
        # Promedio de puntuaciones por serie y Variables de puntuaciones extraídas del excel
        'PD_A': 0,
        'PD_C': 0,
        'PD_O': 0,
        'PD_F_A': 0,
        'PD_TR': 0, 
        'PD_TR_doubleAst': 0,# TR ante eventos de doble asterisco
        'PD_TR_noAst': 0, # TR ante eventos de ningún asterisco
        'PD_TR_alerta': 0, # TR_doubleAst - TR_noAst
        'PD_TR_ladoAst': 0, # TR ante eventos con un asterisco a un lado
        'PD_TR_centroAst': 0,# TR ante eventos con un asterisco en el centro
        'PD_TR_orientacion': 0,# TR_ladoAst - TR_centroAst
        'PD_TR_congruente': 0, # TR ante eventos congruentes
        'PD_TR_incongruente': 0, # TR ante eventos incongruentes
        'PD_TR_ejecutivo': 0,# TR_incongruente - TR_congruente
        'PD_F_TR': 0,  # Fatiga o variabilidad del tiempo de reacción principio y final de la prueba

    }
    
    # Leer los valores del DataFrame según el índice
    for idx, row in df.iterrows():
        indice = str(row[col_indice]).strip().upper()
        valor = row[col_valor]
        
        # Asignar el valor según el índice
        if indice == 'A':
            resultados['PD_A'] = valor
        elif indice == 'C':
            resultados['PD_C'] = valor
        elif indice == 'O':
            resultados['PD_O'] = valor
        elif indice == 'F_A':
            resultados['PD_F_A'] = valor
        elif indice == 'F_TR':
            resultados['PD_F_TR'] = valor
        elif indice == 'TR':
            resultados['PD_TR'] = valor
        elif indice == 'TR_ALERTA':
            resultados['PD_TR_alerta'] = valor
        elif indice == 'TR_ORIENTACION':
            resultados['PD_TR_orientacion'] = valor
        elif indice == 'TR_EJECUTIVO':
            resultados['PD_TR_ejecutivo'] = valor
    
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
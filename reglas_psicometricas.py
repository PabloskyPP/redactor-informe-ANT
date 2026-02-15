"""
Módulo con las reglas psicométricas y baremos del test Stroop
"""
# Variables de puntuaciones extraídas del excel
A = None  # Porcentaje de aciertos
C = None  # Errores de comisión
O = None  # Errores de omisión
F_A = None  # Fatiga o variabilidad de aciertos principio y final de la prueba
TR = None  # Tiempo de reacción promedio
TR_doubleAst = None  # TR ante eventos de doble asterisco
TR_noAst = None  # TR ante eventos de ningún asterisco
TR_alerta = None  # TR_doubleAst - TR_noAst
TR_ladoAst = None  # TR ante eventos con un asterisco a un lado
TR_centroAst = None  # TR ante eventos con un asterisco en el centro
TR_orientacion = None  # TR_ladoAst - TR_centroAst
TR_congruente = None  # TR ante eventos congruentes
TR_incongruente = None  # TR ante eventos incongruentes
TR_ejecutivo = None  # TR_incongruente - TR_congruente
F_TR = None  # Fatiga o variabilidad del tiempo de reacción principio y final de la prueba

# Baremos
# Estos baremos se ajustan según grupo de edad
BAREMOS_BASE = {
    80: {"A": 179,"C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 83, "TR_orientacion": 29.9, "TR_ejecutivo": 29.9},
    78: {"A": 179, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 83, "TR_orientacion": 29.9, "TR_ejecutivo": 29.9},
    76: {"A": 171, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 79, "TR_orientacion": 26.2, "TR_ejecutivo": 26.2},
    74: {"A": 167, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 76, "TR_orientacion": 24.4, "TR_ejecutivo": 24.4},
    72: {"A": 163, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 74, "TR_orientacion": 22.6, "TR_ejecutivo": 22.6},
    70: {"A": 159, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 72, "TR_orientacion": 20.8, "TR_ejecutivo": 20.8},
    68: {"A": 155, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 121, "TR_alerta": 70, "TR_orientacion": 19.0, "TR_ejecutivo": 19.0},
    66: {"A": 151, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 101, "TR_alerta": 68, "TR_orientacion": 17.2, "TR_ejecutivo": 17.2},
    64: {"A": 147, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 99,  "TR_alerta": 65, "TR_orientacion": 15.4, "TR_ejecutivo": 15.4},
    62: {"A": 143, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 96, "TR_alerta": 63, "TR_orientacion": 13.6, "TR_ejecutivo": 13.6},
    60: {"A": 139, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 93, "TR_alerta": 61, "TR_orientacion": 11.8, "TR_ejecutivo": 11.8},
    58: {"A": 135, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 90, "TR_alerta": 59, "TR_orientacion": 9.9, "TR_ejecutivo": 9.9},
    56: {"A": 131, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 87, "TR_alerta": 57, "TR_orientacion": 8.1, "TR_ejecutivo": 8.1},
    54: {"A": 127, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 85, "TR_alerta": 54, "TR_orientacion": 6.3, "TR_ejecutivo": 6.3},
    52: {"A": 123, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 82, "TR_alerta": 52, "TR_orientacion":4.5, "TR_ejecutivo":4.5},
    50: {"A": 119, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 79, "TR_alerta": 50, "TR_orientacion": 2.7, "TR_ejecutivo": 2.7},
    48: {"A": 115, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 76, "TR_alerta": 48, "TR_orientacion": 0.9, "TR_ejecutivo": 0.9},
    46: {"A": 111, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 73, "TR_alerta": 46, "TR_orientacion": -0.9, "TR_ejecutivo": -0.9},
    44: {"A": 107, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 71, "TR_alerta": 43, "TR_orientacion": -2.7, "TR_ejecutivo": -2.7},
    42: {"A": 103, "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 68, "TR_alerta": 41, "TR_orientacion": -4.5, "TR_ejecutivo": -4.5},
    40: {"A": 99,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 65, "TR_alerta": 39, "TR_orientacion": -6.3, "TR_ejecutivo": -6.3},
    38: {"A": 95,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 62, "TR_alerta": 37, "TR_orientacion": -8.2, "TR_ejecutivo": -8.2},
    36: {"A": 91,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 59, "TR_alerta": 35, "TR_orientacion":-10.0 , "TR_ejecutivo":-10.0 },
    34: {"A": 87,   "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 57, "TR_alerta": 32, "TR_orientacion": -11.8, "TR_ejecutivo": -11.8},
    32: {"A": 83,   "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 54, "TR_alerta": 30, "TR_orientacion": -13.6, "TR_ejecutivo": -13.6},
    30: {"A": 79,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 51, "TR_alerta": 28, "TR_orientacion": -15.4, "TR_ejecutivo": -15.4},
    28: {"A": 75,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 48, "TR_alerta": 26, "TR_orientacion": -17.2, "TR_ejecutivo": -17.2},
    26: {"A": 71,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 45, "TR_alerta": 24, "TR_orientacion": -19.0, "TR_ejecutivo": -19.0},
    24: {"A": 67,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 43, "TR_alerta": 21, "TR_orientacion": -20.8, "TR_ejecutivo": -20.8},
    22: {"A": 63,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 40, "TR_alerta": 19, "TR_orientacion": -22.6, "TR_ejecutivo": -22.6},
    20: {"A": 59,  "C": 179,"O": 179,"F_A": 179,"F_TR": 179, "TR": 37, "TR_alerta": 17, "TR_orientacion": -24.4, "TR_ejecutivo":-24.4}
}


def obtener_ajuste_edad(edad):
    """
    Retorna los ajustes a aplicar a las PD según la edad
    Basado en las tablas del manual de ANT
    
    Args:
        edad: Edad del participante
        
    Returns:
        dict: Diccionario con ajustes para cada índice
    """
    if 16 <= edad <= 44:
        return {"A": 0, "C": 0, "O": 0, "F_A": 0, "F_TR": 0, "TR": 0, "TR_alerta": 0, "TR_orientacion": 0, "TR_ejecutivo": 0}
    elif 45 <= edad <= 64:
        return {"A": -8, "C": 0, "O": 0, "F_A": 0, "F_TR": 0, "TR": -4, "TR_alerta": -5, "TR_orientacion": 0, "TR_ejecutivo": 0}
    elif edad >= 65:
        return {"A": -14, "C": 0, "O": 0, "F_A": 0, "F_TR": 0, "TR": -11, "TR_alerta": -15, "TR_orientacion": 0, "TR_ejecutivo": 0}
    else:
        # Menores de 16 años, sin baremos específicos
        return {"A": 0, "C": 0, "O": 0, "F_A": 0, "F_TR": 0, "TR": 0, "TR_alerta": 0, "TR_orientacion": 0, "TR_ejecutivo": 0}


def obtener_PT_desde_PD(PD_ajustada, indice):
    """
    Obtiene la PT (Puntuación Típica) a partir de la PD ajustada
    
    Args:
        PD_ajustada: Puntuación directa ajustada por edad
        indice: 'A', 'C', 'O', 'F_A', 'F_TR', 'TR', 'TR_alerta', 'TR_orientacion' o 'TR_ejecutivo'
        
    Returns:
        int: Puntuación típica (20-80)
    """
    # Verificar si el baremo para este índice tiene valores reales (no placeholder 179)
    # Si todos los valores son 179, significa que no hay baremo disponible
    if all(BAREMOS_BASE[pt][indice] == 179 for pt in BAREMOS_BASE.keys()):
        # No hay baremo disponible, devolver PT=50 (normal) por defecto
        return 50
    
    # Para índices de error como C y O, menor es mejor (baremo inverso)
    if indice in ['C', 'O']:
        # Buscar en los baremos de menor a mayor PT (invertido)
        for pt in sorted(BAREMOS_BASE.keys()):
            if PD_ajustada <= BAREMOS_BASE[pt][indice]:
                return pt
        # Si es mayor que el máximo, devolver PT=20
        return 20
    else:
        # Para índices normales (A, TR, TR_alerta, etc.), mayor PD = mayor PT
        # Buscar en los baremos de mayor a menor PT
        for pt in sorted(BAREMOS_BASE.keys(), reverse=True):
            if PD_ajustada >= BAREMOS_BASE[pt][indice]:
                return pt
        
        # Si es menor que el mínimo, devolver PT=20
        return 20


def clasificar_PT(PT):
    """
    Clasifica una PT en bajo, normal o alto
    
    Args:
        PT: Puntuación típica
        
    Returns:
        str: 'bajo', 'normal' o 'alto'
    """
    if PT <= 30:
        return 'bajo'
    elif PT < 70:
        return 'normal'
    else:
        return 'alto'


def obtener_puntuaciones_tipicas(resultados):
    """
    Obtiene las puntuaciones típicas y clasificaciones basadas en las puntuaciones directas
    
    Args:
        resultados: Dict con puntuaciones directas y edad
        
    Returns:
        dict: Diccionario con clasificaciones en 3 niveles
    """
    edad = resultados['edad']
    
    # Obtener ajustes por edad
    ajustes = obtener_ajuste_edad(edad)

    # Procesar cada índice (A, C, O, F_A, F_TR, TR, TR_alerta, TR_orientacion, TR_ejecutivo)
    indices = ['A', 'C', 'O', 'F_A', 'F_TR', 'TR', 'TR_alerta', 'TR_orientacion', 'TR_ejecutivo']
    
    for indice in indices:
        # Obtener la puntuación directa
        pd_key = f'PD_{indice}'
        pd_value = resultados.get(pd_key, 0)
        
        # Aplicar ajuste por edad
        ajuste = ajustes.get(indice, 0)
        pd_ajustada = pd_value + ajuste
        
        # Obtener PT desde la PD ajustada
        pt = obtener_PT_desde_PD(pd_ajustada, indice)
        
        # Clasificar la PT
        clasificacion = clasificar_PT(pt)
        
        # Guardar PT y clasificación en resultados
        resultados[f'PT_{indice}'] = pt
        resultados[f'Clasificacion_{indice}'] = clasificacion

    # Crear diccionario de clasificaciones para retornar
    clasificaciones = {
        'A': resultados['Clasificacion_A'],
        'C': resultados['Clasificacion_C'],
        'O': resultados['Clasificacion_O'],
        'F_A': resultados['Clasificacion_F_A'],
        'F_TR': resultados['Clasificacion_F_TR'],
        'TR': resultados['Clasificacion_TR'],
        'TR_alerta': resultados['Clasificacion_TR_alerta'],
        'TR_orientacion': resultados['Clasificacion_TR_orientacion'],
        'TR_ejecutivo': resultados['Clasificacion_TR_ejecutivo'],
    }
    
    return clasificaciones

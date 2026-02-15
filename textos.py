"""
Módulo con los textos para generar el informe del test ANT
"""

# ============================================================================
# PÁRRAFOS FIJOS (siempre se incluyen)
# ============================================================================

PARRAFOS_FIJOS = {

    'titulo_general_prueba': """1. Objetivo de la prueba.""",
    'objetivo_prueba': """Esta prueba evalúa la eficiencia del funcionamiento de las tres redes o procesos atencionales que conforman la atención: alerta, orientación y control ejecutivo.
- Red de alerta o “arousal”. Se encarga de ayudarnos a mantener el estado de vigilancia y activación durante el día. Incrementa y mantiene el estado de activación general y voluntaria para prepararnos ante la posible aparición de un estímulo y la emisión de la respuesta a dicho estímulo.
- Red de orientación. Está implicada en los procedimientos de orientación y dirección de la atención hacia un evento, de manera voluntaria o involuntariamente. 
- Red de control ejecutivo. Se relaciona con todos los procesos que nos ayudan a regular nuestra conducta y cognición, reclutando y controlando áreas cerebrales necesarias para ejecutar tareas cognitivas complejas. Esta se encarga de inhibir información distractora, inhibir conductas habituales cuando no son necesarias y de monitorizar nuestra conducta de manera que podamos adaptarnos a las circunstancias cambiantes que se nos presentan en el entorno. Se pone en marcha en situaciones de procesamiento complejo y controlado.
Esta prueba es de utilidad para medir las capacidades atencionales de la persona. Y puede, por lo tanto, ser de utilidad para identificar algunas de las siguientes condiciones: Deterioro Cognitivo Leve, Demencia, Alzheimer, TDAH, o la eficacia de una intervención.
    """,


    'titulo_procedimiento': """2. Descripción de la tarea.""",
    'descripcion_procedimiento1': """En esta prueba el evaluado observa una serie de símbolos (estímulos) que aparecen en pantalla. Uno de estos símbolos es una flecha hacia la izquierda o la derecha en el centro de la pantalla. La tarea del evaluado consiste en lo más rápido y acertadamente posible contestar con las flechas del teclado, ⬅ o ➡, hacia qué lado indica la flecha de la pantalla. Este estímulo objetivo al que hay que responder aparece junto con el resto de los estímulos siguiendo un cierto orden, pero con un retardo en su aparición variable (puede tardar más o menos tiempo en aparecer). Además de estos dos estímulos, en la pantalla aparecerán otros que bien pueden ser: pistas, distractores o señales irrelevantes. El primer caso de esto es la aparición de uno, dos o ningún asterisco. Resulta que en las condiciones en que aparecen asteriscos frente a cuando no aparece ninguno, el participante recibe una pista de que el estímulo objetivo va a aparecer pronto. Además, cuando aparece un solo asterisco a uno de los lados de la cruz de fijación (una cruz constantemente situada en el centro de la pantalla), este siempre supone una pista de en qué lado va a aparecer la flecha. Estos 5 posibles asteriscos se ven tal que así:""",
    'descripcion_procedimiento2': """Finalmente, hay un último tipo de señal adicional que aparece en cada evento. Esto es, unas líneas rectas o flechas junto con la flecha central objetivo. En el caso de las flechas, estas pueden señalar en la misma u opuesta dirección de la flecha objetivo, resultando facilitadoras o engañosas respectivamente. De esta manera el centro de la pantalla a la hora de detectar la dirección de la flecha central se presenta como una de las siguientes 3 maneras:""",
    'descripcion_procedimiento3': """La prueba consiste en 4 bloques de eventos. El primero es un bloque de entrenamiento de 24 ensayos, en el cual el participante se familiariza con la tarea, mientras se le da retroalimentación de su rendimiento durante la misma. Después se realizan los otros 3 bloques experimentales, de 48 ensayos cada uno y sin retroalimentación. Los 48 ensayos de cada bloque comprenden todas las combinaciones de las diferentes condiciones de la tarea (4 según las pistas de orientación, 2 según las pistas de alerta, 3 según las líneas adicionales facilitadoras, distractoras o neutras, y 2 según la dirección de la flecha objetivo). En total la prueba dura unos 10 minutos aproximadamente.""",


    'titulo_indices': """
    3. Índices que se obtienen.""",
    'descripcion_indices': """Principalmente se consiguen dos puntuaciones en esta tarea: la precisión (A; porcentage de aciertos) y velocidad o tiempo de respuesta (TR). La precisión sirve para medir el rendimiento atencional general del evaluado. También se distinguen dos tipos de errores que nos dan información sobre el estilo atencional predominante: comisiones (C, respuestas dadas pero érroneamente) y omisiones (O, falta de respuesta). Por otro lado, el tiempo de respuesta sirve para medir tres aspectos atencionales muy específicos. La eficiencia de la red de alerta (TR_alerta) se calcula a partir de restar el tiempo de respuesta ante los eventos en condición de doble asterisco menos los eventos en condición de ningún asterisco. La eficiencia de la red de orientación (TR_orientación) se calcula de restar los tiempos de respuesta para los eventos con pista espacial (aparición de un asterisco del lado que aparecerá la flecha) menos el tiempo de respuesta antes los eventos sin pista espacial (aparición de un asterisco en el centro de la pantalla). Finalmente, la eficiencia de la red de control ejecutivo (TR_ejecutivo) se calcula restando el tiempo de respuesta en los eventos con flechas adicionales distractoras (incongruentes) menos el tiempo de respuesta en eventos con flechas adicionales facilitadoras (congruentes). Por último, otro índice que podemos obtener de esta prueba es en relación a la atención sostenida o grado de fatiga (F). Esto es la capacidad para mantener un rendimiento constante a lo largo de la prueba, sin cansarse o fatigarse. Ocurre que en caso de fatiga el rendimiento empeora hacia el final de la prueba, frente al principio. Este peor rendimiento debido a la fatiga se pude ver reflejado en una peor precisión (F_A; Aciertos al final - al principio de la prueba), o en un enlantecimiento del tiempo necesitado para responder (F_TR; Tiempo de Reacción al final - al principio de la prueba).""",
    
    'titulo_resultados': "Presentación de los resultados de {nombre_completo}",
    
    'texto_tabla_resultados': """En la siguiente tabla se muestra los resultados de {nombre} en la prueba ANT. Estos resultados se presentan como puntuación directa (PD) y como puntuación típica (PT). La puntuación típica es una calificación que compara la puntuación de {nombre} con la puntuación promedio y desviación típica de puntuaciones que los individuos de su edad tienden a obtener. La desviación típica representa con cuanta variabilidad los participantes de esta prueba puntúan por arriba o por debajo de la puntuación media. En pruebas como esta, en las que se espera una distribución normal de las puntuaciones, esta PT coincide en mayor medida con los percentiles, de manera que un PT de 50 equivaldría a un rendimiento en la prueba superior al 50% de los individuos de su edad, y lo mismo con un PT de 20 o 80 (valor mínimo y máximo respectivamente). Dicho esto, se muestra en la siguiente tabla los resultados obtenidos por {nombre} en esta prueba ANT:
    """,
}

# ============================================================================
# PÁRRAFOS CONDICIONALES SEGÚN PUNTUACIONES
# ============================================================================
# Se podría añadir un índice de fiabilidad basado en desviación típica

# PD_Total - Según puntuación directa total y correspondiente percentil
PARRAFO_A = {

    'A bajo':"""{nombre} muestra un porcentaje de aciertos bajo, lo que indica complicaciones para completar eficientemente la tarea presentada. Según este resultado, la capacidad atencional general resulta inferior a la media para su edad.""",

    'A normal':"""{nombre} muestra un porcentaje de aciertos normal, lo que indica una capacidad atencional general adecuada a la esperada para su edad.""",
    
    'A alto':"""{nombre} muestra un porcentaje de aciertos alto, lo que indica una capacidad atencional general superior a la media para su edad.""",
}

PARRAFO_C = {

    'C bajo':"""{nombre} presenta un número de errores de comisión bajo, lo que señala que pocas veces {nombre} emite una respuesta errónea. Este resultado señala una capacidad superior al promedio para discriminar la información de manera eficiente y una muy baja impulsividad a la hora de tomar decisiones. Así, esto podría ser también un indicador de la preferencia por un estilo atencional más reflexivo, con respuestas más lentas pero más precisas.""",

    'C normal':"""{nombre} presenta un número de errores de comisión normal, lo que señala que {nombre} emite un número de respuestas erróneas dentro de lo esperado para su edad. Este resultado señala una capacidad adecuada para discriminar la información de manera eficiente y una impulsividad dentro de lo esperado para su edad a la hora de tomar decisiones.""",

    'C alto':"""{nombre} presenta un número de errores de comisión alto, lo que señala que {nombre} emite un número de respuestas erróneas superior a lo esperado para su edad. Este resultado señala una capacidad inferior al promedio para discriminar la información de manera eficiente y una impulsividad superior a lo esperado para su edad a la hora de tomar decisiones. Así, esto podría ser también un indicador de la preferencia por un estilo atencional más impulsivo, con respuestas más rápidas pero menos precisas.""",
}

PARRAFO_O = {
    'O bajo':"""{nombre} presenta un número de errores de omisión bajo, lo que señala que pocas veces {nombre} no ha respondido cuando debería. Este resultado puede señalar una velocidad de procesamiento de la información y de toma de decisiones bien ajustada a la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad superior al promedio para mantener la atención sostenida a lo largo de la tarea, sin distraerse o fatigarse, y de manera que le impida emitir una respuesta en los momentos oportunos.""",

    'O normal':"""{nombre} presenta un número de errores de omisión normal, lo que señala que {nombre} no ha respondido cuando debería un número de veces dentro de lo esperado para su edad. Este resultado puede señalar una velocidad de procesamiento de la información y toma de decisiones adecuada a la exigencia temporal de la tarea. Otra dimensión atencional que puede medir este índice es una capacidad adecuada para mantener la atención sostenida a lo largo de la tarea, sin distraerse o fatigarse demasiado, y de manera que le impida emitir una respuesta en los momentos oportunos.""",
    
    'O alto':"""{nombre} presenta un número de errores de omisión alto, lo que señala que {nombre} no ha respondido cuando debería un número de veces superior a lo esperado para su edad. Este resultado puede señalar una velocidad de procesamiento de la información y toma de decisiones demasiado lenta para la exigencia temporal de la tarea. Otra explicación puede ser debido a una capacidad inferior al promedio para mantener la atención sostenida a lo largo de la tarea. Con tendencia a distraerse o fatigarse, lo que le dificulta emitir una respuesta en los momentos oportunos.""",
}

PARRAFO_F = {
    'F_A bajo y F_TR bajo':"""El rendimiento de {nombre} durante la tarea ha ido mejorando con el avance de la misma, mostrando mejor precisión y velocidad de respuesta al final de la prueba que al principio. Esto indica una buena atención sostenida y resistencia a la fatiga. {nombre} muestra un desempeño especialmente bueno ante tareas simples y repetitivas, las cuales con el tiempo es capaz de automatizar a la perfección, sin cansarse o aburrirse.""", 

    'F_A bajo y F_TR normal':"""{nombre} muestra una velocidad de respuesta que se mantiene constante a lo largo de la prueba, y una precisión que incluso mejora según avanza la misma. Esto indica una buena atención sostenida y resistencia a la fatiga. {nombre} muestra un desempeño especialmente bueno ante tareas simples y repetitivas, las cuales con el tiempo es capaz de automatizar a la perfección, sin cansarse o aburrirse.""",

    'F_A bajo y F_TR alto':"""{nombre} muestra una precisión de respuesta que aumenta con el avance de la tarea, mientras que la velocidad de respuesta se ralentiza a lo largo de la prueba. Esto indica una clara preferencia de {nombre} por un estilo atencional más reflexivo, con la adopción de un procesamiento de la información más lento pero preciso. {nombre} parece ser muy capaz de automatizar eficazmente tareas simples y repetitivas. Aunque, a su vez, la falta de excitación de esta tarea monótona le supone un mayor esfuerzo y cansancio por mantener la atención sostenida. Finalmente, {nombre} presenta un importante enlantecimiento en su velocidad de trabajo, el cual puede deberse en parte a la fatiga. O a la preferencia y adopción de un estilo atencional más reflexivo con el transcurso de la tarea.""",
    
    'F_A normal y F_TR bajo':"""{nombre} muestra una precisión de respuesta constante a lo largo de la tarea, mientras que la velocidad de respuesta aumenta con el avance de la tarea. Esto indica una excelente capacidad de automatización de la tarea, especialmente ante tareas simples y repetitivas como esta. Esta habilidad es útil para reducir el esfuerzo ante tareas monótonas y poco estimulantes, y reducir así el cansancio generado. O incluso, en este caso, aumentando la velocidad con la que se realiza la tarea, sin perder calidad en la precisión.""",
    
    'F_A normal y F_TR normal':"""muestra una rendimiento sumamente constante a lo largo de la prueba, sin que su precisión y velocidad de respuesta se vean afectadas. Esto indica una excelente capacidad de atención sostenida y resistencia a la fatiga, incluso, o especialmente, ante tareas simples monótonas como esta.""",

    'F_A normal y F_TR alto':"""{nombre} muestra una precisión de respuesta constante a lo largo de la tarea, mientras que la velocidad de respuesta se ralentiza. Esto indica dos cosas. Por un lado, el enlantecimiento en su velocidad de trabajo sugiere en {nombre} una baja resistencia a la fatiga ante tareas monótonas y poco estimulantes. Por otro lado, este resulta indica la preferencia de {nombre} por un estilo atencional más reflexivo. De esta manera, ante la aparición de cansancio, {nombre} decide tomarse más tiempo en su respuesta, y así poder seguir procesando la información de manera precisa y consciente.""",

    'F_A alto y F_TR bajo':"""{nombre} muestra una aceleración de su velocidad de respuesta con el avance de la tarea, aunque de la mano de un empeoramiento de su precisión. Esto indica dos cosas. Primero, la aparición de cansancio con el avance de la tarea, especialmente ante tareas monótonas y poco estimulantes. En segundo lugar, una clara preferencia y adopción de {nombre} por un estilo atencional más impulsivo, con respuestas más rápidas pero menos precisas. {nombre} parece tener dificultades para reunir una motivación más intrínseca en el desempeño de la tarea. Y así, ante la falta de estimulación, se cansa o aburre más que lo esperado para su edad, afectando negativamente a su esfuerzo, atención sostenida y rendimiento durante la tarea.""",
    
    'F_A alto y F_TR normal':"""{nombre} muestra una velocidad de respuesta constante, pero un empeoramiento de su precisión con el avance de la tarea. Esto es indicativo de una baja resistencia a la fatiga, especialmente ante tareas monótonas y poco estimulantes como esta. Con la aparición de cansancio, {nombre} podría esforzarse más para mantener una buena precisión y calidad de respuesta, a costa de tomarse más tiempo para pensar y responder. Pero en este caso, parece que {nombre}, bien por falta de capacidad o de motivación, no adopta este estilo atencional más reflexivo, eficaz ante la aparición de cansancio y deterioro en la calidad de la ejecución.""",

    'F_A alto y F_TR alto':"""{nombre} muestra un enlantecimiento de su velocidad de respuesta y un empeoramiento de su precisión con el avance de la tarea. Esto indica una muy baja resistencia al cansancio o el aburrimiento, especialmente ante tareas monótonas y poco estimulantes como esta. Según este índice {nombre} tiene grandes dificultades para mantener la atención sostenida lo que le lleva a no responder o responder erratica o aleatoriamente ante una tarea. Parece así que el rendimiento de {nombre} dependerá más de cuán estimulante le resulte una actividad. Y tiene por tanto, dificultades para reunir motivación más intrínseca en el desempeño de una tarea, y así poder realizar también estas actividades más monótonas o aburridas pero igualmente importantes para la vida diaria.""",
    }

PARRAFO_TR = {

    'TR bajo':"""{nombre} muestra un tiempo de respuesta bajo, lo que indica una velocidad de procesamiento de la información y toma de decisiones superior a la media para su edad. Aunque esta mayor velocidad también puede ser debida a un estilo atencional más impulsivo, con respuestas más rápidas aunque menos precisas. Véase el número de errores de comisión para valorar esta posibilidad.""",

    'TR normal':"""{nombre} muestra un tiempo de respuesta normal, lo que indica una velocidad de procesamiento de la información y toma de decisiones adecuada a la media para su edad.""",
    
    'TR alto':"""{nombre} muestra un tiempo de respuesta alto, lo que indica una velocidad de procesamiento de la información y toma de decisiones inferior a la media para su edad. Este resultado puede señalar la necesidad de {nombre} de más tiempo para  """,
}

PARRAFO_alerta = {

    'TR_alerta bajo':"""{nombre} mostró una eficiencia de la red de alerta superior a la media para su edad. Esto se traduce en una excelente capacidad para mantener un alto estado de vigilancia y activación. Es decir, que {nombre} ha estado especialmente despierto durante la tarea. Esto le permite reconectar y atender rápidamente con la tarea en los momentos que aparece información relevante.""",

    'TR_alerta normal':"""{nombre} mostró una eficiencia de la red de alerta adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para mantener un estado de vigilancia y activación durante la tarea. Es decir, que {nombre} ha estado suficientemente despierto durante la tarea. Esto le permite reconectar y atender adecuadamente con la tarea en los momentos que aparece información relevante.""",
    
    'TR_alerta alto':"""{nombre} mostró una eficiencia de la red de alerta inferior a la media para su edad. Esto se traduce en una capacidad limitada por dificultades para mantener un alto estado de vigilancia y activación. Es decir, parece que {nombre} ha estado poco despierto durante la tarea. Esto le dificulta reconectar y atender adecuadamente con la tarea en los momentos que aparece información relevante.""",
}
PARRAFO_orientacion = {

    'TR_orientacion bajo':"""Respecto a la red de orientación, {nombre} mostró una eficiencia superior a la media para su edad. Esto se traduce en una excelente capacidad para orientar y dirigir la atención hacia los eventos relevantes de la tarea.""",

    'TR_orientacion normal':"""Respecto a la red de orientación, {nombre} mostró una eficiencia adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para orientar y dirigir la atención hacia los eventos relevantes de la tarea.""",
    
    'TR_orientacion alto':"""Respecto a la red de orientación, {nombre} mostró una eficiencia inferior a la media para su edad. Esto se traduce en una capacidad limitada por dificultades para orientar y dirigir la atención hacia los eventos relevantes de la tarea.""",
}
PARRAFO_ejecutivo = {

    'TR_ejecutivo bajo':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo superior a la media para su edad. Esto se traduce en una excelente capacidad para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un alto control para procesar y ejecutar tareas complejas.""",

    'TR_ejecutivo normal':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo adecuada a la media para su edad. Esto se traduce en una capacidad adecuada para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un control adecuado para procesar y ejecutar tareas complejas.""",
    
    'TR_ejecutivo alto':"""Finalmente, {nombre} mostró una eficiencia de la red de control ejecutivo inferior a la media para su edad. Esto se traduce en una capacidad limitada por dificultades para inhibir la información irrelevante y distractora y las respuestas impulsivas durante la tarea. Así, mostrando {nombre} un control limitado para procesar y ejecutar tareas complejas.""",
}
"""
Módulo para generar el informe en formato DOCX
"""
import os
from datetime import datetime
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from PIL import Image
from textos import (
    PARRAFOS_FIJOS, PARRAFO_A, PARRAFO_C, PARRAFO_O, PARRAFO_S, PARRAFO_TR, PARRAFO_ejecutivo, PARRAFO_alerta, PARRAFO_orientacion,
)

def agregar_portada(doc: Document, nombre_completo: str, datos: dict) -> None:
    """
    Agrega la portada del informe
    
    Args:
        doc: Documento de Word
        nombre_completo: Nombre completo del encuestado
        datos: Diccionario con datos generales (edad, fecha_aplicacion, etc.)
    """
    # Título
    titulo = doc.add_heading('PRUEBA ANT, Test de Redes Atencionales', 0)
    titulo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    # Aumentar tamaño de fuente del título
    for run in titulo.runs:
        run.font.size = Pt(24)
    
    # Espacio
    doc.add_paragraph().add_run().add_break()
    
    # Información del participante
    info = doc.add_paragraph()
    info.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    # Nombre del encuestado
    nombre_run = info.add_run(f"Nombre del encuestado: {nombre_completo}\n")
    nombre_run.bold = True
    nombre_run.font.size = Pt(14)
    
    # Edad
    if datos.get('edad'):
        edad_run = info.add_run(f"Edad: {datos['edad']} años\n")
        edad_run.font.size = Pt(14)
    
    # Fecha de aplicación (si está disponible)
    if datos.get('fecha_aplicacion'):
        fecha_app_run = info.add_run(f"Fecha de aplicación: {datos['fecha_aplicacion']}\n")
        fecha_app_run.font.size = Pt(14)
    
    # Fecha del informe
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    fecha_informe_run = info.add_run(f"Fecha del informe: {fecha_actual}\n")
    fecha_informe_run.font.size = Pt(14)
    
    # Espacio
    doc.add_paragraph().add_run().add_break()
    
    # Nota confidencial
    nota = doc.add_paragraph()
    nota.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    nota_run = nota.add_run(f"Este es un informe de evaluación cognitiva, obtenido a partir del rendimiento de {nombre_completo} en la prueba ANT (Test de Redes Atencionales).")
    doc.add_paragraph()  # Espacio
    nota.add_run("\n" + "-" * 50 + "\n")  # Línea de separación
    nota.add_run("\nInforme confidencial de uso profesional y educativo")
    nota_run.italic = True
    nota_run.font.size = Pt(12)

def crear_informe_docx(resultados, clasificaciones, nombre_caso="caso", scale_factor_width=0.8, scale_factor_height=0.5):
    """
    Crea el documento Word con el informe del test ANT
    
    Args:
        resultados: Dict con puntuaciones directas y datos del encuestado
        clasificaciones: Dict con clasificaciones (PT)
        nombre_caso: Nombre del evaluado (fallback si no está en resultados)
        
    Returns:
        Document: Documento Word generado
    """
    doc = Document()
    
    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
    
    # Extraer nombres de resultados
    nombre_completo = resultados.get('nombre_completo') or nombre_caso
    nombre = resultados.get('nombre') or nombre_caso
    
    # Preparar datos para la portada
    datos_portada = {
        'edad': resultados.get('edad'),
        'fecha_aplicacion': resultados.get('fecha_aplicacion')
    }
    
    # 1. PORTADA (Primera página)
    agregar_portada(doc, nombre_completo, datos_portada)
    doc.add_page_break()
    
    # ========================================================================
    # TÍTULO E INTRODUCCIÓN
    # ========================================================================
    # ========================================================================
    # DESCRIPCIÓN DE LA PRUEBA
    # ========================================================================
    
    parrafo = doc.add_paragraph()
    run = parrafo.add_run(PARRAFOS_FIJOS['titulo_general_prueba'])
    run.bold = True
    doc.add_paragraph(PARRAFOS_FIJOS['objetivo_prueba'])

    parrafo = doc.add_paragraph()
    run = parrafo.add_run(PARRAFOS_FIJOS['titulo_procedimiento'])
    run.bold = True
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento1'])
    
    # Imagen parte spatial cueing
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
    grafico_path = os.path.join(script_dir, 'spatial cue.png')
    if os.path.exists(grafico_path):
        try:
            # Obtener dimensiones de la imagen
            img = Image.open(grafico_path)
            width, height = img.size
            # Aplicar factor de escala
            new_width = Inches(width / 96 * scale_factor_width)  # 96 DPI
            new_height = Inches(height / 96 * scale_factor_height)
            # Agregar imagen
            doc.add_picture(grafico_path, width=new_width, height=new_height)
            last_paragraph = doc.paragraphs[-1]
            last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        except Exception as e:
            print(f"Advertencia: No se pudo insertar la imagen spatial cue.png: {e}")
    
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento2'])
    
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento3'])
    
    # Imagen parte PC
    grafico_path = os.path.join(script_dir, 'congruency cue.png')
    if os.path.exists(grafico_path):
        try:
            img = Image.open(grafico_path)
            width, height = img.size
            new_width = Inches(width / 96 * scale_factor_width)
            new_height = Inches(height / 96 * scale_factor_height)
            doc.add_picture(grafico_path, width=new_width, height=new_height)
            last_paragraph = doc.paragraphs[-1]
            last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        except Exception as e:
            print(f"Advertencia: No se pudo insertar la imagen congruency cue.png: {e}")

    parrafo = doc.add_paragraph()
    run = parrafo.add_run(PARRAFOS_FIJOS['titulo_indices'])
    run.bold = True
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_indices'])
    doc.add_page_break()

    # ========================================================================
    # INSERTAR Tabla resultados
    # ========================================================================
    
    # Título de resultados
    titulo_resultados = doc.add_paragraph()
    titulo_resultados.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = titulo_resultados.add_run(PARRAFOS_FIJOS['titulo_resultados'].format(nombre_completo=nombre_completo))
    run.bold = True
    run.font.size = Pt(14)
    doc.add_paragraph()  # Espacio
    
    doc.add_paragraph(PARRAFOS_FIJOS['texto_tabla_resultados'].format(nombre=nombre, nombre_completo=nombre_completo))

    # Tabla PDs, PTs y clasificaciones
    tabla = doc.add_table(rows=4, cols=6)

    # Aplicar estilo simple con bordes negros y encabezado con fondo gris claro
    tabla.style = 'Table Grid'
    # Aplicar fondo gris claro al encabezado
    for cell in tabla.rows[0].cells:
        cell._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w'))))
    
    # Encabezados
    hdr_cells = tabla.rows[0].cells
    hdr_cells[0].text = ''
    hdr_cells[1].text = 'Aciertos (A)'
    hdr_cells[2].text = 'Comisiones (C)'
    hdr_cells[3].text = 'Omisiones (O)'
    hdr_cells[4].text = 'Fatiga precisión (F_A)'
    hdr_cells[5].text = 'Velocidad de respuesta (TR)'
    hdr_cells[6].text = 'Fatiga velocidad de respuesta (F_TR)'
    hdr_cells[7].text = 'Eficaciencia de la red de alerta (TR_alerta)'
    hdr_cells[8].text = 'Eficaciencia de la red de orientación (TR_orientacion)'
    hdr_cells[9].text = 'Eficaciencia de la red ejecutiva (TR_ejecutivo)'


    # Centrar el texto en las celdas del encabezado
    for cell in hdr_cells:
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            
    # Fila 1: PD (Puntuación Directa)
    row1 = tabla.rows[1].cells
    row1[0].text = 'Puntuación Directa (PD)'
    row1[1].text = str(resultados.get('PD_A', 0))
    row1[2].text = str(resultados.get('PD_C', 0))
    row1[3].text = str(resultados.get('PD_O', 0))
    row1[4].text = str(resultados.get('PD_F_A', 0))
    row1[5].text = str(resultados.get('PD_TR', 0))
    row1[6].text = str(resultados.get('PD_F_TR', 0))
    row1[7].text = str(resultados.get('PD_TR_alerta', 0))
    row1[8].text = str(resultados.get('PD_TR_orientacion', 0))
    row1[9].text = str(resultados.get('PD_TR_ejecutivo', 0))
    
    # Fila 2: PT (Puntuación Típica) - E no tiene PT
    row2 = tabla.rows[2].cells
    row2[0].text = 'Puntuación Típica (PT)'
    row2[1].text = str(resultados.get('PT_A', 0))
    row2[2].text = str(resultados.get('PT_C', 0))
    row2[3].text = str(resultados.get('PT_O', 0))
    row2[4].text = str(resultados.get('PT_F_A', 0))
    row2[5].text = str(resultados.get('PT_TR', 0))
    row2[6].text = str(resultados.get('PT_F_TR', 0))
    row2[7].text = str(resultados.get('PT_TR_alerta', 0))
    row2[8].text = str(resultados.get('PT_TR_orientacion', 0))
    row2[9].text = str(resultados.get('PT_TR_ejecutivo', 0))
    
    # Fila 3: Clasificación (bajo/normal/alto)
    row3 = tabla.rows[3].cells
    row3[0].text = 'Rendimiento'
    row3[1].text = str(resultados.get('Clasificacion_A', '-'))
    row3[2].text = str(resultados.get('Clasificacion_C', '-'))
    row3[3].text = str(resultados.get('Clasificacion_O', '-'))
    row3[4].text = str(resultados.get('Clasificacion_F_A', '-'))
    row3[5].text = str(resultados.get('Clasificacion_F_TR', '-'))
    row3[6].text = str(resultados.get('Clasificacion_TR', '-'))
    row3[7].text = str(resultados.get('Clasificacion_TR_alerta', '-'))
    row3[8].text = str(resultados.get('Clasificacion_TR_orientacion', '-'))
    row3[9].text = str(resultados.get('Clasificacion_TR_ejecutivo', '-'))

    # Centrar el texto en las celdas de las filas 1, 2 y 3
    for row in [row1, row2, row3]:
        for cell in row:
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph()  # Espacio

    # ========================================================================
    # PÁRRAFOS CONDICIONALES
    # ========================================================================

    # Construir clave para buscar el párrafo condicional A, C, O 
    clas_A = resultados.get('Clasificacion_A', 'normal')
    clas_C = resultados.get('Clasificacion_C', 'normal')
    clas_O = resultados.get('Clasificacion_O', 'normal')
    clas_F_A = resultados.get('Clasificacion_A', 'normal')
    clas_F_TR = resultados.get('Clasificacion_F_TR', 'normal')
    clas_TR = resultados.get('Clasificacion_TR', 'normal')
    clas_TR_alerta = resultados.get('Clasificacion_TR_alerta', 'normal')
    clas_TR_orientacion = resultados.get('Clasificacion_TR_orientacion', 'normal')
    clas_TR_ejecutivo = resultados.get('Clasificacion_TR_ejecutivo', 'normal')
    
    # Función auxiliar para buscar la clave correcta en el diccionario
    def encontrar_clave_PT(a, c, o, f_a, f_tr, tr, tr_alerta, tr_orientacion, tr_ejecutivo):
        """Genera posibles claves y busca en PARRAFOS_PT"""
  
            posibles_claves = [
                    f'P {a} C {c} O {o} F_A {f_a} F_TR {f_tr} TR {tr} TR_alerta {tr_alerta} TR_orientacion {tr_orientacion} TR_ejecutivo {tr_ejecutivo}',
                    f'P {a} C {c} O {o}',  # Clave simplificada
                    f'P {a}',  # Solo A
                    f'C {c}',  # Solo C
                    f'O {o}',  # Solo O
                    f'F_A {f_a}',  # Solo F_A
                    f'F_TR {f_tr}',  # Solo F_TR
                    f'TR {tr}',  # Solo TR
                    f'TR_alerta {tr_alerta}',  # Solo TR_alerta
                    f'TR_orientacion {tr_orientacion}',  # Solo TR_orientacion
                    f'TR_ejecutivo {tr_ejecutivo}'  # Solo TR_ejecutivo
                ]
                for clave in posibles_claves:
                    if clave in PARRAFOS_PT:
                        return clave
                return None

    # Buscar y añadir párrafo correspondiente
    texto_condicional = ""
    clave_PT = encontrar_clave_PT(clas_A, clas_C, clas_O, clas_F_A, clas_F_TR, clas_TR, clas_TR_alerta, clas_TR_orientacion, clas_TR_ejecutivo)
    
    if clave_PT and clave_PT in PARRAFOS_PT:
        texto_pt = PARRAFOS_PT[clave_PT].format(nombre=nombre)
        texto_condicional += texto_pt
    else:
        # Si no se encuentra la clave, agregar mensaje de debug
        print(f"Advertencia: No se encontró texto para A={clas_A}, C={clas_C}, O={clas_O}")
        texto_condicional += f"Resultados: A={clas_A}, C={clas_C}, O={clas_O}. "


    # Añadir todo el texto condicional al documento en un solo párrafo
    doc.add_paragraph(texto_condicional)

    # ========================================================================
    return doc

def guardar_informe(doc, ruta_salida):
    """
    Guarda el documento generado
    
    Args:
        doc: Documento Word
        ruta_salida: Ruta donde guardar el archivo
    """
    doc.save(ruta_salida)
    print(f"Informe generado exitosamente en: {ruta_salida}")

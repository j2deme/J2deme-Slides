# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding: utf-8
"""
Author Jaime Jesús Delgado Meraz <j2deme>
"""

import os
import sys
import json
from time import sleep
import questionary
import click

from rich import print  # Overrides print() function
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress

error_console = Console(stderr=True, style="bold red")

SOURCE_DIR = "src"
DIST_DIR = "dist"
CLASS_TEMPLATE = "src/templates/Clase.md"
CONFERENCE_TEMPLATE = "src/templates/Ponencia.md"
MARP_COMMAND = "marp"

# Revisa si marp.exe esta disponible en el sistema
# Si no está disponible, usa npx marp
try:
    if os.system("marp --version > NUL 2>&1") != 0:
        MARP_COMMAND = "npx marp"
except Exception as e:
    error_console.print(f"[bold red]Error checking marp version: {e}")

# MARK: SLIDE LIST


def get_slides():
    """
    Obtiene una lista de archivos .md en la carpeta SOURCE_DIR

    Returns:
        False si no existen archivos .md en la carpeta SOURCE_DIR
        Una lista de archivos .md si existen archivos en la carpeta SOURCE_DIR
    """
    slides = [file for file in os.listdir(SOURCE_DIR) if file.endswith(".md")]

    if len(slides) == 0:
        return False
    else:
        return slides

# MARK: THEME SELECTOR


def theme_selector(answer=True):
    """
    Muestra una tabla con los temas disponibles y permite al usuario seleccionar uno.

    Args:
        answer (bool, optional): Indica si se espera una respuesta del usuario.
                                Si es True, se muestra un formulario para seleccionar el tema.
                                Si es False, se espera que el usuario presione enter para regresar al menú principal.
                                Por defecto es True.

    Returns:
        dict: Un diccionario que contiene los colores primario y secundario del tema seleccionado.
    """
    themes = {
        "Default": {
            "primary": "#1274c5",
            "secondary": "#c22344"
        },
        "Sky": {
            "primary": "#3b82f6",
            "secondary": "#d97706"
        },
        "Blue": {
            "primary": "#2563eb",
            "secondary": "#ebad25"
        },
        "Indigo": {
            "primary":  "#4f46e5",
            "secondary": "#e11d48"
        },
        "Purple": {
            "primary": "#7e22ce",
            "secondary": "#fb923c"
        },
        "Green": {
            "primary": "#22c55e",
            "secondary": "#c026d3"
        },
        "Yellow": {
            "primary": "#f59e0b",
            "secondary": "#3b82f6"
        },
        "Red": {
            "primary": "#E11D48",
            "secondary": "#0EA5E9"
        },
        "Orange": {
            "primary": "#f97316",
            "secondary": "#9333ea"
        },
        "Laravel": {
            "primary": "#f05340",
            "secondary": "#f0ab40"
        },
        "Mindstorms": {
            "primary": "#049f98",
            "secondary": "#881560"
        }
    }

    table = Table(show_header=True, header_style="bold",
                  title="Temas", title_style="bold cyan")
    table.add_column("Nombre")
    table.add_column("Color primario")
    table.add_column("Color secundario")

    for theme in themes:
        table.add_row(theme,
                      Text(themes[theme]['primary'].upper(),
                           style=themes[theme]['primary']),
                      Text(themes[theme]['secondary'].upper(),
                           style=themes[theme]['secondary']))

    print(table)

    if answer == True:
        answers = questionary.form(
            theme=questionary.select(
                "¿Qué tema quieres usar?", choices=themes, pointer="👉")
        ).ask()

        return themes[answers['theme']]
    else:
        questionary.press_any_key_to_continue(
            message="Presiona cualquier tecla para continuar...").ask()
        main()


# MARK: SLIDE FROM JSON


def slide_from_json():
    """
    Crea una presentación a partir de los datos de un archivo JSON.

    Returns:
        dict: Un diccionario que contiene los datos de la presentación.
    """
    # Establece el directorio actual como ruta de trabajo
    path = os.getcwd()
    subjects_path = f"{path}/src/subjects.json"

    # Revisa si existe subjects.json y si existe, lee el archivo
    if os.path.exists(subjects_path):
        with open(subjects_path, 'r', encoding="utf-8") as file:
            data = json.load(file)

        # Revisa si hay materias en el archivo y las muestra para seleccionar una
        if len(data) > 0:
            subjects = [questionary.Choice(
                title=f"{subject["name"]} ({subject['code']})", value=subject) for subject in data]

            subject = questionary.select(
                "¿De qué materia quieres crear la presentación?", choices=subjects, pointer="👉").ask()

            # Revisa si la materia tiene unidades y si no está vacía
            if "units" not in subject or len(subject["units"]) == 0:
                print("[bold red]No hay unidades disponibles para esta materia ❌")
                sleep(2)
                main()

            units = [questionary.Choice(title=f"{unit["unit"]}. {
                                        unit["name"]}", value=unit) for unit in subject["units"]]

            unit = questionary.select(
                "¿De qué unidad quieres crear la presentación?", choices=units, pointer="👉").ask()

            # Si la materia no tiene un "theme" definido, establece uno por default
            if 'theme' in subject:
                theme = subject["theme"]
            else:
                theme = {
                    "primary": "#1274c5",
                    "secondary": "#c22344"
                }

            return {
                'subject': subject["name"],
                'unit': unit["unit"],
                'unit_name': unit["name"],
                'topics': unit["topics"],
                'skill': unit["skill"],
                'code': subject["code"],
                'satca': subject["satca"],
                'careers': subject["careers"],
                'primary': theme["primary"],
                'secondary': theme["secondary"]
            }
        else:
            print("[bold red]No hay datos de materias disponibles ❌")
            sleep(2)
            main
    else:
        print("[bold red]El archivo de materias no existe ❌")
        sleep(2)
        main()

# MARK: NEW CLASS


def new_class_slide():
    """
    Crea una nueva presentación de clase.

    Returns:
        None
    """

    # Pregunta al usuario si desea seleccionar una materia de un archivo JSON o ingresar los datos manualmente
    action = questionary.select(
        "¿Cómo quieres crear la presentación?", choices=['Manual', 'Desde JSON'], pointer="👉").ask()

    if action == 'Desde JSON':
        manual = False
        answers = slide_from_json()
    else:
        manual = True
        answers = questionary.form(
            subject=questionary.text("Materia"),
            unit=questionary.text("Unidad"),
            unit_name=questionary.text("Nombre de la unidad"),
            code=questionary.text("Clave", default="ABC - 999"),
            satca=questionary.text("SATCA", default="9 - 9 - 9"),
        ).ask()

        theme = theme_selector()
        answers['primary'] = theme['primary']
        answers['secondary'] = theme['secondary']

    # Si la unidad es menor a 10, se agrega un cero al inicio
    unit = f"0{answers['unit']}" if int(
        answers['unit']) < 10 else f"{answers['unit']}"

    subject_name = answers['subject']
    acronym = __generate_acronym(answers)

    # Título de la presentación y nombre del archivo
    title = f"{subject_name} - {unit} - {answers['unit_name']}"
    filename = f"{acronym}-{unit}_{answers['code'].replace(' ', '')}"

    if manual == True:
        answers['careers'] = ": Ingeniería en Sistemas Computacionales"
        # TOC de la presentación
        answers['toc'] = "1. [Tema 1](#tema-1)\n2. [Tema 2](#tema-2)\n\n"
        # Placeholder para la competencia específica de la unidad
        answers['contents'] += "---\n\n# Competencia específica de la unidad\n\n"
        answers['contents'] += f"> Competencia específica de la unidad {
            unit}\n\n"
        # Temas de la presentación
        answers['contents'] += "---\n\n<!-- _class: lead -->\n# Tema 1\n\n---\n\n# Tema 1\n\n"
        answers['contents'] += "---\n\n<!-- _class: lead -->\n# Tema 2\n\n---\n\n# Tema 2\n\n"

    else:
        careers = ""
        for career in answers['careers']:
            careers += f": {career}\n"

        answers['contents'] = ""
        answers['toc'] = ""
        topics = []
        subtopics = []

        for idx, topic in enumerate(answers['topics']):
            # Algunos temas pueden tener subtemas
            if isinstance(topic, dict):
                subtopics.append(topic['topics'])
                topic = topic['name']
                topics.append(topic)
            else:
                topics.append(topic)
                subtopics.append(None)

            hyphenated = topic.replace(' ', '-').lower()
            answers['toc'] += f"{idx + 1}. [{topic}](#{hyphenated})"

            if idx + 1 < len(answers['topics']):
                answers['toc'] += "\n"

        # answers['contents'] += "\n---\n\n"
        answers['contents'] += "# Competencia específica de la unidad\n\n"
        if isinstance(answers['skill'], list):
            for skill in answers['skill']:
                answers['contents'] += f"> {skill}\n\n"
        else:
            answers['contents'] += f"> {answers['skill']}\n\n"

        for idx, topic in enumerate(topics):
            answers['contents'] += f"---\n\n<!-- _class: lead -->\n# {
                topic}\n\n"
            answers['contents'] += f"---\n\n# {topic}\n\n"

            # Si el tema tiene subtemas, se agregan a la presentación
            if subtopics[idx] is not None:
                for subtopic in subtopics[idx]:
                    answers['contents'] += f"---\n\n# {topic}\n\n"
                    answers['contents'] += f"## {subtopic}\n\n"

        # Elimina 2 saltos de línea al final de answers[contents]
        answers['contents'] = answers['contents'][:-2]

    # Toma como base el archivo CLASS_TEMPLATE, reemplaza las variables y crea un nuevo archivo
    with open(CLASS_TEMPLATE, 'r', encoding="utf-8") as file:
        filedata = file.read()
        filedata = filedata.replace(
            '===TITLE===', title).replace(
            '===HEADER===', f"{answers['subject']} - U{answers['unit']}").replace(
            '===SUBJECT===', answers['subject']).replace(
            '===UNIT===', answers['unit']).replace(
            '===UNIT_NAME===', answers['unit_name']).replace(
            '===CODE===', answers['code']).replace(
            '===SATCA===', answers['satca']).replace(
            '===PRIMARY_COLOR===', answers['primary']).replace(
            '===SECONDARY_COLOR===', answers['secondary']).replace('===CONTENTS===', answers['contents']).replace('===CAREERS===', careers).replace('===TOC===', answers['toc'])

        # Revisa si el archivo ya existe
        if os.path.exists(f"{SOURCE_DIR}/{filename}.md"):
            # Pregunta al usuario si desea sobreescribir el archivo
            overwrite = questionary.confirm(
                f"¿Deseas sobreescribir {filename}.md?").ask()

            if overwrite == False:
                # Ofrecer al usuario la opción de agregar un texto adicional al nombre del archivo en lugar de un número
                add_text = questionary.confirm(
                    "¿Quieres agregar un texto adicional al nombre del archivo?").ask()

                if add_text == True:
                    additional = questionary.text('Texto adicional').ask()
                    if additional != "":
                        # Elimina espacios adicionales y reemplaza los espacios por guiones
                        suffix = additional.strip().replace(' ', '-')
                    else:
                        suffix = "99"

                    filename = f"{filename}-{suffix}"
                else:
                    i = 1
                    while os.path.exists(f"{SOURCE_DIR}/{filename}-{i}.md"):
                        i += 1
                    filename = f"{filename}-{i}"

        with open(f"{SOURCE_DIR}/{filename}.md", 'w', encoding="utf-8") as new_file:
            new_file.write(filedata)
            print(
                f"[bold green]Presentación para {answers['subject']} - U{answers['unit']} creada con éxito ✅")

# MARK: NEW SPEECH


def new_speech_slide():
    """
    Crea una nueva presentación de ponencia.

    Returns:
        None
    """
    answers = questionary.form(
        title=questionary.text("Título"),
        subtitle=questionary.text("Subtítulo", default=""),
        # author=questionary.text("Autor"),
        # date=questionary.text("Fecha"),
        # event=questionary.text("Evento"),
    ).ask()

    theme = theme_selector()

    # Toma como base el archivo CONFERENCE_TEMPLATE, reemplaza las variables y crea un nuevo archivo
    with open(CONFERENCE_TEMPLATE, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(
            '===TITLE===', answers['title']).replace(
            '===SUBTITLE===', answers['subtitle']).replace(
            '===PRIMARY_COLOR===', theme['primary']).replace(
            '===SECONDARY_COLOR===', theme['secondary']).replace(
            '===HEADER===', answers['title'])
        # .replace('===DATE===', answers['date'])
        # .replace('===EVENT===', answers['event'])

        filename = answers['title'].replace(' ', '-')

        with open(f"{SOURCE_DIR}/{filename}.md", 'w') as new_file:
            new_file.write(filedata)
            print(
                f"[bold green]Presentación para {answers['title']} creada con éxito ✅")

# MARK: TYPE SELECTOR


def new_slide():
    """
    Crea una nueva presentación.

    Pregunta al usuario qué tipo de presentación desea crear y
    redirige a la función correspondiente según la respuesta.

    Opciones disponibles:
    - Clase: Crea una diapositiva para una clase.
    - Ponencia: Crea una diapositiva para una ponencia.

    Después de crear la diapositiva, espera 2 segundos y vuelve al menú principal.
    """
    answers = questionary.form(
        type=questionary.select("¿Qué tipo de presentación quieres crear?",
                                choices=['Clase', 'Ponencia'],
                                pointer="👉")
    ).ask()

    if answers['type'] == 'Clase':
        new_class_slide()
    elif answers['type'] == 'Ponencia':
        new_speech_slide()

    sleep(2)
    main()

# MARK: SLIDES MANAGER


def manage_slides():
    """
    Gestiona las presentaciones.

    Muestra una lista de presentaciones disponibles y permite al usuario realizar diferentes acciones, como previsualizar, exportar a HTML o PDF, o regresar.

    Args:
        None

    Returns:
        None
    """
    slides = get_slides()

    if slides == False:
        print("[bold orange]No hay presentaciones disponibles 📭")

        answers = questionary.form(
            action=questionary.confirm(
                "¿Quieres crear una nueva presentación?")
        ).ask()

        if answers['action'] == True:
            new_slide()
    else:
        # Mostrar lista de presentaciones
        answers = questionary.form(
            slide=questionary.select(
                "¿Qué presentación quieres usar?", choices=slides, pointer="👉")
        ).ask()

        slide = answers['slide'].replace('.md', '')

        print(Panel.fit(f"[bold green]Presentación: {slide}"))

        choices = [
            "Previsualizar",
            "Exportar a PDF",
            "Exportar a HTML",
            "Exportar a imágenes",
            "Exportar portada",
            "Regresar"
        ]

        answers = questionary.form(
            action=questionary.select(
                "¿Qué quieres hacer?", choices=choices, pointer="👉")
        ).ask()

        if answers['action'] == 'Previsualizar':
            __preview(slide)
        elif answers['action'] == 'Exportar a HTML':
            __export_html(slide)
        elif answers['action'] == 'Exportar a PDF':
            __export_pdf(slide)
        elif answers['action'] == 'Exportar portada':
            __export_cover(slide)
        elif answers['action'] == 'Exportar a imágenes':
            __export_images(slide)
        elif answers['action'] == 'Regresar':
            pass
    sleep(2)
    main()


# MARK: BATCH SLIDES


def batch_slides():
    """
    Permite exportar todas las presentaciones a PDF.

    Returns:
        None
    """

    # Mostrar un mensaje de advertencia por el tiempo que puede tomar el proceso
    answers = questionary.form(
        action=questionary.confirm(
            "Este proceso puede tardar un poco, ¿quieres continuar?")
    ).ask()

    if answers['action'] == False:
        main()
    else:
        slides = get_slides()

        if slides == False:
            print("[bold orange]No hay presentaciones disponibles 📭")
            sleep(2)
            main()
        else:
            # Crea una barra de progreso y la actualiza conforme se exportan las presentaciones
            with Progress() as progress:
                task = progress.add_task(
                    "[bold green]Exportando presentaciones...", total=len(slides))
                for slide in slides:
                    slide = slide.replace('.md', '')
                    error = os.system(
                        f"{MARP_COMMAND} {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}.pdf --allow-local-files --pdf-outlines --pdf-outlines.pages=false --pdf-notes > NUL 2>&1")
                    if error != 0:
                        error_console.print(
                            f"[bold red]{slide} ❌")
                    progress.update(
                        task, description=f"[bold green]{slide} ✅", advance=1)

            print(
                f"[bold green]Todas las presentaciones han sido exportadas a PDF con éxito ✅")

    sleep(2)
    main()


# MARK: MAIN


def main():
    """
    Función principal que muestra un menú de opciones y ejecuta la acción seleccionada por el usuario.

    Returns:
        None
    """
    Console().clear()
    print(Panel.fit("[bold green]J2deme Slides", title="Bienvenido"))

    choices = [
        "Nueva presentación",
        "Batch de presentaciones",
        "Gestor de presentaciones",
        "Ver temas",
        "Salir"
    ]

    answers = questionary.form(
        action=questionary.select(
            "¿Qué quieres hacer hoy?", choices=choices, pointer="👉")
    ).ask()

    if answers['action'] == 'Nueva presentación':
        new_slide()
    elif answers['action'] == 'Batch de presentaciones':
        batch_slides()
    elif answers['action'] == 'Gestor de presentaciones':
        manage_slides()
    elif answers['action'] == 'Ver temas':
        theme_selector(False)
    elif answers['action'] == 'Salir':
        print("[bold cyan]¡Hasta luego! 👋")
        Console().clear()
        sys.exit()


@click.command()
@click.option('--pdf', is_flag=True, help='Exportar la presentación indicada a PDF')
@click.option('--preview', is_flag=True, help='Previsualizar la presentación indicada')
@click.argument('slide', required=False)
def cli(pdf, preview, slide):

    if slide:
        slide = slide.replace('.md', '')
        if pdf:
            __export_pdf(slide)
        elif preview:
            __preview(slide)
    else:
        main()


def __preview(slide):
    os.system(
        f"{MARP_COMMAND} {SOURCE_DIR}/{slide}.md --preview --allow-local-files --output {DIST_DIR}/{slide}.html")


def __export_pdf(slide):
    error = os.system(
        f"{MARP_COMMAND} {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}.pdf --allow-local-files --pdf-outlines --pdf-outlines.pages=false --pdf-notes")
    if error != 0:
        error_console.print(
            f"[bold red]Error al exportar {slide} a PDF ❌")
    else:
        print(
            f"[bold green]{slide} exportada a PDF con éxito ✅")


def __export_html(slide):
    error = os.system(
        f"{MARP_COMMAND} {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}.html --allow-local-files")
    if error != 0:
        error_console.print(
            f"[bold red]Error al exportar {slide} a HTML ❌")
    else:
        print(
            f"[bold green]{slide} exportada a HTML con éxito ✅")


def __export_cover(slide):
    error = os.system(
        f"{MARP_COMMAND} {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}-cover.png --allow-local-files --image=png --image-scale=2")
    if error != 0:
        error_console.print(
            f"[bold red]Error al exportar portada de {slide} ❌")
    else:
        print(
            f"[bold green]Portada de {slide} exportada con éxito ✅")


def __export_images(slide):
    error = os.system(
        f"{MARP_COMMAND} {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}/{slide}.png --allow-local-files --images=png --image-scale=2")
    if error != 0:
        error_console.print(
            f"[bold red]Error al exportar imágenes de {slide} ❌")
    else:
        print(
            f"[bold green]Imágenes de {slide} exportadas con éxito ✅")


def __generate_acronym(answers):
    '''
    Genera una abreviación para el nombre de la materia, útil para el nombrado del archivo Markdown.

    Returns:
        str: Abreviatura de la materia
    '''

    # Si las respuestas incluyen "acronym" no es necesario generar una abreviatura
    if 'acronym' in answers:
        return answers['acronym']
    else:
        # Genera una abreviatura para el nombre de la materia si tiene más de una palabra
        if len(answers['subject'].split()) > 1:
            # Elimina conectivas del nombre de la materia
            prepositions = ['la', 'el', 'los', 'las', 'y', 'en', 'a']
            if len(answers['subject'].split()) > 2:
                prepositions.append('de')

            subject_clean = ' '.join(
                [word for word in answers['subject'].split() if word.lower() not in prepositions])

            # Toma la primera letra de cada palabra y las convierte a mayúsculas
            acronym = ''.join(word[0].upper()
                              for word in subject_clean.split())
            return acronym
        else:
            # Si el nombre de la materia tiene una sola palabra, se usa tal cual
            return answers['subject']


if __name__ == '__main__':
    cli()

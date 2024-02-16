# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding: utf-8
"""
Author Jaime Jesús Delgado Meraz <j2deme>
"""

import os
import sys
from time import sleep
import questionary

from rich import print  # Overrides print() function
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

error_console = Console(stderr=True, style="bold red")

SOURCE_DIR = "src"
DIST_DIR = "dist"
CLASS_TEMPLATE = "src/templates/Clase.md"
CONFERENCE_TEMPLATE = "src/templates/Ponencia.md"


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


def theme_selector(answer=True):
    """
    Función que muestra una tabla con los temas disponibles y permite al usuario seleccionar uno.

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
            "primary": "#f43f5e",
            "secondary": "#16a34a"
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
        input("Presiona enter para regresar al menú principal...")
        main()


def new_class_slide():
    """
    Crea una nueva presentación de clase.

    Returns:
        None
    """
    answers = questionary.form(
        subject=questionary.text("Materia"),
        unit=questionary.text("Unidad"),
        unit_name=questionary.text("Nombre de la unidad"),
        code=questionary.text("Clave", default="ABC - 999"),
        satca=questionary.text("SATCA", default="9 - 9 - 9"),
    ).ask()

    theme = theme_selector()
    print(theme)

    # Toma como base el archivo CLASS_TEMPLATE, reemplaza las variables y crea un nuevo archivo
    with open(CLASS_TEMPLATE, 'r') as file:
        # Si la unidad es menor a 10, se agrega un cero al inicio
        unit = f"0{answers['unit']}" if int(
            answers['unit']) < 10 else f"{answers['unit']}"

        if len(answers['subject'].split()) > 1:
            # Genera una abreviatura para el nombre de la materia
            subject_abbr = ''.join(word[0].upper()
                                   for word in answers['subject'].split())

            title = f"{subject_abbr} - {unit} - {answers['unit_name']}"
            filename = f"{subject_abbr}-{unit}"
        else:
            title = f"{answers['subject']} - {unit} - {answers['unit_name']}"
            filename = f"{answers['subject']}-{unit}"

        filedata = file.read()
        filedata = filedata.replace(
            '___TITLE___', title).replace(
            '___HEADER___', answers['subject']).replace(
            '___SUBJECT___', answers['subject']).replace(
            '___UNIT___', answers['unit']).replace(
            '___UNIT_NAME___', answers['unit_name']).replace(
            '___CODE___', answers['code']).replace(
            '___SATCA___', answers['satca']).replace(
            '___PRIMARY_COLOR___', theme['primary']).replace(
            '___SECONDARY_COLOR___', theme['secondary'])

        with open(f"{SOURCE_DIR}/{filename}.md", 'w') as new_file:
            new_file.write(filedata)
            print(
                f"[bold green]Presentación para {answers['subject']} - U{answers['unit']} creada con éxito ✅")


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
        print("[bold yellow] ⚠ WIP")

    sleep(2)
    main()


def manage_slides():
    """
    Función que gestiona las presentaciones.

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
            "Exportar a HTML",
            "Exportar a PDF",
            "Regresar"
        ]

        answers = questionary.form(
            action=questionary.select(
                "¿Qué quieres hacer?", choices=choices, pointer="👉")
        ).ask()

        if answers['action'] == 'Previsualizar':
            os.system(
                f"marp {SOURCE_DIR}/{slide}.md --preview --allow-local-files --output {DIST_DIR}/{slide}.html")
        elif answers['action'] == 'Exportar a HTML':
            error = os.system(
                f"marp {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}.html --allow-local-files")
            if error != 0:
                error_console.print(
                    f"[bold red]Error al exportar {slide} a HTML ❌")
            else:
                print(
                    f"[bold green]{slide} exportada a HTML con éxito ✅")
        elif answers['action'] == 'Exportar a PDF':
            error = os.system(
                f"marp {SOURCE_DIR}/{slide}.md --output {DIST_DIR}/{slide}.pdf --allow-local-files --pdf-outlines --pdf-outlines.pages=false --pdf-notes")
            if error != 0:
                error_console.print(
                    f"[bold red]Error al exportar {slide} a PDF ❌")
            else:
                print(
                    f"[bold green]{slide} exportada a PDF con éxito ✅")
        elif answers['action'] == 'Regresar':
            pass
    sleep(2)
    main()


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
        "Gestor de presentaciones",
        "Temas",
        "Salir"
    ]

    answers = questionary.form(
        action=questionary.select(
            "¿Qué quieres hacer hoy?", choices=choices, pointer="👉")
    ).ask()

    if answers['action'] == 'Nueva presentación':
        new_slide()
    elif answers['action'] == 'Gestor de presentaciones':
        manage_slides()
    elif answers['action'] == 'Temas':
        theme_selector(False)
    elif answers['action'] == 'Salir':
        print("[bold cyan]¡Hasta luego! 👋")
        Console().clear()
        sys.exit()


if __name__ == '__main__':
    main()
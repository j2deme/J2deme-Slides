---
marp: true
title: Algoritmia y Estructuras de Datos - Proyectos Finales
author: Jaime Jesús Delgado Meraz
header: Algoritmia y Estructuras de Datos - Proyectos Finales
footer: "[&bull;](#contenidos) **DR. JJDM**"
paginate: true
theme: j2deme
math: mathjax
style: |
  :root {
    --primary: #1274c5;
    --secondary: #c22344;
  }
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Proyectos Finales

## Algoritmia y Estructuras de Datos

Dr. Jaime Jesús Delgado Meraz

###

#### IAD-2401

<img class="logo" alt="TecNM" src="../src/assets/Logo-TECNM.svg" />

---

# Docente

![bg right:40%](../src/assets/banner.svg)

Nombre
: Dr. Jaime Jesús Delgado Meraz

Correo
: <jesus.delgado@tecvalles.mx>
: <jaime.dm@cdvalles.tecnm.mx>

Enlaces
: :icon:brand-github: github.com/j2deme
: :icon:news: j2deme.github.io
: :icon:brand-instagram: j2deme

---

<!-- _class: cols-2 -->

# Asignatura

::: left

Nombre
: Algoritmia y Estructuras de Datos

Carrera
: Ingeniería en Inteligencia Artificial

:::
::: right

Clave
: IAD-2401

SATCA
: 2 - 3 - 5

:::

---

<!-- _class: toc -->

# Contenidos

1. [Gestor de biblioteca inteligente](#proyecto-1)
2. [Gestor de proyectos estudiantiles](#proyecto-2)

---

# Requerimientos generales

- Todos los proyectos deben ser desarrollados con las tecnologías vistas en clase (Python, interfaz de terminal).
- Las aplicaciones deben ser desarrolladas en equipos de máximo 5 integrantes.
- Cada proyecto debe contar con un repositorio en GitHub, donde se documente el desarrollo del proyecto, incluyendo el código fuente, instrucciones de uso y cualquier otra información relevante.
- Se debe implementar un menú que permita interactuar con el usuario, permitiendo seleccionar las diferentes opciones, sin necesidad de reiniciar la aplicación.
- Los datos deben ser almacenados entre sesiones, utilizando archivos de texto, JSON o cualquier otro formato adecuado.

---

<!-- _class: lead -->

# Proyecto 1

## Gestor de biblioteca inteligente 📚

---

# Gestor de biblioteca inteligente 📚

## Descripción

- La biblioteca del campus tiene cientos de libros, pero no existe un sistema para gestionarlos.
- Esto genera que los estudiantes no sepan qué libros están disponibles y no pueden reservar con anticipación.
- Además, no hay forma de descubrir lecturas relacionadas con sus intereses (por ejemplo, si les gustó un libro de Python, ¿qué otro podrían leer?).
- Se requiere crear un sistema que no solo administre el préstamo de libros, sino que también sugiera lecturas afines, convirtiendo la biblioteca en una red de conocimiento.

---

# Gestor de biblioteca inteligente 📚

## Requerimientos funcionales

- La aplicación debe modelar entidades del problema mediante clases en Python: `Libro` (con título, autor, género, año y disponibilidad), `Usuario` (nombre, ID) y `Prestamo` (usuario, libro, fecha).
- Todos los datos deben persistir entre sesiones, utilizando archivos JSON o CSV.
- La aplicación debe permitir regisrar, consultar, actualizar y eliminar libros y usuarios.
- Se debe implementar un sistema de búsqueda de libros por título, autor o género.
- Cada que se registre un nuevo libro, el sistema debe reordenar la lista de libros alfabéticamente por título utilizando el algoritmo de ordenamiento quicksort.
- La aplicación debe permitir a los usuarios solicitar préstamos de libros, verificando la disponibilidad y registrando la fecha de préstamo, mediante una cola FIFO.

---

# Gestor de biblioteca inteligente 📚

## Requerimientos funcionales (cont.)

- Algunos usuarios pueden tener prioridad para préstamos (por ejemplo, profesores), gestionando esto con una cola de prioridad.
- La aplicación debe construir un grafo no dirigido donde cada nodo es un libro y las aristas conectan libros del mismo género o autor.
- Se debe implementar un algoritmo de búsqueda en profundidad (DFS) para sugerir libros relacionados basados en el grafo.
- La aplicación debe proporcionar un menú interactivo para que los usuarios puedan navegar por las opciones sin reiniciar la aplicación.

---

<!-- _class: lead -->

# Proyecto 2

## Gestor de proyectos estudiantiles 📁

---

# Gestor de proyectos estudiantiles 📁

## Descripción

- En Tec Valles, los estudiantes participan constantemente en proyectos (investigación, desarrollo de software, competencias).
- Sin embargo, la coordinación es caótica: no hay seguimiento claro de tareas, fechas límite ni responsables.
- El jefe de sistemas, abre la convocatoria para que un equipo desarrolle un sistema que permita a un grupo de estudiantes organizar un proyecto desde cero:
  - Registrar tareas y asignarlas
  - Establecer fechas
  - Visualizar el orden en que deben ejecutarse (_p.e._, de acuerdo con su estatus, no puedes “probar” antes de “desarrollar”).
- La intención es que el sistema ayude a los equipos de trabajo a no perderse en el caos.

---

# Gestor de proyectos estudiantiles 📁

## Requerimientos funcionales

- La aplicación debe modelar entidades mediante clases en Python: `Proyecto` (nombre, equipo), `Tarea` (descripción, fecha límite, estado) y `Estudiante` (nombre, matrícula). (Atributos sugeridos).
- Todos los datos deben persistir entre sesiones, utilizando archivos JSON o CSV.
- La aplicación debe permitir registrar, consultar y marcar como finalizadas tareas y proyectos.
- Se debe implementar un sistema de búsqueda para localizar tareas por descripción, fecha límite, estado o estudiante asignado.
- Al consultar el panel de tareas, estas deben mostrarse ordenadas por fecha límite utilizando el algoritmo de ordenamiento quicksort.
- La aplicación debe gestionar las tareas pendientes mediante una cola FIFO, permitiendo a los estudiantes ver y completar tareas en el orden en que fueron asignadas.

---

# Gestor de proyectos estudiantiles 📁

## Requerimientos funcionales (cont.)

- Las tareas pueden tener dependencias (por ejemplo, "Desarrollar" debe completarse antes de "Probar"), por lo que se requiere implementar una representación a modo de árbol que muestre estas relaciones.
- La aplicación debe proporcionar un menú interactivo para que los usuarios puedan navegar por las opciones sin reiniciar la aplicación.

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

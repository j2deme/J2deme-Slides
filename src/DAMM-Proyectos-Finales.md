---
marp: true
title: DAMM - Proyectos
author: Jaime Jesús Delgado Meraz
header: Desarrollo de Aplicaciones Móviles Multiplataforma - Proyectos
footer: '[&oast;](#contenidos) **MSC. JJDM**'
paginate: true
theme: j2deme
math: mathjax
style: |
  :root {
    --primary: #3b82f6;
    --secondary: #d97706;
  }
---
<!-- _paginate: false -->

# Proyectos finales

## Desarrollo de Aplicaciones Móviles Multiplataforma

---

# Docente

![bg right:40%](../src/assets/banner.png)

Nombre
: MSC. Jaime Jesús Delgado Meraz

Correo
: <jesus.delgado@tecvalles.mx>
: <jaime.dm@cdvalles.tecnm.mx>

---

# Asignatura

:::: flex
::: col 1/2 px-2
Nombre
: Desarrollo de Aplicaciones Móviles Multiplataforma

Carrera
: Ingeniería en Sistemas Computacionales
:::
::: col 1/2
Clave
: DFB - 2204

SATCA
: 1 - 4 - 5
:::
::::

---
<!-- _class: toc -->
# Contenidos

1. [Generalidades](#generalidades)
2. [Sistema de Votaciones](#sistema-de-votaciones)
3. [Control de Inventarios](#control-de-inventarios)
4. [Control de Citas Médicas](#control-de-citas-médicas)

---
<!-- _class: lead -->
# Generalidades

---

# Generalidades

- Los proyectos a realizar serán la estrategia de evaluación final de las asignaturas de **Desarrollo de Aplicaciones Móviles Multiplataforma** y **Tópicos Avanzados de Base de Datos**.
- Deberán integrar el uso de una base de datos No SQL, que deberá ser implementada en la nube.
- Se deberá documentar el proceso de puesta en marcha de la base de datos, incluyendo la creación de la base de datos, colecciones, índices, usuarios y permisos, así como la conexión a la base de datos desde la aplicación.

---

# Generalidades

- Los proyectos se realizarán en equipos de máximo 5 integrantes.
- La evaluación de los proyectos se realizará en dos etapas:
  1. Prototipo funcional (50%)
  2. Evaluación individual (50%)
- Se debe hacer uso de los widgets y componentes de Flutter para la creación de la interfaz gráfica, no limitándose a los ejemplos vistos en clase.
- Se considerará la originalidad y creatividad en la implementación de las funcionalidades.

---

# Consideraciones de diseño

- Se deberá implementar un sistema de autenticación y registro para el acceso a la aplicación.
- La interfaz gráfica deberá ser intuitiva y fácil de usar, así como atractiva visualmente.
- La paleta de colores y tipografía deberán ser consistentes en toda la aplicación.
- Se debe hacer uso de los componentes de diseño, funcionalidad, interacción, animación y navegación que mejor se adapten a las necesidades de la aplicación.

---

# Consideraciones funcionales

- Las aplicaciones deberán ser funcionales y permitir a los usuarios realizar las acciones mínimas descritas en cada uno de los proyectos.
- Deben poder consumir y enviar datos a la base de datos No SQL implementada en la nube.
- Considere que la visualización de los datos deberá ser clara y concisa, permitiendo a los usuarios interactuar con la información de manera sencilla.

---
<!-- _class: lead -->
# Sistema de Votaciones

---

# Sistema de Votaciones

- El sistema de votaciones deberá permitir a los usuarios registrarse y votar en alguna de las votaciones disponibles, publicadas por otros usuarios.
- Los usuarios deberán poder visualizar las votaciones activas y votar en ellas.
- Cada usuario podrá votar una sola vez en una determinada votación y podrá cambiar su voto antes de que la votación finalice.
- Al finalizar la votación, se deberá mostrar el resultado de la misma en el historial de votaciones.
- Se deberá implementar un sistema de autenticación y registro para el acceso a la aplicación.

---

# Sistema de Votaciones

- Los usuarios podrán crear votaciones y definir las opciones de voto, indicando la fecha de inicio y fin de la votación, la pregunta a responder y las opciones de respuesta, la cantidad de opciones de respuesta será variable.
- Los usuarios podrán ver el historial de votaciones y los resultados de las votaciones finalizadas, tanto las que han creado como las que han votado.
- La vista individual del historial de votaciones deberá mostrar la pregunta, las opciones de respuesta, la fecha de inicio y fin de la votación y el resultado final por opción.

---
<!-- _class: lead -->
# Control de Inventarios

---

# Control de Inventarios

- El sistema de control de inventarios deberá permitir a los usuarios realizar consultas y filtrados diversos sobre el inventario de una empresa (o negocio) y generar cotizaciones de los artículos disponibles.
- Los artículos del inventario deberán tener al menos un código, nombre, descripción, precio, categoría, cantidad en existencia y una imagen.
- Los usuarios podrán realizar búsquedas por código, nombre, categoría y precio de los artículos.
- **No** se requiere que el listado de artículos se ingrese desde la aplicación, se puede considerar que los artículos ya están registrados en la base de datos.

---

# Control de Inventarios

- Los usuarios podrán ver el detalle de un artículo, mostrando la información disponible, así como imagen del mismo.
- Se debe implementar un sistema de autenticación y registro para el acceso a la aplicación.
- Además de las consultas, los usuarios deberán poder crear cotizaciones, seleccionando los artículos y la cantidad de cada uno, y generando un total a pagar, mismas que podrán ser guardadas y consultadas posteriormente.

---
<!-- _class: lead -->
# Control de Citas Médicas

---

# Control de Citas Médicas

- El sistema de control de citas médicas deberá permitir a los usuarios registrarse y solicitar citas con médicos disponibles.
- Los usuarios podrán ver el listado de médicos disponibles y solicitar una cita con alguno de ellos, ya sea por especialidad o por nombre.
- También podrán ver el historial de citas solicitadas y el estado de las mismas, así como cancelar citas pendientes.
- Los usuarios sólo deben poder solicitar una cita por médico a la vez, hasta que su cita haya sido atendida.

---

# Control de Citas Médicas

- Los médicos y especialidades deberán ser registrados directamente en la base de datos, los médicos deberán tener un horario de atención y una especialidad asociada.
- Los usuarios podrán ver el detalle de un médico, mostrando la información disponible, así como la especialidad y horario de atención.
- En la vista individual por médico, se debe mostrar la disponibilidad de citas, permitiendo solicitar una cita en un horario disponible  para una fecha determinada, considerando una duración de 30 minutos por cita.
- Sólo se podrán solicitar citas en horarios disponibles y con un mínimo de 3 días de anticipación.

---

<!-- _class: inverted -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

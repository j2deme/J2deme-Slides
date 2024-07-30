---
marp: true
title: DAMM - 02 - Examen
author: Jaime Jesús Delgado Meraz
header: Desarrollo de Aplicaciones Móviles Multiplataforma - U2 - Examen
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

# Unidad 2 <br> Examen

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

1. [Mini Proyecto 1](#mini-proyecto-1)
2. [Mini Proyecto 2](#mini-proyecto-2)
3. [Mini Proyecto 3](#mini-proyecto-3)

---

# Consideraciones generales

- Los proyectos deberán hacer uso de los widgets revisados en clase, así como cualquier otro widget que el equipo considere relevante para el desarrollo del proyecto.
- Se deben combinar widgets de diseño, funcionales, interactivos y animación para que el proyecto sea interesante y atractivo.
- Todos los proyectos deben hacer uso del manejo de estado.
- En general, no se requiere más de una pantalla para los proyectos propuestos, pero si el equipo considera que es necesario, puede agregar más pantallas y rutas.

---

# Consideraciones generales

- Los proyectos deben ser entregados en un repositorio de GitHub, con un archivo `README.md` que contenga:
  - Nombre del proyecto.
  - Clave del grupo.
  - Integrantes del equipo.
- Sólo se aceptarán proyectos dentro de la fecha y hora límite establecida.
- El mini proyecto se presentará en una sesión síncrona, donde se mostrará el funcionamiento del mismo y el docente podrá hacer preguntas dirigidas, para validar la participación de cada integrante en el desarrollo.
- La calificación se dividirá entre la funcionalidad y el dominio del tema (50/50).

---
<!-- _class: lead -->
# Mini Proyecto 1

---

# Juego de la Colmena 🐝

> Una colmena tiene diferentes tipos de abejas: una reina, obreras, zánganos y larvas; el apicultor debe tratar de encontrar a la abeja reina antes de llegar al límite de picaduras.

- El juego debe mostrar un tablero de 5x5 que represente la colmena con las abejas, así como los puntos de vida del jugador.
- Todos los espacios deberán contener abejas obreras, zánganos o larvas, distribuidas aleatoriamente.
- La abeja reina se esconderá en una posición aleatoria, pero nunca en las esquinas.

---

# Características

- El jugador podrá "destapar" una celda por turno y ver qué tipo de abeja se encuentra en ella (la celda destapada no podrá ser seleccionada de nuevo).
- El jugador inicia el juego con 7 puntos de vida y pierde puntos según la abeja que encuentre: larva (`0`), obrera (`-1`) o zángano (`-2`).
- El juego terminará si el jugador encuentra a la abeja reina o si pierde todos sus puntos de vida.
- Si se desea jugar de nuevo se debe generar un nuevo tablero y restablecer los puntos de vida.

---
<!-- _class: lead -->
# Mini Proyecto 2

---

# Juego de Pig 🐷

> El juego de Pig es un juego de dados en el que el jugador lanza un dado y acumula puntos, pero si saca un `1` pierde todos los puntos acumulados en su turno.

- El juego debe permitir a dos jugadores competir por llegar a `100` puntos.
- Un jugador será el jugador humano y el otro será la computadora.
- El juego debe mostrar el puntaje de cada jugador y el puntaje acumulado en el turno actual.
- El jugador humano siempre inicia el juego.

---

# Características

- Se usará un dado de `6` caras para acumular puntos.
- El jugador humano debe poder lanzar el dado o pasar el turno (hasta después de lanzar el dado al menos una vez).
- La computadora lanzará el dado automáticamente hasta que acumule al menos `20` puntos o saque un `1`.
- Cualquier jugador que saque un `1` recibe un _pig 🐷_ y pierde todos los puntos acumulados en el turno, y pasa el turno al otro jugador.

---
<!-- _class: lead -->
# Mini Proyecto 3

---

# Mini ONO 0️⃣

> El juego de ONO consiste descartar cartas con valores númericos o especiales, para acercarse a `99` puntos, sin pasarse.

- Un jugador será el jugador humano y el otro será la computadora.
- El juego inicia con un total de `0` puntos.
- Ambos jugadores tendrán `4` cartas durante todo el juego, y podrán descartar una carta por turno, que será reemplazada por una nueva carta al terminar su turno.
- El juego debe mostrar el total actual y las cartas de cada jugador en todo momento.

---

# Características

- Las cartas tendrán principalmente valores del `1` al `9` que suman su valor al total.
- Existen cartas especiales que tendrán los siguientes efectos:
  - `-10`: resta `10` al total, llevandolo a negativo si es el caso.
  - `x2`: no suma ni resta, pero duplica el valor de la siguiente carta.
  - `HOLD`: mantiene el total y pasa el turno al otro jugador.
- Cuando un jugador llega a `99` o más puntos, el juego termina y el otro jugador gana.
- Si se desea jugar de nuevo se generarán nuevas cartas y se restablecerá el total.

::: info
**Nota:** Las cartas serán generadas aleatoriamente, de manera infinita hasta que termina el juego, considerando que las cartas especiales son menos comunes.
:::

---

<!-- _class: inverted -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

---
marp: true
title: FP - Proyectos finales
author: Jaime Jesús Delgado Meraz
header: Fundamentos de Programación -  Proyectos Finales
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

<!-- _class: centered -->
<!-- _paginate: false -->

# <!-- fit --> Proyectos finales

## Fundamentos de Programación

<img class="logo" alt="TecNM" src="../src/assets/Logo-TECNM.svg" />

---

# Docente

![bg right:40%](../src/assets/banner.svg)

Nombre
: Dr. Jaime Jesús Delgado Meraz

Correo
: <jesus.delgado@tecvalles.mx>
: <jaime.dm@cdvalles.tecnm.mx>

---

# Asignatura

<!-- _class: cols-2 -->

# Asignatura

::: left

Nombre
: Fundamentos de Programación

Carrera
: Ingeniería en Sistemas Computacionales
: Ingeniería en Desarrollo de Aplicaciones

:::
::: right

Clave
: AED - 1285

SATCA
: 2 - 3 - 5

:::

---

<!-- _class: toc -->

# Contenidos

1. [Cuatro en raya](#proyecto-1)
2. [Buscaminas Twist](#proyecto-2)

---

# Requerimientos generales

- Todos los proyectos deben ser desarrollados con las tecnologías vistas en clase (Python, interfaz de terminal).
- Dado que los proyectos representan juegos, deben ser interactivos y permitir la interacción con el usuario.
- Adicionalmente, deben considerar la posibilidad de ganar o perder, así como la posibilidad de reiniciar el juego.
- El diseño de los proyectos debe ser claro y sencillo, permitiendo al usuario entender fácilmente cómo interactuar con el juego.
- Se debe implementar un menú que permita interactuar con el usuario, permitiendo seleccionar la opción deseada.

---

<!-- _class: lead -->

# Proyecto 1

## Cuatro en raya 🔴🔴🔴🔴

---

# Cuatro en raya 🔴🔴🔴🔴

## Descripción

> También conocido como "Conecta 4", es un juego de mesa en el que dos jugadores compiten por alinear cuatro fichas del mismo color en un tablero de 7 columnas y 6 filas.

- El juego debe permitir a los jugadores seleccionar la columna en la que desean colocar su ficha, validando que la columna no esté llena y que la ficha "caiga" en la posición correcta.
- El juego debe indicar cuándo un jugador ha ganado, ya sea por alinear cuatro fichas en horizontal, vertical o diagonal, o bien, indicar que el juego ha terminado en empate, si no hay más movimientos posibles.
- Al finalizar el juego, se debe permitir a los jugadores reiniciar el juego o salir del mismo.

---

# Cuatro en raya 🔴🔴🔴🔴

## Tablero de juego

- El tablero de juego debe ser de 7 columnas y 6 filas, permitiendo a los jugadores colocar sus fichas en la columna deseada.

![tablero de conecta 4 h:300 #c](https://www.casualarena.com/bundles/app/st/games/co4/rules/connect-4-rules.jpg)

- Si no se conoce el juego, se puede consultar en <https://www.epasatiempos.es/juego-4-en-raya.php>

---

# Cuatro en raya 🔴🔴🔴🔴

## Requerimientos funcionales

- Se debe mostrar el menú para jugar o salir del juego.
- Se debe elegir el color de las fichas de cada jugador (rojo o amarillo).
- Se debe mostrar el tablero de juego, permitiendo a los jugadores seleccionar la columna en la que desean colocar su ficha.
- Se debe validar que la columna seleccionada no esté llena y que la ficha "caiga" en la posición correcta.
- Se debe indicar cuándo un jugador ha ganado, ya sea por alinear cuatro fichas en horizontal, vertical o diagonal, o bien, indicar que el juego ha terminado en empate, si no hay más movimientos posibles.
- Al finalizar el juego, se debe permitir a los jugadores reiniciar el juego o salir del mismo.
- En todo momento se debe mostrar el estado actual del tablero de juego, es decir, las fichas colocadas y las posiciones vacías, así como el jugador que tiene el turno.

---

# Cuatro en raya 🔴🔴🔴🔴

## Consideraciones adicionales

- El equipo de desarrollo es libre de agregar funcionalidades adicionales al juego, siempre y cuando cumpla con los requerimientos mínimos.
- Adicionalmente, podrán elegir entre desarrollar el juego para dos jugadores (PvP) o contra la máquina (PvE), en cuyo caso, se deberá implementar un algoritmo que permita a la máquina tomar decisiones de juego.

---

<!-- _class: lead -->

# Proyecto 2

## Buscaminas Twist 💣️

---

# Buscaminas Twist 💣️

## Descripción

- Como su nombre lo indica, es una variante del clásico juego de buscaminas, en el que el jugador debe descubrir todas las casillas que no contienen minas, evitando descubrir una casilla con una mina.
- El _twist_ de este juego es que se basa más en la suerte que en la lógica, ya que el jugador debe elegir una casilla al azar y descubrir si contiene una mina o no.
- Para lo anterior, el juego debe permitir al jugador seleccionar una casilla del tablero, indicando si contiene una mina o no, y mostrar el resultado.
  - Si la casilla contiene una mina, el jugador pierde una vida.
  - Si la casilla no contiene una mina, el juego continúa y el jugador puede seleccionar otra casilla.
- El juego termina cuando el jugador ha perdido todas sus vidas o ha descubierto todas las casillas que no contienen minas.

---

# Buscaminas Twist 💣

## Requerimientos funcionales

- Se debe mostrar el menú para jugar, para posteriormente elegir el tamaño del tablero o salir del juego.
- En todo momento se debe mostrar el estado actual del tablero de juego, es decir, las casillas descubiertas y las casillas ocultas, así como el número de vidas restantes.
  - La selección de casillas debe basarse en la posición de la casilla en el tablero, es decir, la fila y columna.
  - Se debe indicar cuántas vidas le quedan al jugador y cuántas casillas le faltan por descubrir.
- Se debe validar si la casilla seleccionada contiene una mina o no; realizando la acción correspondiente.
- El juego termina cuando el jugador ha perdido todas sus vidas o ha descubierto todas las casillas que no contienen minas, indicando si ha ganado o perdido, y la opción de reiniciar el juego o salir del mismo.
- Revisa el buscaminas **clásico** en <https://buscaminas.eu/>.

---

# Buscaminas Twist 💣

## Consideraciones adicionales

- Se deberá implementar un algoritmo que permita colocar las minas en el tablero de forma aleatoria.
- Para que el juego sea relativamente "justo", se recomienda que el número de minas sea proporcional al tamaño del tablero, considere la siguiente fórmula para calcular el número de minas:

$$minas = \frac{filas \times columnas}{6}$$

- El número de vidas se calculará en relación al número de bombas en el tablero, considerando la siguiente fórmula:

$$vidas = minas - 2$$

- El equipo de desarrollo es libre de agregar funcionalidades adicionales al juego, siempre y cuando cumpla con los requerimientos mínimos.

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

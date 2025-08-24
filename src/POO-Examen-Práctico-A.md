---
marp: true
title: Programación Orientada a Objetos - Examen práctico - A
author: Jaime Jesús Delgado Meraz
header: Programación Orientada a Objetos - Examen práctico - A
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

# Examen práctico

## Programación Orientada a Objetos

Dr. Jaime Jesús Delgado Meraz

### 03 y 04

#### IAD - 2424

#### AED - 1286

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
: Programación Orientada a Objetos

Carrera
: Ingeniería en Sistemas Computacionales
: Ingeniería en Desarrollo de Aplicaciones
: Ingeniería en Inteligencia Artificial

:::
::: right

Clave
: AED - 1286
: IAD - 2424

SATCA
: 2 - 3 - 5

:::

---

<!-- _class: lead -->

# Descripción

---

Despiertas en la orilla de una isla desierta... o eso parece hasta que escuchas algunos gruñidos a lo lejos, ves algunos árboles frutales y sabes que al menos podrás calmar el hambre por unos días.

Sigues caminando un poco más y encuentras un bote abandonado, pero que al parecer funciona, el único problema es que esta encadenado a un árbol y no tienes la llave, al revisar el bote encuentras una nota que dice:

> "No se quién seas, pero si encontraste esta nota, es porque no pude regresar al bote, busca la llave... tal vez aún pueda servirte..."

Sabes que la llave está en algún lugar de la isla, pero no tienes idea de donde buscarla, explorar la isla es tu única opción, ya que no tienes nada más que hacer.

---

Al explorar la isla, vas encontrando diferentes objetos, algunos útiles y otros peligrosos, pero lo que más te interesa es encontrar la llave para poder salir de la isla.

Encuentras rocas que no sirven para nada, algunas frutas que te ayudan a sobrevivir, pero también encuentras algunos objetos peligrosos como serpientes, escorpiones y hasta un cocodrilo.

La meta es encontrar la llave antes de que sea demasiado tarde...

---

# Requerimientos funcionales

Deberán desarrollar un programa que simule la búsqueda de la llave, el programa deberá tener al menos las siguientes características:

- Deben representar la isla donde se ubicarán objetos al azar:
  - Las rocas ⛰, no sirven para nada, pero al menos no son peligrosas.
  - Las frutas sirven para sobrevivir 🥥🍌🍍, si te encuentras con alguna de ellas, se gana una vida.
  - Las serpientes 🐍 y los escorpiones 🦂 son peligrosos, si se encuentra con alguno de ellos, se pierde una vida.
  - El cocodrilo 🐊 es el más peligroso de todos, si lo encuentras, se pierde el juego.
- La llave 🗝 por otro lado, es la meta del juego, si la encuentras, ganas el juego.

---

# Requerimientos funcionales

- El jugador tendrá un número de vidas ❤ (5) que se irán perdiendo al encontrar objetos peligrosos (-1), y se ganarán al encontrar frutas (+1).
- El jugador deberá moverse por el mapa eligiendo un par de coordenadas a la vez, y el programa deberá mostrar el objeto que se encuentra en esa celda, así como los efectos que tiene sobre el jugador.
- El juego deberá terminar cuando el jugador encuentre la llave, o cuando se quede sin vidas, o si encuentra al cocodrilo, según lo que ocurra primero.
- Si se elige una celda que **ya se ha explorado**, se debe mostrar un mensaje indicando que ya se ha explorado esa celda y deberá pedir nuevamente las coordenadas.
- Si se elige una celda **fuera del rango** de la isla, se deberá mostrar un mensaje indicando que las coordenadas son inválidas y deberá pedir nuevamente las coordenadas.
- Una vez que se ha explorado una celda, se deberá mostrar el mapa de la isla con los objetos que ya han sido explorados y los que aún no han sido explorados.

---

# Requerimientos funcionales

- Al finalizar el juego y dependiendo de la situación, se deberá mostrar un mensaje indicando si el jugador ganó o perdió, así como el número de vidas restantes.
- Adicionalmente, se deberá "descubrir" el mapa de la isla, mostrando todos los objetos que se encontraban en la isla, así como el objeto que se encontró en cada celda.
- El programa deberá ser capaz de reiniciarse para jugar nuevamente.

---

# Requerimientos técnicos

- La isla se representará como una matriz de **6x6**, donde cada celda contendrá un objeto al azar (roca, fruta, serpiente, escorpión, cocodrilo o llave).
- Se deberán implementar las clases que representen los objetos de la isla y sus efectos, así como la clase que represente al jugador.
- Se deberá implementar un menú que permita interactuar con el juego, así como mostrar la información del jugador (vidas y coordenadas) y el mapa de la isla.
- Además de utilizar clases y objetos, se deberá implementar la herencia y el polimorfismo en el diseño del programa.

::: warning
Aunque es posible realizar el examen sin utilizar herencia y polimorfismo, no utilizar estos conceptos hará que la calificación sea más baja.
:::

---

# Requerimientos técnicos

- La distribución de los objetos en la isla deberá cumplir con las siguientes condiciones:
  - Aunque suena obvio, pero dos objetos no pueden estar en la misma celda.
  - Sólo puede haber un cocodrilo y una llave en la isla.
  - Debe haber al menos 3 frutas y 3 rocas en la isla.
  - Debe haber al menos 2 serpientes y 2 escorpiones en la isla.
  - El resto de los objetos pueden ser cualquier combinación de frutas, rocas, serpientes y escorpiones.

---

# Consideraciones de evaluación

- El examen se evaluará de acuerdo a los siguientes criterios:

| Criterio                                                | Porcentaje |
| :------------------------------------------------------ | :--------: |
| Jugabilidad básica                                      |    20%     |
| Implementación de las clases y objetos                  |    20%     |
| Menú e interacción con el usuario                       |    10%     |
| Implementación de la herencia                           |    15%     |
| Implementación del polimorfismo                         |    15%     |
| Dominio del tema[*:Se evaluará al explicar la solución] |    20%     |

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

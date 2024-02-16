---
marp: true
title: EDD - U2 - Recursividad
author: Jaime Jesús Delgado Meraz
header: Estructuras de Datos - U2
footer: '[&oast;](#contenidos) **MSC. JJDM**'
theme: j2deme
paginate: true
math: mathjax
---

# Unidad 2 <br> Recursividad

## Estructuras de Datos

---

# Docente

![bg right:40%](../src/assets/banner.png)

Nombre
: MSC. Jaime Jesús Delgado Meraz

Correo
: <jesus.delgado@tecvalles.mx>

---

# Asignatura

:::: flex
::: col 1/2 px-2
Nombre
: Estructura de Datos

Carrera
: Ingeniería Informática e Ingeniería en Sistemas Computacionales
:::
::: col 1/2
Clave
: AED - 1026

SATCA
: 2 - 3 - 5
:::
::::

---
<!-- _class: toc -->
# Contenidos

1. [Introducción](#introducción)
2. [Recursividad](#recursividad)
3. [Funciones recursivas](#funciones-recursivas)
4. [Problemas recursivos](#problemas-recursivos)

---

<!-- _class: lead -->

# Introducción

---

# Introducción

- La recursividad es un concepto que se utiliza en programación para resolver problemas que se pueden descomponer en problemas más pequeños del mismo tipo.
- Esta asociada a las estructuras de datos pues se puede utilizar para recorrerlas y realizar operaciones sobre sus elementos.
- Sin embargo, su aplicación no se limita a las estructuras de datos, sino que se puede utilizar para resolver problemas de cualquier tipo.

---

<!-- _class: lead -->

# Recursividad

---

# Recursividad

> Es un concepto que se utiliza en programación para resolver problemas que se pueden descomponer en problemas más pequeños del mismo tipo.

- Se refiere a la capacidad de una función de llamarse a sí misma.
- Aunque la recursividad puede ser una técnica poderosa, es importante saber cuándo usarla y cuándo no usarla.
- Usada correctamente, puede ser una herramienta muy poderosa para resolver problemas complejos.
- Por otro lado, si se utiliza de manera incorrecta, puede provocar que el programa se ejecute de manera infinita.

---

# Recursividad

- La recursividad no solo consiste en llamar a una función desde sí misma, sino que también debe cumplir con las siguientes condiciones:
  - Debe tener un caso base.
  - Debe cambiar su estado y moverse hacia el caso base.
- Si no se cumplen estas condiciones, la función se ejecutará de manera infinita.
- Dependiendo del lenguaje de programación, la recursividad puede ser más o menos eficiente que una solución iterativa.

---

# Recursividad

## Caso base

> Es el caso más simple que se puede resolver.

- El caso base es aquel que que no requiere de llamadas recursivas.
- Es el caso que se resuelve de manera directa y permite que la función se detenga.

---

# Recursividad

## Cambio de estado

- El cambio de estado es el proceso mediante el cual la función se mueve hacia el caso base.
- Si no se realiza el cambio de estado, la función se ejecutará de manera infinita.
- El cambio de estado se puede realizar de dos maneras:
  - Cambio de parámetros.
  - Cambio de variables.

---

## Cambio de estado

:::: flex

::: col 1/2 px-2

### Cambio de parámetros

- El cambio de parámetros consiste en modificar los parámetros de la función para que se acerquen al caso base.

```c
int factorial(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
```

:::
::: col 1/2 px-2

### Cambio de variables

- El cambio de variables consiste en modificar las variables de la función para que se acerquen al caso base.

```c
int factorial(int n) {
  int result = 1;
  while (n > 0) {
    result *= n;
    n--;
  }
  return result;
}
```

::::

- Propiamente, el cambio de variables no es recursividad, pero se puede utilizar para resolver problemas recursivos.

---

# Recursividad

## Ejemplo

:::: flex

::: col 1/2 px-2

### Factorial

- El factorial de un número es el producto de todos los números enteros positivos desde 1 hasta n.

```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
```

:::
::: col 1/2 px-2

### Fibonacci

- La sucesión de Fibonacci es una sucesión infinita de números naturales que comienza con los números 0 y 1, y a partir de estos, cada término es la suma de los dos anteriores.

```python
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
```

:::
::::

---

# Recursividad VS Iteración

- La recursividad y la iteración son dos técnicas que se pueden utilizar para resolver problemas de manera repetitiva, mientras que la recursividad se basa en la auto referencia, la iteración se basa en la repetición.

:::: flex
::: col 1/2 px-2

### Recursividad

```python
def potenciaR(x, n):
  if n == 0:
    return 1
  else:
    return x * potenciaR(x, n - 1)
```

:::
::: col 1/2 px-2

### Iteración

```python
def potenciaI(x, n):
  result = 1
  for i in range(n):
    result *= x
  return result
```

:::
::::

- En este caso, la estructura de la función recursiva es más sencilla que la función iterativa, pero la función iterativa es más eficiente en términos de tiempo y memoria.

---

<!-- _class: lead -->

# Funciones recursivas

---

# Funciones recursivas

> Una función recursiva es una función que se llama a sí misma.

- Para que una función sea recursiva, debe cumplir con las condiciones de la recursividad.
  1. Auto referenciarse.
  2. Tener un caso base.
  3. Cambiar su estado y moverse hacia el caso base.
- La definición de una función recursiva suena simple, pero no todas las funciones que se llaman a sí mismas son recursivas.

---

# Funciones recursivas

## ¿Cuándo usar recursividad?

- En general, se recomienda utilizar recursividad cuando:
  - El problema se puede descomponer en problemas más pequeños del mismo tipo.
    - _P.e_. Factorial, Fibonacci.
  - El problema se puede descomponer en problemas más pequeños de un tipo similar.
    - _P.e._ Recorrer una estructura de datos.
  - El problema se puede descomponer en problemas más pequeños de un tipo diferente.
    - _P.e._ Ordenamiento de datos.

::: warning
⚠ La recursividad es una técnica poderosa, pero no siempre es la mejor opción.
:::

---

# Funciones recursivas

## ¿Cuándo no usar recursividad?

- Es importante tener claro que la recursividad no es una "pieza intercambiable" con los ciclos, sino que es una técnica que se debe utilizar cuando sea adecuada.
- De hecho, es posible resolver cualquier problema recursivo con ciclos, pero no siempre es posible resolver un problema iterativo con recursividad.
- Entonces ¿cuándo no usar recursividad?
  - Cuando el problema se puede resolver de manera iterativa.
  - Cuando la recursividad no aporta nada al problema.
  - Cuando la recursividad no es eficiente.

::: info
ℹ Lenguajes como Haskell y Lisp son más eficientes con recursividad que con ciclos, por lo que debe considerarse el lenguaje de programación.
:::

---

# Funciones pseudo recursivas

- Existen funciones que se llaman a sí mismas, pero que no son recursivas, sino _pseudo recursivas_. Es posible definirlas en 3 categorías:
  - Funciones mutuamente recursivas.
  - Funciones recursivas indirectas.
  - Funciones con ciclos que se llaman a sí mismas.
- Estas funciones no son recursivas porque no cumplen con las condiciones de la recursividad, únicamente se llaman a sí mismas de manera directa o indirecta.

---

# Funciones pseudo recursivas

## Funciones mutuamente recursivas

:::: flex
::: col 1/2 px-2

```python
def par(n):
  if n == 0:
    return True
  else:
    return impar(n - 1)

def impar(n):
  if n == 0:
    return False
  else:
    return par(n - 1)
```

:::
::: col 1/2 px-2

- En este caso, la función `par` llama a la función `impar` y viceversa, creando una dependencia circular.
- Sin embargo, no tienen un caso base claro dentro de una sola función para detener la recursión.
- Mas bien, el caso base está distribuido en ambas funciones, haciéndolas mutuamente recursivas pero no recursivas independientes.

:::
::::

---

# Funciones pseudo recursivas

## Funciones recursivas indirectas

:::: flex
::: col 1/2 px-2

```python
def procesa_a():
  print("a")
  procesa_b()

def procesa_b():
  print("b")
  procesa_a()
```

- En este caso, la auto referencia no esta dentro de la misma función, sino que se da a través de una llamada a otra función.

:::
::: col 1/2 px-2

- Involucra una cadena de llamadas a través de otras funciones, creando un ciclo.
- Como tal no cumple con la condición de recursividad, ya que no se llama a sí misma de manera directa.
- Adicionalmente, para el ejemplo mostrado, no existe un caso base que detenga la recursión, haciendo que se ejecute de manera infinita.

:::
::::

---

# Funciones pseudo recursivas

## Funciones con ciclos que se llaman a sí mismas

:::: flex
::: col 1/2 px-2

```python
def fibbonacci(n):
  while True:
    print(n)
    fibbonacci(n - 1)
```

- En este caso, la función se llama a sí misma dentro de un ciclo, pero no tiene un caso base que detenga la recursión.

:::
::: col 1/2 px-2

- Lo anterior hace que se ejecute de manera infinita, lo que además de no ser adecuado, tampoco es recursividad.
- Aunque la función se llama a sí misma, no cuenta con un caso base ni cambia su estado para acercarse al caso base.

:::
::::

---

<!-- _class: lead -->

# Problemas recursivos

---

# Problemas recursivos

- La recursividad se puede utilizar para resolver problemas de cualquier tipo, pero es más común utilizarla para resolver problemas de estructuras de datos.
- En este caso, la recursividad se puede utilizar para recorrer las estructuras de datos y realizar operaciones sobre sus elementos.
  - La recursividad en los recorridos simplifica el código y lo hace más legible.
  - Para operaciones como el ordenamiento, la recursividad puede ser más eficiente que los ciclos, puesto que no se requiere de variables auxiliares.

---

# Problemas recursivos

- Además de los problemas de estructuras de datos, también se pueden resolver problemas de otro tipo, como:
  - Factorial.
  - Fibonacci.
  - Torres de Hanoi.
  - Buscar un elemento en una matriz.
  - Buscar un elemento en una cadena.
  - Buscar un elemento en un árbol binario.
  - Buscar un elemento en un grafo.
  - Ordenamiento de datos.

---

<!-- _class: inverted -->

# Midiendo el tiempo y la complejidad

:::: flex
::: col 1/2 px-2

- Para medir el tiempo de ejecución de un programa, se puede utilizar el módulo `time` de Python que permite medir el tiempo en segundos.

```python
import time

start = time.time()
# Código a medir
end = time.time()
print(end - start)
```

:::

::: col 1/2 px-2

- Una alternativa es utilizar el módulo `timeit` de Python, el cual permite medir el tiempo de ejecución en milisegundos.

```python
import timeit

start = timeit.default_timer()
# Código a medir
end = timeit.default_timer()
print(end - start)
```

:::
::::

---

<!-- _class: inverted -->

- También se puede usar la función `timeit` para medir el tiempo de ejecución de una función.

```python
import timeit

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# number es la cantidad de veces que se ejecuta la función
print(timeit.timeit(lambda: factorial(10), number=10000))

# Tiempo de ejecución con diferentes valores de n
tiempos = [timeit.timeit(lambda: factorial(n), number=10000) for n in range(1, 11)]
```

---

# Problemas recursivos

## El ajedrez

![bg right:45%](../src/assets/illustration/wise-man-playing-chess.jpeg)

Hace mucho tiempo, en la antigua India, vivía un rey llamado Sheram, poderoso y arrogante, estratega y asiduo a los juegos de estrategia.

Un día, un sabio llamado Sissa inventó un nuevo juego que llamó _chaturanga_, el juego era muy complejo y desafiante, y Sheram quedó fascinado con él.

Sheram le pidió a Sissa que le enseñara a jugar al ajedrez y pronto el rey se convirtió en un experto en el juego.

---

## El ajedrez

Sheram estaba tan agradecido con Sissa por haberle enseñado el ajedrez que le dijo:

> _"Sissa, eres un hombre muy sabio. Como recompensa por tu ingenio, puedes pedirme cualquier cosa que quieras."_

Sissa pensó un momento y luego dijo:

> _"Su Majestad, le pido un grano de trigo por la primera casilla del tablero de ajedrez, dos granos por la segunda, cuatro granos por la tercera, y así sucesivamente, duplicando la cantidad de granos en cada casilla."_

El rey Sheram se rió.

> _"¿Eso es todo?", dijo. "Es una petición muy modesta. Te concederé tu deseo."_

---

## El ajedrez

Y así, Sissa recibió su recompensa. Pero el rey Sheram no sabía que había cometido un error. Cuando Sissa llegó a la última casilla del tablero, el número de granos que había pedido era tan grande que el rey no podía pagarlos.

El rey Sheram se dio cuenta de que había sido muy arrogante al hacer una promesa sin pensar en las consecuencias. Había subestimado la inteligencia de Sissa y el poder del crecimiento exponencial.

---

## El ajedrez y la recursividad

- El problema del ajedrez es un problema clásico de recursividad.
- El problema consiste en calcular la cantidad de granos de trigo que se necesitan para llenar un tablero de ajedrez, si en la primera casilla se coloca un grano, y en las siguientes se va duplicando la cantidad de granos en cada casilla.
- El problema se puede resolver de manera iterativa, pero es más sencillo y eficiente resolverlo de manera recursiva.
- La leyenda anterior se utiliza a menudo para ilustrar el concepto de crecimiento exponencial, el cual en este caso, se puede resolver mediante el factorial.

---

## El ajedrez y la recursividad

- En este caso, el tablero de ajedrez es de 8x8 casillas, por lo que se requiere de una función que calcule el factorial de 64.
- La función factorial se puede definir de manera recursiva como:

$$
n! = \left\{
\begin{array}{ll}
1 & \text{si } n = 0 \\
n \times (n - 1)! & \text{si } n > 0
\end{array}
\right.
$$

- En el relato, la cantidad de granos de trigo a pagar es el factorial de 64, que es un número muy grande, y fue imposible de pagar.
- El resultado es de hecho 1.2688693218588417e+29, lo que equivale a 126886932185884164103433389335161480802865516174545192198801894375214704230400000000000000, para ser exactos.

---

## El ajedrez y la recursividad

- El problema del ajedrez se puede resolver tanto de manera iterativa como recursiva.

:::: flex
::: col 1/2 px-2

### Iterativo

```python
def factorial(n):
  result = 1
  while n > 0:
    result *= n
    n -= 1
  return result
```

:::
::: col 1/2 px-2

### Recursivo

```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
```

:::
::::

- Si bien la versión iterativa tiene una complejidad de $O(n)$ y la versión recursiva tiene una complejidad de $O(2^n)$, esta última es más sencilla de implementar y de entender, por lo que es más recomendable utilizarla, incluso si es menos eficiente.

---

<!-- _class: inverted -->

::: coding
:::

---

# Problemas recursivos

## Las torres de Hanoi

![bg right:45%](../src/assets/illustration/brahma-vishnu-shiva.jpeg)

Hace mucho tiempo, los monjes de un monasterio en la región de Hanói, se encontraban rezando a Brahma, Vishnu y Shiva, ya que querían saber cuándo iba a ser destruido el mundo.

Apareció el dios Brahma y les entregó una base con tres postes de diamante, uno de ellos con 64 discos de oro puro de diferentes tamaños apilados de mayor a menor, empezando por el más grande en la base.

---

## Las torres de Hanoi

Una vez que el dios Brahma se retiró, los monjes se preguntaban qué debían hacer con los discos, en ese momento se manifestó el dios Vishnu y les explicó las reglas que debían seguir para complacer a sus dioses:

- Solo se puede mover un disco a la vez.
- Solo se puede mover el disco que se encuentre en la punta de un poste.
- Nunca se puede colocar un disco más grande sobre uno más pequeño.

Los monjes se alegraron de saber lo que tenían que hacer y pensaron que si movían todos los discos de un poste al otro cumpliendo las reglas que les había sido explicadas, complacerían a sus dioses y estos les dirían cuándo se terminaría el mundo.

---

## Las torres de Hanoi

Cuando estaban a punto de comenzar a mover los discos, apareció el dios Shiva y les dijo: "cuando terminen de mover los 64 discos, en ese momento el mundo habrá terminado".

Los monjes se llenaron de miedo, pues si no movían los discos, sus dioses se enfadarían con ellos y los castigarían, pero si terminaban de mover todos los discos, entonces el mundo llegaría a su fin.

Los monjes tuvieron que pensar en una solución para mover los discos, pero sin terminar de moverlos todos.

Cuando por fin encontraron la solución, movieron el primer disco y se fueron a dormir, seguros de que harían falta muchas vidas para que el mundo se acabara.

---

## Las torres de Hanoi

- El problema de las torres de Hanoi también es muy recurrido para ilustrar el concepto de recursividad.
- El problema consiste en mover todos los discos de un poste a otro, cumpliendo con las siguientes reglas:
  - Solo se puede mover un disco a la vez.
  - Solo se puede mover el disco que se encuentre en la punta de un poste.
  - Nunca se puede colocar un disco más grande sobre uno más pequeño.
- Si bien existen varias soluciones para el problema, nos enfocaremos en la solución recursiva.

---

## Las torres de Hanoi

- En el relato, se mencionan 3 postes y 64 discos, lo que se requiere es calcular el número de movimientos que se necesitan para mover los 64 discos desde el primer al último poste.
- Para calcular el número de movimientos, se debe entender cuantos movimientos se acumulan por cada disco en el problema:
  - Si se tiene un disco, sólo se requiere un movimiento.
  - Si se tienen dos discos, se necesitan 3 movimientos: mover el disco 1 al poste 2, mover el disco 2 al poste 3, mover el disco 1 al poste 3.
  - Si se tienen tres discos, se necesitan 7 movimientos: el disco 1 al poste 3, el disco 2 al poste 2, el disco 1 al poste 2, el disco 3 al poste 3, el disco 1 al poste 1, el disco 2 al poste 3, el disco 1 al poste 3.

---

## Las torres de Hanoi

:::: flex
::: col 1/2 px-2

- Se observa que cada que se agrega un disco, se acumulan el doble de movimientos que se tenían hasta el momento, más un movimiento adicional.

| Discos | Movimientos | Desglose |
| :----: | :---------: | :------: |
| 1     | 1           | 1        |
| 2     | 3           | 1 + 1 + 1 |
| 3     | 7           | 3 + 1 + 3 |
| 4     | 15          | 7 + 1 + 7 |

:::
::: col 1/2 px-2

- El número de movimientos se puede calcular mediante la siguiente fórmula:

$$
2^n - 1
$$

- Donde $n$ es el número de discos.
- Para el caso de las torres de Hanoi, se requieren $2^{64} - 1$ movimientos, lo que equivale a 18,446,744,073,709,551,615 movimientos.

:::
::::

---

## Las torres de Hanoi y la recursividad

- Aunque no es estrictamente necesario, también se puede resolver el problema de la torres de Hanoi usando recursividad.
- La función para calcular el número de movimientos se puede definir de manera recursiva como:

$$
movimientos(n) = \left\{
\begin{array}{ll}
1 & \text{si } n = 1 \\
2 \times movimientos(n - 1) + 1 & \text{si } n > 1
\end{array}
\right.
$$

- La función se puede implementar de la siguiente manera:

```python
def movimientos(n):
  if n == 1:
    return 1
  else:
    return 2 * movimientos(n - 1) + 1
```

---

## Las torres de Hanoi y la recursividad

- Este problema pareciera no necesitar la recursividad, ya que se tiene una fórmula directa para calcular el número de movimientos.
- Sin embargo, la solución recursiva muestra cómo se puede dividir el problema en problemas más pequeños que se resuelven de la misma manera, además de plantear la solución del problema de una manera más entendible.

### Fórmula

$$
2^n - 1
$$

### Recursividad

$$
movimientos(n) = \left\{
\begin{array}{ll}
1 & \text{si } n = 1 \\
2 \times movimientos(n - 1) + 1 & \text{si } n > 1
\end{array}
\right.
$$

:::: flex
::: col 1/2 px-2

:::
::: col 1/2 px-2

:::
::::

---

<!-- _class: inverted -->

::: coding
:::

---

# Problemas recursivos

## El problema de los conejos :rabbit:

![bg right:45%](../src/assets/illustration/fibbonacci-rabbits.jpeg)

Un granjero compró un par de conejos que se reproducen cada mes, sabe que los conejos tardan dos meses en alcanzar la madurez y, a partir de entonces, dan a luz a un par de conejos cada mes.

El granjero quiere saber cuántos pares de conejos habrá en un año.

---

## El problema de los conejos 🐇🐇

La solución al problema de los conejos es la siguiente:

- En el primer mes, habrá un par de conejos (el par original).
- En el segundo mes, habrá dos pares de conejos (el par original y el par que nació).
- En el tercer mes, habrá tres pares de conejos (el par original, el par que nació en el segundo mes y el par que nació en el tercer mes).
- Y así sucesivamente...

---

## El problema de los conejos 🐇🐇🐇

- El problema de los conejos requiere de una función que calcule el número de conejos que habrá en un mes determinado.
- Esta función requiere del número de conejos que había en el mes anterior, y del número de conejos que nacieron en el mes anterior, mismos que a su vez requieren de sus respectivos valores anteriores.
- Es un claro ejemplo de recursividad, ya que se requiere de un caso base y de un cambio de estado para acercarse al caso base.
- La función se puede definir de manera recursiva como:

$$
conejos(n) = \left\{
\begin{array}{ll}
1 & \text{si } n = 1 \\
2 & \text{si } n = 2 \\
conejos(n - 1) + conejos(n - 2) & \text{si } n > 2
\end{array}
\right.
$$

---

## Conejos, Fibonacci y recursividad 🐇🐇🐇🐇🐇

- El problema de los conejos fue planteado por el matemático italiano Leonardo de Pisa, mejor conocido como Fibonacci, en su libro _Liber Abaci_ en el año 1202.
- El problema anterior asemeja la sucesión de Fibonacci, la cual se puede definir de manera recursiva como:

$$
fibonacci(n) = \left\{
\begin{array}{ll}
0 & \text{si } n = 0 \\
1 & \text{si } n = 1 \\
fibonacci(n - 1) + fibonacci(n - 2) & \text{si } n > 1
\end{array}
\right.
$$

- Adicionalmente al caso base, la sucesión de Fibonacci tiene un caso base adicional, que es el número 0.

---

## Conejos, Fibonacci y recursividad 🐇🐇🐇🐇🐇🐇🐇🐇

- Resulta que la sucesión de Fibonacci es la solución al problema de los conejos.
- Recordemos que la sucesión de Fibonacci es la siguiente:

$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
$$

- Para el caso de los conejos, la sucesión de Fibonacci se puede interpretar de la siguiente manera:

$$
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
$$

- Con lo anterior, al final del año, en el mes 12, habrá 144 pares de conejos.

---

# Resumen

- La recursividad es una técnica poderosa que se puede utilizar para resolver problemas complejos.
- Sin embargo, no siempre es la mejor opción, ya que puede ser menos eficiente que una solución iterativa.
- La recursividad es una herramienta que se debe utilizar cuando sea adecuada, y no como una pieza intercambiable con los ciclos.
- Antes de implementar una solución recursiva, hay que conocer el problema que se resuelve, así como las implementaciones propias del lenguaje de programación que se utilice.

---

<!-- _class: inverted -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

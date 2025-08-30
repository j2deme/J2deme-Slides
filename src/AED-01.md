---
marp: true
title: Algoritmia y Estructuras de Datos - 01 - Análisis y Diseño de Algoritmos
author: Jaime Jesús Delgado Meraz
header: Algoritmia y Estructuras de Datos - U1
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

# Análisis y Diseño de Algoritmos

## Algoritmia y Estructuras de Datos

Dr. Jaime Jesús Delgado Meraz

### Unidad 01

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

1. [Definición](#definición)
2. [Complejidad algorítmica](#complejidad-algorítmica)

---

# Competencia Específica de la Unidad

> Diseña, analiza y evalúa la eficiencia de algoritmos para resolver problemas computacionales diversos, comprendiendo diferentes técnicas de diseño y su implementación en código funcional.

---

<!-- _class: lead -->

# Definición

---

<!-- _class: cols-2 -->

# Definición

## ¿Qué es un algoritmo?

::: left

Un **algoritmo** es una **secuencia finita, precisa y efectiva** de pasos bien definidos para resolver un problema o realizar una tarea.

> 📌 _No es código, es una idea. El código es solo una forma de expresarlo._

:::
::: right

**Características clave**:

- **Finitud**: Debe terminar en un número finito de pasos.
- **Precisión**: Cada paso debe ser claro y no ambiguo.
- **Entrada bien definida**: Datos iniciales necesarios.
- **Salida esperada**: Resultado específico y verificable.
- **Eficiencia**: Uso óptimo de recursos (tiempo y memoria).

:::

---

<!-- _class: split -->

# Definición

## ¿Qué es un algoritmo?

::: left

**Ejemplo cotidiano**: Algoritmo para hacer café ☕

1. Hervir agua.
2. Colocar café molido en el filtro.
3. Verter agua caliente sobre el café.
4. Esperar a que se filtre.
5. Servir en una taza.

:::
::: right

**Ejemplo computacional**: Algoritmo para calcular el área de un círculo

1. Leer el valor del radio $r$.
2. Calcular $area = \pi * r^2$.
3. Mostrar el resultado.

:::
::: bottom

> 💡 _Ambos son algoritmos: uno físico, otro abstracto, sin embargo, ambos siguen una lógica clara._

:::

---

<!-- _class: split -->

# Definición

## Algoritmo vs Programa

::: left

### Algoritmo

- Idea abstracta de solución
- Independiente del lenguaje
- Enfocado en _qué_ y _cómo_
- Puede expresarse en pseudocódigo, diagramas, palabras
- Es universal: puede aplicarse en cualquier contexto

:::

::: right

### Programa

- Implementación concreta en un lenguaje
- Ejecutable por una máquina
- Incluye detalles técnicos (variables, sintaxis)
- Depende del entorno y lenguaje usado

:::
::: bottom
[tip: Un algoritmo bien diseñado puede implementarse en cualquier lenguaje.]
:::

---

<!-- _class: cols-2 -->

# Definición

## Algoritmo vs Programa

::: left

### Algoritmo

Suma de dos números:

1. Leer `a` y `b`.
2. Calcular `suma = a + b`.
3. Devolver `suma`.

:::

::: right

### Programa

```python
def sumar(a, b):
  return a + b

resultado = sumar(5, 3)
print(resultado)
```

```bash
8
```

:::

---

# Definición

## ¿Qué es la complejidad algorítmica?

La **complejidad algorítmica** mide cómo crece el **tiempo de ejecución** o el **uso de memoria** de un algoritmo a medida que aumenta el tamaño de la entrada ($n$).

> 🔍 _No todos los algoritmos son igual de buenos, pero un algoritmo eficiente puede manejar millones de datos en segundos._

### Tipos principales

- **Complejidad temporal**: tiempo de ejecución.
- **Complejidad espacial**: memoria utilizada.

**Ejemplo**:

- Buscar una palabra en un diccionario desordenado → $O(n)$ (lineal).
- Buscar en un diccionario ordenado (búsqueda binaria) → $O(\log n)$ (logarítmica).

---

# Definición

## Notación Big O

La **notación Big O** describe el **peor caso** del crecimiento de un algoritmo, es decir, cómo se comporta el tiempo de ejecución o el uso de memoria a medida que aumenta el tamaño de la entrada.

**¿Por qué es importante?**

- Permite comparar algoritmos independientemente del hardware.
- Ayuda a predecir el comportamiento con grandes volúmenes de datos.

> 📘 _Nos interesa el límite superior: "este algoritmo nunca será peor que..."_

---

# Definición

## Notación Big O

| Notación    | Nombre      | Ejemplo típico                  |
| ----------- | ----------- | ------------------------------- |
| $O(1)$      | Constante   | Acceder a un arreglo por índice |
| $O(\log n)$ | Logarítmica | Búsqueda binaria                |
| $O(n)$      | Lineal      | Búsqueda lineal                 |
| $O(n^2)$    | Cuadrática  | Bucles anidados                 |
| $O(2^n)$    | Exponencial | Problema de la mochila          |
| $O(n!)$     | Factorial   | Problema del vendedor viajero   |

> ⚠️ Big O ignora constantes: $O(3n + 5)$ = $O(n)$

---

# Definición

## Notación Big O

- Es importante entender que la notación Big O se centra en el **peor caso** de un algoritmo, lo que significa que describe cómo se comporta el tiempo de ejecución o el uso de memoria a medida que aumenta el tamaño de la entrada.
- No se ocupa de los casos promedio o mejores, ya que estos pueden ser engañosos, sin embargo, existen notaciones alternativas como la notación Big Omega ($\Omega$) para el mejor caso y Big Theta ($\Theta$) para el caso promedio.

Estas no son tan comunes como la notación Big O, pero son útiles para un análisis más completo.

::: info
Para motivos del curso, nos centraremos en la notación Big O.
:::

---

# Definición

## Problema del mundo real: Promedio de calificaciones

Supongamos que eres un profesor y necesitas calcular el **promedio de 5 calificaciones** de un estudiante.

**Algoritmo**:

1. Leer las 5 calificaciones.
2. Sumarlas.
3. Dividir la suma entre 5.
4. Mostrar el resultado.

---

# Definición

## Implementación en Python

```python
calificaciones = [85, 90, 78, 92, 88]
suma = 0

for cal in calificaciones:
    suma += cal

promedio = suma / len(calificaciones)
print(f"Promedio: {promedio:.2f}")
```

- **Complejidad temporal**: $O(n)$
- **Complejidad espacial**: $O(1)$ (solo usamos `suma` y `cal`)

---

# Definición

## Estructuras de datos

Una **estructura de datos** es una forma de **organizar, almacenar y gestionar** la información en un programa para que pueda ser utilizada de manera eficiente.

Las estructuras de datos permiten representar información compleja en memoria y facilitan operaciones como búsqueda, inserción, eliminación y recorrido.

> 💡 _Elegir la estructura adecuada es tan importante como el algoritmo que la procesa._

---

<!-- _class: split -->

# Definición

## Clasificación general

::: top
Las estructuras de datos se clasifican en dos grandes categorías:
:::
::: left

### Lineales

- Los elementos se organizan en una **secuencia**.
- Cada elemento tiene un **predecesor y sucesor**, excepto el primero y el último.
- Ejemplos: arreglos, listas, pilas, colas.

:::
::: right

### No lineales

- Los elementos **no siguen una secuencia**.
- Cada elemento puede estar conectado a varios otros.
- Ejemplos: árboles, grafos.

:::

---

# Definición

## Ejemplos comunes y sus usos

| Estructura         | Tipo      | Características principales                       | Ejemplo de uso                         |
| ------------------ | --------- | ------------------------------------------------- | -------------------------------------- |
| **Arreglo**        | Lineal    | Acceso directo por índice, tamaño fijo.           | Almacenar calificaciones de un examen. |
| **Lista**          | Lineal    | Dinámica, permite inserción/eliminación flexible. | Lista de tareas pendientes.            |
| **Pila**           | Lineal    | LIFO (Last In, First Out).                        | Historial de navegación web.           |
| **Cola**           | Lineal    | FIFO (First In, First Out).                       | Impresión en cola.                     |
| **Lista enlazada** | Lineal    | Nodos conectados por punteros.                    | Implementar pilas o colas dinámicas.   |
| **Árbol**          | No lineal | Jerarquía, nodos con hijos.                       | Sistema de archivos, árbol DOM.        |
| **Grafo**          | No lineal | Nodos conectados por aristas.                     | Mapas, redes sociales.                 |

---

# Definición

## ¿Por qué importan las estructuras de datos?

La elección de una estructura de datos impacta directamente en:

Eficiencia del algoritmo
: Algunas operaciones son más rápidas en ciertas estructuras.
: _p.e._ buscar en un arreglo desordenado es $O(n)$, pero en uno ordenado puede ser $O(\log n)$ con búsqueda binaria.

Uso de memoria
: Algunas estructuras usan más espacio pero ofrecen mejor rendimiento.
: _p.e._ una lista enlazada usa más memoria por los punteros, pero permite crecer dinámicamente.

---

# Definición

## ¿Por qué importan las estructuras de datos?

Facilidad de mantenimiento
: Estructuras claras facilitan el desarrollo y la depuración.
: _p.e._ usar una pila para deshacer acciones (`Ctrl+Z`) es intuitivo y eficiente.

> 🧠 _"La estructura correcta puede convertir un algoritmo inútil en uno brillante."_

---

# Definición

## Ejemplo práctico: Escenario de hospital

Supongamos un sistema de gestión en un hospital, distintas estructuras de datos pueden modelar distintos procesos:

- **Pila**: para manejar emergencias que deben atenderse inmediatamente (LIFO).
- **Cola**: para turnos médicos generales (FIFO).
- **Montículo (heap)**: para priorizar pacientes según gravedad (cola de prioridad).
- **Lista enlazada**: para mantener un historial clínico dinámico.
- **Árbol binario de búsqueda**: para buscar rápidamente registros de pacientes por ID.

---

# Definición

## Relación con algoritmos

Cada estructura de datos **favorece ciertos algoritmos**:

- **Arreglos ordenados** → Búsqueda binaria ($O(\log n)$)
- **Listas enlazadas** → Inserción rápida en cualquier posición ($O(1)$ si tienes el nodo)
- **Árboles binarios balanceados** → Búsqueda, inserción y eliminación en $O(\log n)$
- **Grafos** → Algoritmos de recorrido como DFS o BFS

> 🔄 _"Una buena estructura de datos es la base para un buen algoritmo."_

---

# Definición

## Resumen conceptual

| Concepto                | Definición breve                                      |
| ----------------------- | ----------------------------------------------------- |
| **Algoritmo**           | Secuencia de pasos para resolver un problema.         |
| **Programa**            | Implementación de un algoritmo en un lenguaje.        |
| **Complejidad**         | Medida del tiempo y espacio que consume un algoritmo. |
| **Big O**               | Notación para describir el peor caso de crecimiento.  |
| **Estructura de datos** | Forma de organizar y gestionar datos en memoria.      |

---

<!-- _class: lead -->

# Complejidad algorítmica

---

# Complejidad algorítmica

## ¿Por qué medir la eficiencia?

No todos los algoritmos que resuelven un problema son igualmente buenos.  
La **eficiencia** determina si un algoritmo es práctico, especialmente con grandes volúmenes de datos.

> 🔍 _Un algoritmo óptimo puede procesar millones de datos en segundos; uno ineficiente podría tardar días._

:::: flex
::: col 1/2 px-2

**¿Qué medimos?**

- Tiempo de ejecución
- Uso de memoria (RAM)
- Uso de recursos del sistema

:::
::: col 1/2 px-2

**¿Cuándo importa?**

- Aplicaciones en tiempo real
- Big Data
- Sistemas embebidos
- IA y machine learning

:::
::::

---

# Complejidad algorítmica

## Conceptos de complejidad algorítmica

La **complejidad algorítmica** mide cómo crece el **tiempo de ejecución** o el **uso de memoria** cuando aumenta el tamaño de la entrada.

Dos tipos principales:

- **Complejidad temporal**: tiempo de ejecución.
- **Complejidad espacial**: memoria utilizada.

> 📈 Nos enfocamos en el **comportamiento asintótico** (cuando $n \to \infty$).

**Asintótico**
: Se refiere al comportamiento de un algoritmo a medida que el tamaño de la entrada se vuelve muy grande.

---

# Complejidad algorítmica

## Casos de análisis

Al analizar un algoritmo, consideramos tres escenarios:

:::: flex
::: col 1/3 px-2

### Mejor caso

- El escenario más favorable.
- _p.e._ encontrar un elemento en la primera posición.

:::
::: col 1/3 px-2

### Caso promedio

- Comportamiento esperado con entradas aleatorias.
- Más difícil de calcular, pero más realista.

:::
::: col 1/3 px-2

### Peor caso

- El escenario más desfavorable.
- Es el que usamos en Big O.

:::
::::

> 🧠 _Big O se enfoca en el peor caso porque garantiza un límite superior._

---

# Complejidad algorítmica

## Análisis de eficiencia (tiempo y espacio)

```js
function sumaHastaN(n) {
  let suma = 0;

  for (let i = 1; i <= n; i++) {
    suma += i;
  }

  return suma;
}
```

- **Tiempo**: el bucle se repite `n` veces → crece linealmente ($O(n)$)
- **Espacio**: solo se usan `suma` e `i` → constante ($O(1)$).

> 🧪 _Este algoritmo es eficiente en espacio, pero lineal en tiempo._

---

# Complejidad algorítmica

## Notación Big O

La **notación Big O** describe el **peor caso** del crecimiento de un algoritmo.

> 📘 _Nos interesa el límite superior: "este algoritmo nunca será peor que..."_

**¿Por qué usamos Big O?**

- Permite comparar algoritmos independientemente del hardware.
- Se enfoca en el crecimiento, no en constantes.
- Es estándar en la industria y academia.

> ⚠️ Big O ignora constantes y términos menores: $O(3n + 5) = O(n)$

---

# Complejidad algorítmica

## Clases comunes de Big O

| Notación      | Nombre       | Ejemplo                         |
| ------------- | ------------ | ------------------------------- |
| $O(1)$        | Constante    | Acceder a un arreglo por índice |
| $O(\log n)$   | Logarítmica  | Búsqueda binaria                |
| $O(n)$        | Lineal       | Búsqueda lineal                 |
| $O(n \log n)$ | Linealítmica | MergeSort                       |
| $O(n^2)$      | Cuadrática   | Bucles anidados                 |
| $O(2^n)$      | Exponencial  | Torres de Hanoi                 |
| $O(n!)$       | Factorial    | Problemas de permutación        |

![bg right fit](../src/assets/AED/Comparison_computational_complexity.png)

---

# Complejidad algorítmica

## Ejemplo: Búsqueda lineal vs binaria

**Búsqueda lineal**:

- Revisa cada elemento.
- Peor caso: $n$ pasos.
- **Big O: $O(n)$**

**Búsqueda binaria**:

- Solo en listas **ordenadas**.
- Divide el espacio a la mitad en cada paso.
- **Big O: $O(\log n)$**

> 🚀 Con 1 millón de elementos, busca en ~20 pasos.

---

# Complejidad algorítmica

## ¿Por qué ordenar antes de usar búsqueda binaria?

Si se realizarán **múltiples búsquedas**, ordenar una vez y usar búsqueda binaria **ahorra tiempo**.

- Ordenar toma $O(n \log n)$ (ej. QuickSort).
- Buscar lineal: $O(n)$ por consulta.
- Buscar binaria: $O(\log n)$ por consulta.

::: quote
_"El tiempo invertido en preparar bien los datos, es un ahorro en cada operación posterior."_
:::

---

<!-- _class: split -->

# Complejidad algorítmica

## Ejemplo: Comparando algoritmos

::: top
Supongamos que queremos sumar los números del 1 al $n$:
:::
::: left

### Versión 1 (bucle)

```js
function sumaIterativa(n) {
  let suma = 0;
  for (let i = 1; i <= n; i++) {
    suma += i;
  }
  return suma;
}
```

- Complejidad: $O(n)$

:::
::: right

### Versión 2 (fórmula)

```js
function sumaFormula(n) {
  return (n * (n + 1)) / 2;
}
```

- Complejidad: $O(1)$

:::
::: bottom

> 🧠 _Ambas dan el mismo resultado, pero la segunda es mucho más eficiente._

:::

---

<!-- _class: cols-2 -->

# Complejidad algorítmica

## ¿Cómo se calcula Big O?

::: left

Pasos básicos:

1. **Identificar operaciones dominantes**: bucles, recursión.
2. **Contar cuántas veces se ejecutan**.
3. **Eliminar constantes y términos menores**.

:::
::: right

<!-- prettier-ignore-start -->
```js
function ejemplo(n) {
  let a = 5; // O(1)
  for (let i = 0; i < n; i++) { // O(n)
    console.log(i); // O(1)
  }
  for (let j = 0; j < n; j++) { // O(n)
    for (let k = 0; k < n; k++) { // O(n)
      console.log(j, k); // O(1)
    }
  }
}
```
<!-- prettier-ignore-end -->

- Total: $O(1) + O(n) + O(n^2)$
- Eliminar constantes: $O(n) + O(n^2)$
- Eliminar términos menores: $O(n^2)$
- **Resultado final: $O(n^2)$**

:::

---

<!-- _class: cols-2 -->

# Complejidad algorítmica

## Ejemplo: Bucles anidados

::: left

```js
function imprimirPares(n) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      console.log(i, j);
    }
  }
}
```

:::
::: right

- El bucle externo se ejecuta $n$ veces.
- Por cada iteración del externo, el interno también se ejecuta $n$ veces.
- Total de operaciones: $n * n = n^2$

> 🧮 **Complejidad: $O(n^2)$**  
> Este es un ejemplo clásico de **crecimiento cuadrático**.

:::

---

<!-- _class: cols-2 -->

# Complejidad algorítmica

## Ejemplo: Bucles independientes

::: left

```js
function operacionesIndependientes(n) {
  // Primer bucle: O(n)
  for (let i = 0; i < n; i++) {
    console.log("Bucle 1:", i);
  }

  // Segundo bucle: O(n)
  for (let j = 0; j < n; j++) {
    console.log("Bucle 2:", j);
  }

  // Operación constante: O(1)
  console.log("Finalizado");
}
```

:::
::: right

- Primer bucle: $O(n)$
- Segundo bucle: $O(n)$
- Operación constante: $O(1)$
- Total: $O(n) + O(n) + O(1) = O(2n + 1)$

> 🧮 **Complejidad: $O(n)$**  
> Se ignoran constantes por lo que $O(2n + 1)$ se simplifica a $O(n)$.

:::

---

<!-- _class: cols-2-->

# Complejidad algorítmica

## Ejemplo: Búsqueda binaria

::: left

```js
function busquedaBinaria(lista, objetivo) {
  let inicio = 0;
  let fin = lista.length - 1;

  while (inicio <= fin) {
    let medio = Math.floor((inicio + fin) / 2);
    if (lista[medio] === objetivo) {
      return medio;
    } else if (lista[medio] < objetivo) {
      inicio = medio + 1;
    } else {
      fin = medio - 1;
    }
  }
  return -1;
}
```

:::
::: right

- En cada paso, el espacio de búsqueda se **divide a la mitad**.
- ¿Cuántas veces puedes dividir $n$ por 2 hasta llegar a 1?  
  Respuesta: $\log_2(n)$

> 🧮 **Complejidad: $O(\log n)$**  
> Muy eficiente para listas grandes y ordenadas.

:::

---

# Complejidad algorítmica

## Importancia en la vida real

En sistemas grandes, la complejidad marca la diferencia:

| Operación   | $n = 1,000$ | $n = 1,000,000$ |
| ----------- | ----------- | --------------- |
| $O(1)$      | 1 µs        | 1 µs            |
| $O(\log n)$ | 10 µs       | 20 µs           |
| $O(n)$      | 1 ms        | 1 s             |
| $O(n^2)$    | 1 s         | 11.5 días       |

> ⚡ _Un algoritmo cuadrático puede ser inviable con grandes datos._

---

# Complejidad algorítmica

## ¿Cómo medir el tiempo de ejecución?

En Python, podemos usar los módulos `time` o `timeit` para medir el rendimiento de un algoritmo.

**Método 1: `time.time()`**

```python
import time

inicio = time.time()

# Código a medir

suma = 0
for i in range(1_000_000):
    suma += i

fin = time.time()
print(f"Tiempo: {fin - inicio:.4f} segundos")
```

---

# Complejidad algorítmica

## ¿Cómo medir el tiempo de ejecución?

**Método 2: `timeit` (más preciso)**

```python
import timeit

codigo = '''
suma = 0
for i in range(1_000_000):
    suma += i
'''

tiempo = timeit.timeit(codigo, number=10)
print(f"Tiempo promedio: {tiempo / 10:.6f} segundos")
```

> 📏 `timeit` es ideal para comparar algoritmos porque minimiza el impacto de otros procesos.

---

# Complejidad algorítmica

## ¿Cómo comparar el uso de memoria?

Podemos usar el módulo `sys.getsizeof()` para comparar el espacio que ocupan diferentes estructuras.

```python
import sys

lista = [i for i in range(1_000)]
tupla = tuple(i for i in range(1_000))

print(f"Lista: {sys.getsizeof(lista)} bytes")
print(f"Tupla: {sys.getsizeof(tupla)} bytes")
```

> 📊 En general, las **tuplas usan menos memoria** que las listas porque son inmutables.

---

<!-- _class: cols-2 -->

# Complejidad algorítmica

## Comparativa: Bucles vs Fórmula

::: left

```python
import time
import sys

# Versión con bucle
def suma_bucle(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Versión con fórmula
def suma_formula(n):
    return n * (n + 1) // 2

n = 1_000_000

# Medir tiempo
t1 = time.time()
resultado1 = suma_bucle(n)
t2 = time.time()
```

:::
::: right

```python
t3 = time.time()
resultado2 = suma_formula(n)
t4 = time.time()

print(f"Bucle: {t2 - t1:.6f} s")
print(f"Fórmula: {t4 - t3:.6f} s")

# Medir memoria (tamaño de la función)
print("= Memoria =")
print(f"Bucle: {sys.getsizeof(suma_bucle)} bytes")
print(f"Fórmula: {sys.getsizeof(suma_formula)} bytes")
```

:::

---

# Complejidad algorítmica

## Ejemplo: Números de Fibonacci

Los números de Fibonacci forman una secuencia donde cada número es la suma de los dos anteriores:

$$
F_0 = 0,\ F_1 = 1,\ F_n = F_{n-1} + F_{n-2}
$$

Secuencia: `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`

**Problema**: Calcular el $n$-ésimo número de Fibonacci.

---

# Complejidad algorítmica

## Versión 1: Recursión simple (ineficiente)

```python
def fibonacci_recursivo(n):
  if n <= 1:
    return n
  return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
```

- **Complejidad temporal**: $O(2^n)$ → exponencial.
- **Complejidad espacial**: $O(n)$ → por la pila de llamadas.

> ⚠️ _Muy lento para n > 40, cada llamada genera dos nuevas llamadas._

---

# Complejidad algorítmica

## Versión 2: Iteración (eficiente)

```python
def fibonacci_iterativo(n):
  if n <= 1:
    return n
  a, b = 0, 1
  for _ in range(2, n + 1):
    a, b = b, a + b
  return b
```

- **Complejidad temporal**: $O(n)$ → lineal.
- **Complejidad espacial**: $O(1)$ → solo usa tres variables.

> ✅ _Mucho más rápido y eficiente en memoria._

---

# Complejidad algorítmica

## Medición de tiempo: Configuración

```python
import time
import sys

n = 35 # Valor manejable para ver la diferencia

print(f"Calculando F({n})...")
```

---

# Complejidad algorítmica

## Medición de tiempo: Recursivo

```python
inicio = time.time()
resultado_rec = fibonacci_recursivo(n)
fin = time.time()

print(f"Recursivo: {resultado_rec}")
print(f"Tiempo: {fin - inicio:.4f} segundos")
```

- Para `n = 35`, puede tardar entre 1 y 5 segundos.
- El tiempo crece **exponencialmente** con `n`.

---

# Complejidad algorítmica

## Medición de tiempo: Iterativo

```python
inicio = time.time()
resultado_iter = fibonacci_iterativo(n)
fin = time.time()

print(f"Iterativo: {resultado_iter}")
print(f"Tiempo: {fin - inicio:.6f} segundos")
```

- Para `n = 35`, toma menos de 0.001 segundos.
- Diferencia de tiempo: **miles de veces más rápido**.

---

# Complejidad algorítmica

## Comparativa final

| Algoritmo | Complejidad | Tiempo (n=35) | Memoria     |
| --------- | ----------- | ------------- | ----------- |
| Recursivo | $O(2^n)$    | ~2.0 s        | Alta (pila) |
| Iterativo | $O(n)$      | ~0.00001 s    | $O(1)$      |

> 🧠 _Una mala elección de algoritmo puede hacer un programa inviable, incluso con hardware potente._

---

<!-- _class: primary centered pattern -->

> _"La práctica no hace al maestro, la práctica **dirigida** hace al maestro."_
>
> <cite>Anders Ericsson, científico cognitivo</cite>

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

---

<!-- paginate: skip -->
<!-- class: references -->

# Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). _Introduction to Algorithms_ (4th ed.). MIT Press.
- Bhargava, A. Y. (2016). _Grokking Algorithms_. Manning Publications. [https://github.com/egonspace/grokking-algorithms](https://github.com/egonspace/grokking-algorithms)
- Skiena, S. S. (2020). _The Algorithm Design Manual_ (3rd ed.). Springer. [https://www3.cs.stonybrook.edu/~skiena/algorist/](https://www3.cs.stonybrook.edu/~skiena/algorist/)
- Goodrich, M. T., & Tamassia, R. (2015). _Data Structures and Algorithms in Java_ (6th ed.). Wiley.
- Tecnológico Nacional de México. (2024). _Programa de la asignatura IAD-2401 - Algoritmia y Estructuras de Datos_.

---

# Recursos

- VisuAlgo: Visualizing Data Structures and Algorithms, [https://visualgo.net](https://visualgo.net)
- AlgoViz: Algorithm Visualizations, [https://algoviz.org](https://algoviz.org)
- USFCA Interactive Python, [https://www.cs.usfca.edu/~galles/visualization/Algorithms.html](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
- Harvard CS50: Algorithms (YouTube), [https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv](https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv)
- Brilliant.org: Algorithms Course, [https://brilliant.org/courses/algorithms/](https://brilliant.org/courses/algorithms/)
- LeetCode: Problems & Visualizations, [https://leetcode.com](https://leetcode.com)
- HackerRank: Data Structures & Algorithms, [https://www.hackerrank.com/domains/data-structures](https://www.hackerrank.com/domains/data-structures)
- The Coding Train (YouTube), [https://www.youtube.com/c/TheCodingTrain](https://www.youtube.com/c/TheCodingTrain)
- Big-O Cheat Sheet, [https://www.bigocheatsheet.com](https://www.bigocheatsheet.com)

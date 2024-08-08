---
marp: true
title: EDD - 04 - Estructuras No Lineales
author: Jaime Jesús Delgado Meraz
header: Estructuras de Datos - U4
footer: '[&oast;](#contenidos) **MSC. JJDM**'
paginate: true
theme: j2deme
math: mathjax
style: |
  :root {
    --primary: #2563eb;
    --secondary: #ebad25;
  }
---
<!-- _paginate: false -->

# Unidad 4

# <!-- fit --> Estructuras No Lineales

## Estructuras de Datos

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
: Estructuras de Datos

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
2. [Nodo](#nodo)
3. [Árboles](#árboles)
4. [Grafos](#grafos)

---
<!-- _class: lead -->
# Introducción

---

# Introducción

- Las estructuras de datos no lineales son aquellas en las que los elementos no están organizados de manera secuencial.
- Son más complejas que las estructuras lineales, sin embargo, esta complejidad también les permite resolver problemas más complejos y variados.
- Las estructuras no lineales también sirven para representar relaciones entre los elementos.

---
<!-- _class: lead -->
# Nodo

---

# Nodo

- Dentro de las estructuras no lineales, el nodo es el elemento básico, al igual que en las estructuras lineales.
- Sin embargo, en las estructuras no lineales, el nodo puede tener más de una relación con otro nodo, lo que permite representar relaciones más complejas.
- _P.e._ en un árbol, un nodo puede tener dos o más hijos, según el tipo de árbol.

![bg right h:85%](../src/assets/EDD/Ejemplo-nodos-no-lineales.png)

---

# Nodo

- Por lo general, un nodo en una estructura no lineal contiene la información del elemento y las referencias a los nodos con los que tiene relación.
- Según se requiera, el nodo podrá usar referencias directas a otros nodos o incluso referencias a estructuras de datos que contienen a otros nodos.
- Al igual que en las estructuras lineales, los nodos y las respectivas estructuras, pueden ser implementados como clases mediante programación orientada a objetos, lo que facilita su uso y mantenimiento.

---
<!-- _class: lead -->
# Árboles

---

# Árboles

> Un árbol es una estructura de datos no lineal que se compone de nodos, donde cada nodo tiene un valor y una lista de referencias a otros nodos.

- Los árboles son estructuras jerárquicas, donde un nodo se considera padre de otro nodo si tiene una referencia a él.
- A su vez, los nodos hijos pueden tener sus propios hijos, formando una estructura en forma de árbol.

::: warning
⚠ Un árbol no puede tener ciclos, es decir, un nodo hijo no puede tener una referencia a un nodo padre como su hijo.
:::

---

# Árboles

- Un árbol tiene un nodo raíz, que es el nodo principal del árbol 🌱.
- Los nodos que no tienen hijos se llaman hojas 🍃, mientras que aquellos que si tienen hijos se denominan ramas 🌿.
- Es posible que un árbol tenga un solo nodo, en cuyo caso, este nodo es la raíz y también es una hoja.

![bg right h:85%](../src/assets/EDD/Ejemplo-árbol.png)

---

# Árboles

## Características

- La **altura** de un árbol es la longitud del camino más largo desde la raíz hasta una hoja.
- La **anchura** de un árbol es el número máximo de nodos que hay en un nivel, es decir, el número de nodos en el nivel más grande.
- La **profundidad** de un nodo es la longitud del camino desde la raíz hasta el nodo, es decir, el número de aristas que hay en el camino.
- Al número de hijos que puede tener un nodo se le llama **grado**.

---

# Árboles

## Clasificación

- Con base en el grado de los nodos, los árboles se pueden clasificar en:
  - **Árbol binario**: cada nodo tiene a lo más 2 hijos, uno izquierdo y uno derecho, si no tiene un hijo, se le asigna un valor nulo al hijo faltante.
  - **Árbol ternario**: cada nodo tiene a lo más 3 hijos, uno izquierdo, uno central y uno derecho, se puede generalizar a un árbol n-ario.
  - **Árbol n-ario**: cada nodo puede tener la cantidad de hijos que se requiera y puede tener un número variable de hijos en cada nodo.

---

# Árboles

## Clasificación: Casos especiales

- Además de la clasificación por el grado de los nodos, los árboles también se pueden clasificar por su forma (donde $n$ es el grado del árbol):
  - **Árbol raíz**: un árbol con un solo nodo.
  - **Árbol completo**: todos los nodos tienen a lo más $n$ hijos y todos los nodos hoja están en el último nivel.
  - **Árbol balanceado**: todos los nodos tienen a lo más $n$ hijos y la diferencia de altura entre los subárboles izquierdo y derecho es a lo más 1.
  - **Árbol degenerado**: todos los nodos tienen a lo más 1 hijo, es decir, es una lista enlazada.

---

# Árboles

## Operaciones

- Algunas de las operaciones más comunes que se pueden realizar con árboles son:
  - **Inserción**: agregar un nuevo nodo al árbol.
  - **Eliminación**: eliminar un nodo del árbol.
  - **Recorrido**: visitar todos los nodos de un árbol.
  - **Búsqueda**: encontrar un nodo con un valor específico.
  - **Altura**: determinar la altura del árbol.
  - **Anchura**: determinar la anchura del árbol.
- Estas operaciones pueden variar según el tipo de árbol y la implementación.

---
<!-- _class: inverted -->

### Mejora a Nodo Doble

- Para mejorar la compatibilidad y reutilización de código, se modificará la clase `NodoDoble` con referencias a los nodos izquierdo y derecho.

:::: flex
::: col 1/2

```python
@property
def izquierdo(self):
    return self.anterior

@izquierdo.setter
def izquierdo(self, inp):
    self.anterior = inp

@izquierdo.deleter
def izquierdo(self):
    del self.anterior
```

:::
::: col 1/2

```python
    @property
    def derecho(self):
        return self.siguiente

    @derecho.setter
    def derecho(self, inp):
        self.siguiente = inp

    @derecho.deleter
    def derecho(self):
        del self.siguiente
```

:::
::::

- Estas funciones ayudarán a mejorar la compatibilidad con las estructuras no lineales.

---

# Árboles

## Implementación de un árbol binario

:::: flex
::: col 1/2

```python
class NodoBinario(NodoDoble):
    def __init__(self, valor):
        super().__init__(valor)
```

:::
::: col 1/2

```python
class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.tamanio = 0
```

:::
::::

- Aunque es posible reutilizar directamente la clase `NodoDoble` de las estructuras lineales, se puede creará una clase `NodoBinario` que herede de `NodoDoble` para que sea más específica.

---

# Árboles

## Implementación de un árbol binario: Inserción

:::: flex
::: col 2/3 px-2

```python
def insertar(self, valor):
    nuevo_nodo = NodoBinario(valor)
    if self.raiz is None:
        self.raiz = nuevo_nodo
    else:
        self.__insertar(self.raiz, nuevo_nodo)
    self.tamanio += 1

def __insertar(self, nodo, nuevo_nodo):
    if nuevo_nodo.valor < nodo.valor:
        if nodo.izquierdo is None:
            nodo.izquierdo = nuevo_nodo
        else:
            self.__insertar(nodo.izquierdo, nuevo_nodo)
    else:
        if nodo.derecho is None:
            nodo.derecho = nuevo_nodo
        else:
            self.__insertar(nodo.derecho, nuevo_nodo)
```

:::
::: col 1/3 px-2

- La inserción en un árbol binario se realiza de manera recursiva, comparando el valor del nuevo nodo con el valor del nodo actual y decidiendo si se inserta a la izquierda o a la derecha.

:::
::::

---

# Árboles

## Implementación de un árbol binario: Eliminación

```python
def eliminar(self, valor):
    if self.raiz is not None:
        self.raiz = self.__eliminar(self.raiz, valor)
        self.tamanio -= 1

def __eliminar(self, nodo, valor):
    if nodo is None:
        return nodo
    if valor < nodo.valor:
        nodo.izquierdo = self.__eliminar(nodo.izquierdo, valor)
    elif valor > nodo.valor:
        nodo.derecho = self.__eliminar(nodo.derecho, valor)
    else:
        if nodo.izquierdo is None:
            return nodo.derecho
        elif nodo.derecho is None:
            return nodo.izquierdo
```

---

# Árboles

## Implementación de un árbol binario: Recorrido

- Los recorridos en un árbol binario se pueden realizar de diferentes maneras, las más comunes son:
  - **Preorden**: primero se visita el nodo actual, luego el subárbol izquierdo y finalmente el subárbol derecho.
  - **Inorden**: primero se visita el subárbol izquierdo, luego el nodo actual y finalmente el subárbol derecho.
  - **Postorden**: primero se visita el subárbol izquierdo, luego el subárbol derecho y finalmente el nodo actual.

::: info
ℹ Los recorridos en un árbol binario se realizan de manera recursiva, visitando los nodos en el orden indicado.
:::

---

# Árboles

## Implementación de un árbol binario: Recorrido

:::: flex
::: col 1/2 px-2

```python
def preorden(self):
    self.__preorden(self.raiz)

def inorden(self):
    self.__inorden(self.raiz)

def postorden(self):
    self.__postorden(self.raiz)
```

- Los métodos `__preorden`, `__inorden` y `__postorden` son métodos privados que se encargan de realizar el recorrido de manera recursiva.

:::
::: col 1/2 px-2

```python
def __preorden(self, nodo):
    if nodo is not None:
        print(nodo.valor)
        self.__preorden(nodo.izquierdo)
        self.__preorden(nodo.derecho)

def __inorden(self, nodo):
    if nodo is not None:
        self.__inorden(nodo.izquierdo)
        print(nodo.valor)
        self.__inorden(nodo.derecho)

def __postorden(self, nodo):
    if nodo is not None:
        self.__postorden(nodo.izquierdo)
        self.__postorden(nodo.derecho)
        print(nodo.valor)
```

:::
::::

---

# Árboles

## Implementación de un árbol binario: Búsqueda

- Los árboles binarios están ordenados, lo que facilita la búsqueda de un valor específico, ya que se puede comparar el valor con el nodo actual y decidir si se busca en el subárbol izquierdo o derecho.

```python
def buscar(self, valor):
    return self.__buscar(self.raiz, valor)

def __buscar(self, nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    if valor < nodo.valor:
        return self.__buscar(nodo.izquierdo, valor)
    return self.__buscar(nodo.derecho, valor)
```

---

# Árboles

## Implementación de un árbol binario: Altura

- La altura de un árbol se puede determinar de manera recursiva, calculando la altura de los subárboles izquierdo y derecho y sumando 1 al máximo de ambas alturas.

```python
def altura(self):
    return self.__altura(self.raiz)

def __altura(self, nodo):
    if nodo is None:
        return 0
    return 1 + max(self.__altura(nodo.izquierdo), self.__altura(nodo.derecho))
```

---

# Árboles

## Implementación de un árbol binario: Anchura

- La anchura del árbol se calcula recursivamente obteniendo la cantidad de nodos en cada nivel y retornando el máximo de estos valores.

:::: flex
::: col 1/2

```python
def anchura(self):
    return self.__anchura(self.raiz)

def __anchura(self, nodo):
    if nodo is None:
        return 0

    cola = Cola()
    cola.encolar(nodo)

    max_ancho = 0
    nivel_ancho = 1
    # Continua while
```

:::
::: col 1/2

```python
while cola.esta_vacia() is False:
    for _ in range(nivel_ancho):
        if cola.esta_vacia():
            break
        actual = cola.desencolar()

        if actual.izquierdo:
            cola.encolar(actual.izquierdo)
        if actual.derecho:
            cola.encolar(actual.derecho)

    if cola.size() > max_ancho:
        max_ancho = cola.size()

    nivel_ancho = cola.size()

return max_ancho
```

:::
::::

---

# Árboles

## Implementación de un árbol n-ario

- La implementación de un árbol n-ario es similar a la de un árbol binario, con la diferencia de que un nodo puede tener un número variable de hijos.
- Identificaremos esta estructura simplemente como `Arbol`.

:::: flex
::: col 1/2

```python
class NodoMultiple:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = ListaDoble()
```

:::
::: col 1/2

```python
class Arbol:
    def __init__(self):
        self.raiz = None
        self.tamanio = 0
```

:::
::::

::: info
ℹ Aunque Python cuenta con su propia implementación de listas, para fines didácticos se puede utilizará la lista doblemente enlazada desarrollada previamente.
:::

---

# Árboles

## Implementación de un árbol n-ario: Inserción

- Se identifica el nodo padre y se le asigna el nuevo hijo, si no se especifica un padre, se asume que el nuevo nodo es la raíz.

```python
def insertar(self, valor, padre=None):
    nuevo_nodo = NodoNario(valor)
    if self.raiz is None:
        self.raiz = nuevo_nodo
    else:
        if padre is None:
            padre = self.raiz
        padre.hijos.insertar(nuevo_nodo)
```

---

# Árboles

## Implementación de un árbol n-ario: Eliminación

- Al eliminar un nodo padre, se eliminan todos los nodos hijos, de manera recursiva.

```python
def eliminar(self, valor):
    if self.raiz is not None:
        self.raiz = self.__eliminar(self.raiz, valor)
        self.tamanio -= 1

def __eliminar(self, nodo, valor):
    if nodo is None: # No hay nodo
        return nodo
    if nodo.valor == valor: # Nodo encontrado
        return None
    for hijo in nodo.hijos: # Se busca en los hijos
        hijo = self.__eliminar(hijo, valor)
    return nodo
```

---

# Árboles

## Implementación de un árbol n-ario: Recorrido

- Los recorridos en un árbol n-ario se pueden realizar de diferentes maneras, las más comunes son:
  - **Preorden**: primero se visita el nodo actual y luego se visitan los hijos.
  - **Postorden**: primero se visitan los hijos y luego el nodo actual.

::: info
ℹ Los recorridos en un árbol n-ario se realizan igualmente de manera recursiva, visitando los nodos en el orden indicado.
:::

---

# Árboles

## Implementación de un árbol n-ario: Recorrido

:::: flex
::: col 1/2 px-2

```python
def preorden(self):
    self.__preorden(self.raiz)

def postorden(self):
    self.__postorden(self.raiz)
```

- Los métodos `__preorden` y `__postorden` son métodos privados que se encargan de realizar el recorrido de manera recursiva.

:::

::: col 1/2 px-2

```python
def __preorden(self, nodo):
    if nodo is not None:
        print(nodo.valor)
        for hijo in nodo.hijos:
            self.__preorden(hijo)

def __postorden(self, nodo):
    if nodo is not None:
        for hijo in nodo.hijos:
            self.__postorden(hijo)
        print(nodo.valor)
```

:::
::::

---

# Árboles

## Implementación de un árbol n-ario: Búsqueda

- La búsqueda en un árbol n-ario se realiza de manera similar a la de un árbol binario, excepto que los nodos pueden tener un número variable de hijos.

```python
def buscar(self, valor):
    return self.__buscar(self.raiz, valor)

def __buscar(self, nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    for hijo in nodo.hijos:
        if self.__buscar(hijo, valor):
            return True
    return False
```

---

# Árboles

## Implementación de un árbol n-ario: Altura

- La altura de un árbol n-ario se puede determinar de manera recursiva.

```python
def altura(self):
    return self.__altura(self.raiz)

def __altura(self, nodo):
    if nodo is None:
        return 0
    altura = 0
    for hijo in nodo.hijos:
        altura = max(altura, self.__altura(hijo))
    return 1 + altura
```

---

# Árboles

## Implementación de un árbol n-ario: Anchura

- La anchura de un árbol n-ario se puede determinar de manera recursiva.

```python
def anchura(self):
    return self.__anchura(self.raiz)

def __anchura(self, nodo):
    if nodo is None:
        return 0
    anchura = 0
    for hijo in nodo.hijos:
        anchura = max(anchura, self.__anchura(hijo))
    return 1 + anchura
```

---

# Árboles

## Aplicaciones

- Los árboles son utilizados en diversas aplicaciones, algunas de las más comunes son:
  - **Árboles de decisión**: se utilizan en inteligencia artificial para tomar decisiones basadas en reglas.
  - **Árboles de búsqueda**: se utilizan en algoritmos de búsqueda para encontrar soluciones a problemas.
  - **Árboles de expresión**: se utilizan en la evaluación de expresiones matemáticas.
  - **Árboles de prefijos**: se utilizan en la representación de palabras y en la búsqueda de palabras en diccionarios.

---
<!-- _class: lead -->
# Grafos
<!-- TODO: Add missing section -->

---

# Grafos

---

# Grafos

## Clasificación

---

# Grafos

## Operaciones

---

# Grafos

## Implementación

---

# Grafos

## Aplicaciones

---

# Conclusión

- Al igual que las estructuras lineales, las estructuras no lineales son fundamentales en la programación.
- Las estructuras no lineales son más complejas y su implementación requiere de un mayor esfuerzo, sin embargo, son necesarias para resolver problemas más complejos.
- Las estructuras no lineales son utilizadas en la vida cotidiana, por ejemplo, en la representación de redes sociales, rutas de transporte, etc.

---

<!-- _class: inverted centered -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

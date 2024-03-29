---
marp: true
title: EDD - 03 - Estructuras Lineales
author: Jaime Jesús Delgado Meraz
header: Estructuras de Datos - U3
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

# Unidad 3 <br> Estructuras Lineales

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
3. [Listas](#listas)
4. [Pilas](#pilas)
5. [Colas](#colas)

---
<!-- _class: lead -->
# Introducción

---

# Introducción

- Como se ha mencionado en las unidades anteriores, las estructuras de datos son una parte fundamental en el desarrollo de software.
- Se utilizan para almacenar y organizar datos de manera eficiente, permitiendo resolver problemas complejos de manera sencilla.
- En esta unidad se estudiarán las estructuras de datos lineales, las cuales son aquellas que permiten almacenar y acceder a los datos de manera secuencial.
- Se revisarán sus características, operaciones y aplicaciones.

---
<!-- _class: lead -->
# Nodo

---

# Nodo

> Un nodo es una estructura de datos que contiene un valor y una referencia a uno o más nodos.

- Se puede considerar como una caja que contiene un valor y un puntero a otro nodo.
- Los nodos se utilizan para construir estructuras de datos más complejas, como listas, pilas y colas.
- Son una estructura de datos fundamental en la programación.

---

# Nodo

- En la programación, un nodo se puede representar como una estructura o una clase.

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo1.siguiente = nodo2
```

![bg right w:95%](../src/assets/EDD/nodos.png)

---

# Nodo

- La estructura de un nodo es muy simple, pero es la base para construir estructuras de datos más complejas.
- Puede contener cualquier tipo de dato, como enteros, flotantes, cadenas, objetos, etc.

::: info
👨🏻‍🏫 Aunque la mayoría de los lenguajes modernos no requieren la creación de la estructura `nodo`, se desarrollará para tomar como base de las estructuras de datos lineales
:::

---
<!-- _class: lead -->
# Listas

---

# Listas

> Una lista es una estructura de datos que almacena una colección de elementos, en la que cada elemento tiene un sucesor y un predecesor.

- Las listas son una de las estructuras de datos más utilizadas en programación, ya que permiten almacenar y acceder a los datos de manera secuencial.
- La mayoría de los lenguajes de programación modernos incluyen una implementación de listas, ya sea como una alternativa a los arreglos o la estructura de datos principal para almacenar datos.

---

# Listas

## Representación en memoria

- Las listas se pueden representar en memoria como una secuencia de nodos enlazados.
- Cada nodo contiene un valor y una referencia al siguiente nodo.
- El primer nodo se conoce como **cabeza** o **inicio** de la lista.
- El último nodo se conoce como **cola** o **fin** de la lista.

![bg right w:85%](../src/assets/EDD/listas-nodos.png)

---

# Listas

## Representación en memoria

- Los nodos no necesariamente se encuentran en posiciones contiguas en memoria, pero se pueden representar de manera secuencial.
- La referencia al siguiente nodo se almacena en el nodo actual, lo que permite recorrer la lista de manera secuencial.

![bg right w:95%](../src/assets/EDD/listas-secuencial.png)

---

# Listas

## Representación en memoria

- En general, las listas se pueden representar en memoria como una secuencia de nodos enlazados, donde cada nodo contiene un valor y una referencia al siguiente nodo.

:::: flex
::: col 1/2

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
```

:::
::: col 1/2

```python
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
```

:::
::::

- En la práctica, es preferible construir una clase que represente la lista y que contenga los métodos necesarios para manipularla.

---

# Listas

## Operaciones

- Las listas permiten realizar operaciones como:
  - Inserción
  - Eliminación
  - Recorrido (o impresión)
  - Búsqueda
  - Ordenamiento

::: info
👨🏻‍🏫 Las operaciones de búsqueda y ordenamiento se revisarán con más detalle en unidades posteriores
:::

---

# Listas

## Tipos de listas

- Las listas pueden clasificarse según sus características y operaciones.
- Las listas más comunes son:
  - Listas simplemente enlazadas
  - Listas doblemente enlazadas
  - Listas circulares
- La diferencia entre estos tipos de listas radica en la forma en que los **nodos** se enlazan entre sí.

---

# Listas

## Listas simplemente enlazadas

> Son listas en las que cada nodo contiene un valor y una referencia al siguiente nodo.

- La referencia al siguiente nodo se almacena en el nodo actual, por su parte, el último nodo de la lista contiene una referencia nula.
- Las listas simplemente enlazadas son las más sencillas y se utilizan en la mayoría de las aplicaciones.
- Python ya cuenta con su propia implementación de listas, sin embargo, se desarrollará una implementación propia para comprender su funcionamiento.

---

# Listas

## Listas simplemente enlazadas: Inserción

```python
class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def agregar(self, valor):
        nuevo = Nodo(valor) # Crear un nuevo nodo apuntando a None

        if self.cola is None: # Si la lista está vacía
            self.cabeza = nuevo
            self.cola = nuevo
        else: # Si la lista no está vacía
            self.cola.siguiente = nuevo
        
        self.tamanio += 1 # Incrementar el tamaño de la lista
        self.cola = nuevo # Actualizar el último nodo
```

---

# Listas

## Listas simplemente enlazadas

```python
lista = ListaSimple()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

# 10 -> 20 -> 30 -> None
```

---

# Listas

## Listas simplemente enlazadas: Eliminar

```python
class ListaSimple:
    # ...
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False
```

---

# Listas

## Listas simplemente enlazadas

```python
lista = ListaSimple()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

# 10 -> 20 -> 30 -> None

lista.eliminar(20)

# 10 -> 30 -> None
```

- La eliminación de un nodo en una lista simplemente enlazada requiere recorrer la lista para encontrar el nodo a eliminar y actualizar las referencias.

---

# Listas

## Listas simplemente enlazadas: Recorrido y búsqueda simple

```python
class ListaSimple:
    # ...
    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
```

---

# Listas

## Listas simplemente enlazadas

:::: flex
::: col 1/2 px-2

```python
lista = ListaSimple()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

# 10 -> 20 -> 30 -> None

lista.recorrer()
# 10
# 20
# 30

print(lista.buscar(20)) # True
print(lista.buscar(40)) # False
```

:::
::: col 1/2 px-2

- En la práctica, también se puede recorrer la lista utilizando un ciclo.

```python
actual = lista.cabeza

while actual:
    print(actual.valor)
    actual = actual.siguiente
```

:::
::::

---

# Listas

## Listas simplemente enlazadas

- Al trabajar con listas simplemente enlazadas (o simplemente listas), también se pueden agregar operaciones como:
  - Obtener el tamaño de la lista
  - Obtener el primer y último nodo
  - Obtener el valor de un nodo en una posición específica
  - Obtener el nodo en una posición específica
- Estas operaciones se pueden implementar de manera similar a las operaciones de inserción, eliminación, recorrido y consulta, por lo que no se revisarán con detalle.

---

# Listas

## Listas doblemente enlazadas

> Son listas en las que cada nodo contiene un valor, una referencia al siguiente nodo y una referencia al nodo anterior.

- A diferencia de las listas simplemente enlazadas,las listas doblemente enlazadas permiten recorrer la lista en ambas direcciones, lo que facilita la implementación de algunas operaciones.
- La implementación de listas doblemente enlazadas es más compleja que la de listas simplemente enlazadas, ya que se deben actualizar las referencias en ambos sentidos.

---

# Listas

## Listas doblemente enlazadas

- La implementación de listas doblemente enlazadas es similar a la de listas simplemente enlazadas, pero se deben una estructura de nodo "mejorada" que contenga una referencia al nodo siguiente y al nodo anterior.

```python
class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
```

---

# Listas

## Listas doblemente enlazadas

- Al trabajar con listas doblemente enlazadas, además de las operaciones que ya se pueden realizar con las listas simples, se pueden agregar operaciones como:
  - Inserción al inicio (la lista simplemente enlazada solo permite la inserción al final)
  - Eliminación al inicio o al final
  - Recorrido en ambas direcciones

---

# Listas

## Listas doblemente enlazadas: Inserción

:::: flex
::: col 1/2

```python
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def agregar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1
```

:::

::: col 1/2 px-2

```python
    def agregar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.cola is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1

    def agregar(self, valor):
        self.agregar_final(valor)
```

:::
::::

---

# Listas

## Listas doblemente enlazadas

```python
lista = ListaDoble()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

# 10 -> 20 -> 30 -> None

lista.agregar_inicio(5)

# 5 -> 10 -> 20 -> 30 -> None

lista.agregar_final(40)

# 5 -> 10 -> 20 -> 30 -> 40 -> None
```

---
<!-- _class: lead -->
# Pilas

---

# Pilas

---
<!-- _class: lead -->
# Colas

---

# Colas

---

<!-- _class: inverted -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

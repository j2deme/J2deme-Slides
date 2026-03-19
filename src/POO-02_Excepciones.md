---
marp: true
title: Programación Orientada a Objetos - 02 - Clases y Objetos - Manejo de excepciones
author: Jaime Jesús Delgado Meraz
header: Programación Orientada a Objetos - U2 - Manejo de excepciones
footer: "[&bull;](#contenidos) **DR. JJDM**"
paginate: true
theme: j2deme
math: mathjax
style: |
  :root {
    --primary: #1274c5;
  }
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Clases y Objetos

## **Manejo de excepciones**

## Programación Orientada a Objetos

Dr. Jaime Jesús Delgado Meraz

### Unidad 02

#### AED - 1286

#### IAD - 2424

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

<!-- _class: toc -->

# Contenidos

1. [Excepciones](#excepciones)
2. [Tipos de Excepciones](#tipos-de-excepciones)
3. [Propagación de Excepciones](#propagación-de-excepciones)
4. [Gestión de Excepciones](#gestión-de-excepciones)
5. [Excepciones Personalizadas](#excepciones-personalizadas)

---

<!-- _class: lead -->

# Excepciones

---

# Excepciones

> Una excepción es un evento que ocurre durante la ejecución de un programa, que interrumpe el flujo normal de las instrucciones.

- Las excepciones se utilizan para indicar que algo inusual ha ocurrido.
- Las excepciones se suelen manejar usando los bloques **try** y **catch** (**except**).
- Una excepción se puede lanzar, ya sea automáticamente por el sistema o manualmente por el programador.

---

# Excepciones

## Try-Catch

::: primary
El bloque **try** se utiliza para probar un bloque de código en busca de errores, por su parte, el bloque **catch / except** se utiliza para manejar los errores.
:::

<div class="flex">
  <div class="w-1/2">

```java
try {
  // Bloque de código a probar
} catch (Exception e) {
  // Bloque de código para manejar la excepción
}
```

  </div>
  <div class="w-1/2">

```python
try:
  # Bloque de código a probar
except Exception as e:
  # Bloque de código para manejar la excepción
```

  </div>
</div>

---

# Excepciones

## Excepciones != Errores

Es importante entender la diferencia entre errores y excepciones.

Error
~ Es un problema que ocurre durante la compilación de un programa.

```java
int x = 10 / 0; // Error aritmético
```

Excepción
~ Es un problema que ocurre durante la ejecución de un programa.

```java
int nums[] = {1, 2, 3};
System.out.println(nums[5]); // Excepción
```

---

# Excepciones

## ¿Cómo detectar excepciones y manejarlas?

- Para desarrolladores novatos, es difícil detectar excepciones y manejarlas, sin embargo, con la práctica se vuelve más fácil.
- Los siguientes puntos pueden ayudar a detectar excepciones:
  - Leer la documentación de los métodos.
  - Leer los mensajes de error durante el desarrollo.
  - Leer los mensajes de error durante la ejecución.

::: success
La mejor forma de aprender a manejar excepciones es practicando 😉.
:::

---

<!-- _class: lead -->

# Tipos de excepciones

---

# Tipos de excepciones

En general, las excepciones se pueden dividir en dos tipos:

Checked Exceptions
~ Son aquellas que el compilador obliga a manejar y heredan de la clase `Exception` o `RuntimeException`.

Unchecked Exceptions
~ Son aquellas que el compilador no obliga a manejar y heredan de la clase `Error`.

---

# Tipos de excepciones

## Checked exceptions

<div class="flex">
  <div class="w-1/2">

Las excepciones que heredan de la clase `Exception` o `RuntimeException` son llamadas `checked exceptions`.

- Este tipo de excepciones son aquellas que el compilador obliga a manejar, es decir, el compilador nos obliga a usar un bloque **try** y **catch** para manejarlas.
- Si no se manejan, el compilador no nos permitirá compilar el programa.

  </div>
  <div class="w-1/2">

### Ejemplos de checked exceptions

- Excepciones de entrada/salida (IO)
- Excepciones de SQL
- Excepciones de Clases (ClassNotFound)
- Excepciones de manejo de archivos (FileNotFound)
- Excepciones de tiempo de ejecución (Runtime)

  </div>

</div>

---

# Tipos de excepciones

## Unchecked exceptions

<div class="flex">
  <div class="w-1/2">

Las excepciones que heredan de la clase **Error** son llamadas **unchecked exceptions**.

- Este tipo de excepciones son aquellas que el compilador no obliga a manejar, es decir, requiere usar un bloque **try-catch**.
- Sin embargo, es recomendable manejarlas para evitar que el programa termine de forma inesperada.

  </div>
  <div class="w-1/2">

### Ejemplos de unchecked exceptions

- Excepciones Aritméticas (_P.e._ dividir entre cero)
- Excepciones de índice de arreglo (_P.e._ acceder a un índice inválido)
- Excepciones de puntero nulo (_P.e._ acceder a un objeto no inicializado)
- Excepciones de conversión de tipos (_P.e._ convertir una cadena a entero)

  </div>

</div>

---

# Tipos de excepciones

## Excepciones más comunes

- **ArithmeticException**: Se lanza cuando ocurre una excepción aritmética, por ejemplo, cuando se intenta dividir entre cero.
- **ArrayIndexOutOfBoundsException**: Se lanza cuando se intenta acceder a un índice inválido de un arreglo.
- **NullPointerException**: Se lanza cuando se intenta acceder a un objeto que no ha sido inicializado.
- **FileNotFoundException**: Se lanza cuando se intenta acceder a un archivo que no existe.
- **IOException**: Se lanza cuando ocurre una excepción de entrada/salida.

---

<!-- _class: inverted -->

# Tipos de excepciones

## Notas sobre excepciones

Cada lenguaje de programación tiene su propia forma de manejar las excepciones, así también la nomenclatura de las excepciones puede variar de un lenguaje a otro.

- En Java las excepciones más comunes son **ArithmeticException**, **ArrayIndexOutOfBoundsException**, **NullPointerException** y **FileNotFoundException**.
- Mientras que en Python esas mismas excepciones son **ZeroDivisionError**, **IndexError**, **TypeError** y **FileNotFoundError**.

Se recomienda leer la documentación de cada lenguaje para conocer las excepciones que maneja.

---

<!-- _class: lead -->

# Propagación de excepciones

---

# Propagación de excepciones 🏓

> Propagar una excepción significa lanzar una excepción de un método a otro.

- Se sugiere que los métodos que puedan lanzar una excepción, lo indiquen en su firma.
- Sin embargo, si un método lanza una excepción y no la maneja, entonces debe indicarlo en su firma.
  - Esto se hace usando la palabra reservada **throws**.
  - En lenguajes como Python, JavaScript, PHP, Ruby y Kotlin no es necesario indicarlo en la firma.

---

# Propagación de excepciones 🏓

- La propagación de excepciones se utiliza para propagar una excepción de un método a otro, es decir, que si un método lanza una excepción, entonces el método que lo invoca debe manejarla o propagarla.
- En caso de que ningún método la maneje, entonces el programa terminará de forma inesperada.

::: info
La propagación de excepciones también se conoce como _burbujeo de excepciones_ 🫧
:::

---

# Propagación de excepciones

# Ejemplo (Java)

```java
public class Main {
  public static void main(String[] args) {
    // La excepción es propagada al método main
    // y se maneja en el bloque try-catch
    try {
      int x = divide(10, 0);
      System.out.println(x);
    } catch (ArithmeticException e) {
      System.out.println("No se puede dividir entre cero");
    }
  }

  public static int divide(int a, int b) throws ArithmeticException {
    // El método no maneja la excepción
    return a / b;
  }
}
```

---

# Propagación de excepciones

## Ejemplo (Python)

```python
def divide(a, b):
  # El método no maneja la excepción
  return a / b

if __name__ == '__main__':
  # La excepción es propagada al método main
  # y se maneja en el bloque try-except
  try:
    x = divide(10, 0)
    print(x)
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
```

---

# Propagación de excepciones

## ¿Cómo prevenir la propagación de excepciones?

- Para prevenir la propagación de excepciones, se debe manejar la excepción en el mismo método que la lanza.
- Esto se hace usando un bloque **try-catch**.
- De esta forma, el método que invoca no tendrá que manejar la excepción.

::: danger
Si no se maneja la excepción, entonces el programa terminará de forma inesperada.
:::

---

<!-- _class: lead -->

# Gestión de excepciones

---

# Gestión de excepciones

- La gestión de excepciones se refiere a cómo se manejan las excepciones, es decir, cómo se controla el flujo del programa cuando ocurre una excepción.
- La correcta gestión de excepciones es importante para evitar que el programa termine de forma inesperada.
- En Java, las excepciones se manejan usando bloques **try-catch**.
- En Python, las excepciones se manejan usando bloques **try-except**.

::: info
La gestión de excepciones también se conoce como _manejo de excepciones_ 🤹.
:::

---

# Gestión de excepciones

## Bloques Try-Catch / Try-Except

- El bloque **try-catch** o **try-except** (según el lenguaje) se utiliza para manejar excepciones o errores.
- Son el componente principal de la gestión de excepciones.
- El bloque **try** se utiliza para ejecutar el código que puede lanzar una excepción.
- El bloque **catch** o **except** se utiliza para manejar la excepción lanzada por el bloque **try**.

---

# Gestión de excepciones

## Implementación (Java)

Supongamos que queremos dividir dos números, pero no sabemos si el divisor será cero.

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    try {
      int x = divide(10, 0);
      System.out.println(x);
    } catch (ArithmeticException e) {
      System.out.println("No se puede dividir entre cero");
    }
  }

  public static int divide(int a, int b)
    throws ArithmeticException {
    return a / b;
  }
}
```

  </div>
  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    // El método maneja su propia excepción
    int x = divide(10, 0);
    System.out.println(x);
  }

  public static int divide(int a, int b) {
    try {
      return a / b;
    } catch (ArithmeticException e) {
      System.out.println("No se puede dividir entre cero");
    }
  }
}
```

  </div>
</div>

---

# Gestión de excepciones

## Implementación (Python)

Supongamos que queremos dividir dos números, pero no sabemos si el divisor será cero.

<div class="flex flex-wrap">

  <div class="w-1/2">

```python
def divide(a, b):
  return a / b

if __name__ == '__main__':
  try:
    x = divide(10, 0)
    print(x)
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
```

  </div>
  <div class="w-1/2">

```python
def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    print('No se puede dividir entre cero')

if __name__ == '__main__':
  x = divide(10, 0)
  print(x)
```

  </div>
</div>

::: success
En adelante entenderemos que el bloque **try-catch** o **try-except** se refiere a ambos.
:::

---

# Gestión de excepciones

## Estructura del bloque Try-Catch

![bg right:40%](https://media.istockphoto.com/id/172765853/photo/baseball-equipment.jpg?s=612x612&w=0&k=20&c=bW-nYGd3D9xSuT-QeA7QgfPhEv0xW8giEYLlwTuI8qE= "baseball ball and mitt on grass")

- El bloque **try-catch** se compone de dos partes básicas:
  - El bloque **try**.
  - El bloque **catch**.
- Un bloque **try-catch** puede tener varias partes opcionales:
  - Bloques **catch** adicionales.
  - El bloque **finally**, este bloque se ejecuta siempre, independientemente de si se lanza una excepción o no.

---

# Gestión de excepciones

## Bloques catch adicionales

- Un bloque **try-catch** puede tener varios bloques **catch**.
- Cada bloque **catch** maneja un tipo de excepción diferente.
- Los bloques **catch** se evalúan en orden, de arriba hacia abajo, y el primer **catch** que coincida con el tipo de excepción lanzada, manejará la excepción.
- Si no hay ningún bloque **catch** que coincida con el tipo de excepción lanzada, entonces la excepción se propagará al método que invoca.

::: info
Antes de poner un bloque **catch** para manejar una excepción, es importante saber qué tipo de excepción se lanzará.
:::

---

# Gestión de excepciones

## Uso de bloques catch adicionales

- Un bloque **try-catch** puede tener varios bloques **catch**.

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    try {
      int x = divide(10, 0);
      System.out.println(x);
    } catch (ArithmeticException e) {
      System.out.println("No se puede dividir entre cero");
    } catch (Exception e) {
      System.out.println("Ocurrió un error");
    }
  }

  public static int divide(int a, int b)
    throws ArithmeticException {
    return a / b;
  }
}
```

  </div>
  <div class="w-1/2">

```python
def divide(a, b):
  return a / b

if __name__ == '__main__':
  try:
    x = divide(10, 0)
    print(x)
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
  except Exception:
    print('Ocurrió un error')
```

  </div>
</div>

---

# Gestión de excepciones

## Bloque Finally

El bloque **finally** se utiliza para ejecutar código que debe ejecutarse **siempre**, independientemente de si se lanza una excepción o no, este bloque es opcional.

- _P.e._ Se podría usar el bloque **finally** para cerrar un archivo o una conexión de base de datos.

El bloque **finally** puede ejecutarse después de alguna de las siguientes situaciones:

1. El bloque **try** se ejecuta y no se lanza ninguna excepción.
2. El bloque **try** se ejecuta y se lanza una excepción, y hay un bloque **catch** que coincide con el tipo de excepción lanzada.
3. El bloque **try** se ejecuta y se lanza una excepción, y no hay un bloque **catch** que coincida con el tipo de excepción lanzada.

---

# Gestión de excepciones

## Uso del bloque Finally

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    try {
      int x = divide(10, 0);
      System.out.println(x);
    } catch (ArithmeticException e) {
      System.out.println("No se puede dividir entre cero");
    } finally {
      System.out.println("Fin del programa");
    }
  }

  public static int divide(int a, int b)
    throws ArithmeticException {
    return a / b;
  }
}
```

  </div>
  <div class="w-1/2">

```python
def divide(a, b):
  return a / b

if __name__ == '__main__':
  try:
    x = divide(10, 0)
    print(x)
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
  finally:
    print('Fin del programa')
```

  </div>
</div>

---

# Gestión de excepciones

## Lanzamiento de Excepciones

- Las operaciones y métodos pueden lanzar excepciones cuando se produce un error.
- Ademas de las excepciones que se lanzan automáticamente, también podemos lanzar nuestras propias excepciones.
- Para lanzar una excepción en Java, usamos la palabra clave **throw**, mientras que en Python se utiliza la palabra clave **raise**.
- Para ambos casos, estas palabras clave se utilizan seguidas de una instancia de la clase **Exception**.

---

# Gestión de excepciones

## Lanzamiento de excepciones

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    try {
      int x = divide(10, 0);
      System.out.println(x);
    } catch (ArithmeticException e) {
      System.out.println("No se puede dividir entre cero");
    }
  }

  public static int divide(int a, int b)
    throws ArithmeticException {
    if (b == 0) {
      throw new ArithmeticException();
    }
    return a / b;
  }
}
```

  </div>
  <div class="w-1/2">

```python
def divide(a, b):
  if b == 0:
    raise Exception("El divisor no puede ser cero")
  return a / b

if __name__ == '__main__':
  try:
    x = divide(10, 0)
    print(x)
  except ZeroDivisionError:
    print('No se puede dividir entre cero')
```

  </div>
</div>

::: warning
En Java, no se debe confundir la palabra clave **throw** con el método **throws**.
:::

---

<!-- _class: lead -->

# Excepciones personalizadas

---

# Excepciones personalizadas

- Además de las excepciones existentes en cada lenguaje, también podemos crear nuestras propias excepciones.
- Las excepciones personalizadas se utilizan para manejar situaciones específicas en las que se produce un error.
- Estas excepciones deben extender la clase **Exception** y se pueden lanzar de la misma manera que las excepciones existentes.
- A estas excepciones personalizadas también se les conoce como _excepciones de usuario_

---

# Excepciones personalizadas

## Propósito

- El propósito de crear excepciones personalizadas es poder manejar situaciones específicas en las que se produce un error. _P.e._
  - Si se está desarrollando una aplicación de un banco, se podría crear una excepción personalizada para cuando un usuario intente retirar más dinero del que tiene en su cuenta (`NotEnoughMoneyException`).
  - En el caso de una aplicación de un restaurante, se podría crear una excepción personalizada para cuando un usuario intente pedir un platillo que no existe en el menú (`DishNotFoundException`).

::: info
Se puede decir que las excepciones personalizadas se utilizan para manejar las excepciones de la **lógica de negocio** de una aplicación.
:::

---

# Excepciones personalizadas

## Creación de excepciones personalizadas

Para crear una excepción personalizada, se debe crear una clase que extienda la clase **Exception**.

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class MyException extends Exception {
  public MyException(String message) {
    super(message);
  }
}
```

  </div>
  <div class="w-1/2">

```python
class MyException(Exception):
  def __init__(self, message):
    super().__init__(message)
```

  </div>
</div>

En ambos casos, se debe sobrescribir el constructor de la clase **Exception** y llamar al constructor de la clase padre con el mensaje de error.

---

# Excepciones personalizadas

## Creación de excepciones personalizadas

```python
# excepciones.py
class ValidationError(Exception):
    """Excepción base para errores de validación."""
    pass

class InvalidNameError(ValidationError):
    """Excepción lanzada cuando el nombre no es válido."""
    pass

class InvalidEmailError(ValidationError):
    """Excepción lanzada cuando el email no es válido."""
    pass

class InvalidAgeError(ValidationError):
    """Excepción lanzada cuando la edad no es válida."""
    pass

class DuplicateEmailError(Exception):
    """Excepción lanzada cuando el email ya está registrado."""
    pass
```

---

# Excepciones personalizadas

## Lanzamiento de excepciones personalizadas

Para lanzar una excepción personalizada, se debe crear una instancia de la excepción y lanzarla usando la palabra clave **throw** en Java o **raise** en Python.

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    try {
      throw new MyException("Ocurrió un error");
    } catch (MyException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

  </div>
  <div class="w-1/2">

```python
if __name__ == '__main__':
  try:
    raise MyException("Ocurrió un error")
  except MyException as e:
    print(e)
```

  </div>
</div>

```shell
Ocurrió un error
```

---

# Excepciones personalizadas

## Lanzamiento de excepciones personalizadas

```python
from .excepciones import InvalidNameError, InvalidEmailError, InvalidAgeError, DuplicateEmailError

class Usuario:
    def __init__(self, nombre, email):
        self._nombre = None
        self._email = None
        self.nombre = nombre  # Usa el setter para validar
        self.email = email    # Usa el setter para validar

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor) < 2:
            raise InvalidNameError("El nombre debe tener al menos 2 caracteres y ser texto.")
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise InvalidEmailError(f"El email '{valor}' no es válido. Debe contener '@' y '.'.")
        self._email = valor
```

# Excepciones personalizadas

## Lanzamiento de excepciones personalizadas

```python
from dataclasses import dataclass
from .excepciones import InvalidNameError, InvalidAgeError # Importación asumida

@dataclass
class UsuarioData:
    nombre: str
    edad: int

    def __post_init__(self):
        if not isinstance(self.nombre, str) or len(self.nombre) < 2:
            raise InvalidNameError("El nombre debe tener al menos 2 caracteres.")
        if not isinstance(self.edad, int) or not (15 <= self.edad <= 100):
            raise InvalidAgeError("La edad debe ser un entero entre 15 y 100.")
```

---

# Excepciones personalizadas

## Excepción de lógica de negocio en Java

Supongamos una aplicación para un banco y un usuario intenta retirar más dinero del que tiene en su cuenta.

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public int SALDO = 100;
  public static void main(String[] args) {
    try {
      retirar(50);
    } catch (NotEnoughMoneyException e) {
      System.out.println(e.getMessage());
    }
  }

  public static void retirar(int cantidad)
    throws NotEnoughMoneyException {
    if (cantidad > SALDO) {
```

  </div>
  <div class="w-1/2">

```java
      throw new NotEnoughMoneyException(
        "Saldo insuficiente");
    } else {
        SALDO -= cantidad;
    }
  }
}
```

  </div>
</div>

---

# Excepciones personalizadas

## Excepción de lógica de negocio en Python

Supongamos una aplicación para un restaurante y un usuario intenta pedir un platillo que no existe en el menú.

```python
class Main:
  if __name__ == '__main__':
    try:
      pedir_platillo('🍕')
    except DishNotFoundException as e:
      print(e)

  def pedir_platillo(platillo):
    platillos = ['🍔', '🍟', '🌭', '🍗']
    if platillo not in platillos:
      raise DishNotFoundException(
        'El platillo no existe en el menú')
    else:
      print('Preparando platillo...')
```

---

# Excepciones personalizadas

## Miembros adicionales

- Las excepciones personalizadas pueden tener miembros adicionales.
- Estos miembros pueden ser de cualquier tipo de dato.
- Estos miembros pueden ser utilizados para almacenar información adicional sobre la excepción. _Por ejemplo:_
  - En una excepción de lógica de negocio para un banco, se podría almacenar el número de cuenta del usuario.
  - En otra, para un restaurante, se podría almacenar el platillo que el usuario intentó pedir.
  - Para una tienda, se podría almacenar el producto que el usuario intentó comprar.

---

# Excepciones personalizadas

## Miembros adicionales en Java

<div class="flex flex-wrap">

  <div class="w-1/2">

```java
public class Main {
  public static void main(String[] args) {
    try {
      throw new MyException("Ocurrió un error", 123);
    } catch (MyException e) {
      System.out.println(e.getMessage());
      System.out.println(e.getDatoAdicional());
    }
  }
}
```

  </div>
  <div class="w-1/2">

```java
public class MyException extends Exception {
  private int datoAdicional;

  public MyException(String message, int datoAdicional) {
    super(message);
    this.datoAdicional = datoAdicional;
  }

  public int getDatoAdicional() {
    return datoAdicional;
  }
}
```

  </div>
</div>

---

# Excepciones personalizadas

## Miembros adicionales en Python

<div class="flex flex-wrap">

  <div class="w-1/2">

```python
class Main:
  if __name__ == '__main__':
    try:
      comprar('🍍')
    except ProductNotFoundException as e:
      print(f'{e}: {e.producto}')

  def comprar(producto):
    productos = ['🍎', '🍌', '🥦', '🍓']
    if producto not in productos:
      raise ProductNotFoundException(
        'No se encontró el producto', producto)
    else:
      print('Comprando producto...')
```

  </div>
  <div class="w-1/2">

```python
class ProductNotFoundException(Exception):
  def __init__(self, message, producto):
    super().__init__(message)
    self.producto = producto
```

```shell
No se encontró el producto: 🍍
```

  </div>
</div>

---

# Excepciones personalizadas

## Consideraciones adicionales

- Es posible crear jerarquías de excepciones personalizadas.
- Se pueden crear excepciones personalizadas que extiendan de otras excepciones personalizadas.
- Se pueden crear excepciones personalizadas que extiendan de las excepciones existentes en el lenguaje.

::: info
El uso de excepciones personalizadas depende de cada desarrollador y de cada aplicación.
:::

---

<!-- _class: inverted -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-mono text-8xl mt-10">
  &lt;/Fin&gt;
</div>

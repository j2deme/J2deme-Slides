---
marp: true
title: Playground
author: Jaime Jesús Delgado Meraz
header: Playground
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

# Unidad 99

# <!-- fit -->Nombre de la unidad

## Asignatura

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

:::: flex
::: col 1/2 px-2
Nombre
: Nombre de la asignatura

Carrera
: Carrera 1 a la que aplica
: Carrera 2 a la que aplica
:::
::: col 1/2 px-2
Clave
: ABC - 1234

SATCA
: 9 - 9 - 9
:::
::::

---

<!-- _class: toc -->

# Secciones

1. [Contenidos](#contenidos)
2. [Layouts](#layouts)
3. [Código](#código)
4. [Bloques](#bloques)

---

<!-- _class: lead -->

# Contenidos

---

# Contenidos

## Prosa

Los párrafos reciben un estilo simple con un color de fuente no totalmente negro, pero suficiente para generar contraste con el color de los encabezados y fondo.

El texto se alinea a la izquierda para permitir una lectura en el orden natural, evitando espaciado inconsistente provocado por el texto justificado.

No es necesario utilizar etiquetas o marcados especiales para el texto en prosa.

---

<!-- _class: cols-2 -->

# Contenidos

## Tipografías

::: left

La plantilla incluye un set de 4 tipografías:

1. Encabezados en tipografía **Poppins**.
2. Cuerpo de las diapositivas en tipografía **Figtree**.
3. Código en línea y código en bloque en tipografía **Iosevka**.
4. Autor de citas en tipografía **Victor Mono** en cursiva.

:::

::: right

Cada tipografia con su propio estilo:

1. <span style="font-family: var(--font-header)">Poppins</span>
2. <span style="font-family: var(--font-body)">Figtree</span>
3. <span style="font-family: var(--font-code)">Iosevka</span>
4. <span style="font-family: var(--font-caligraphic); font-style: italic;">Victor Mono Cursiva</span>

:::

---

<!-- _class: cols-2 -->

# Contenidos

## Estilos de texto

::: left

- **Negritas**
- _Itálicas_
- ~~Tachado~~
- `Código de una línea`
- [Enlace](https://www.example.com)
- <kbd>Ctrl</kbd> + <kbd>C</kbd>
- <mark>Resaltado</mark>
- Texto con nota <note>\*</note>

:::
::: right

```md
- **Negritas**
- _Italicas_
- ~~Tachado~~
- `Código de una línea`
- [Enlace](http://www.example.com)
- <kbd>Ctrl</kbd> + <kbd>C</kbd>
- <mark>Resaltado</mark>
- Texto con nota <note>\*</note>
```

Los estilos de texto se pueden combinar con los párrafos.

:::
::: note
Se sugiere que la nota sea breve.
:::

---

# Contenidos

## Párrafo con énfasis

En algunos casos se puede requerir enfatizar un párrafo de entre los demás, para esto se antepone el símbolo `>` que cambia el estilo del párrafo.

> Como este párrafo, que se observa distinto al párrafo anterior, agregando una cintilla a la izquierda y cambiando ligeramente el color de fuente.

```md
En algunos casos se puede requerir enfatizar un párrafo de entre los demás,
para esto se antepone el símbolo `>` que cambia el estilo del párrafo.

> Como este párrafo, que se observa distinto al párrafo anterior, agregando ...
````

---

# Contenidos

## Listas

Es posible utilizar diferentes tipos de listas:

- Listas de viñetas
- Listas numeradas
- Listas de definición

Cada una de las anteriores con su propio estilo y estructura.

---

# Contenidos

## Listas

### Listas de viñetas

- Las listas de viñetas son útiles para enumerar elementos sin un orden específico.
  - Se pueden anidar.
    - Aunque no es recomendable hacerlo más allá de dos niveles.

```md
- Las listas de viñetas son útiles para enumerar elementos sin un orden específico.
  - Se pueden anidar.
    - Aunque no es recomendable hacerlo más allá de dos niveles.
```

---

# Contenidos

## Listas

### Listas numeradas

1. Las listas numeradas son útiles para enumerar elementos con un orden específico.
2. Y aunque se pueden anidar, es preferible no hacerlo.
   1. Porque puede resultar confuso.

```md
1. Las listas numeradas son útiles para enumerar elementos con un orden específico.
2. Y aunque se pueden anidar, es preferible no hacerlo.
```

1. Este debería ser el 3er elememento...

::: warning
Al "romper" la lista numerada, se reinicia el contador, y no hay forma de continuar la numeración o cambiar el número de inicio, a menos que se utilice directamente HTML.
:::

---

<!-- _class: cols-2 -->

# Contenidos

## Listas

### Listas numeradas

::: left

Se pueden tener listas numeradas anidadas.

- A partir del 2o nivel, se requiere indentar con doble tabulacion.
- Por default el 1er nivel se estiliza con arábigos, el 2o con romanos en minúsculas y el 3o con letras minúsculas.

:::
::: right

```md
1. Elemento 1
   1. Sub elemento 1
      1. Sub sub elemento 1
   2. Sub elemento 2
2. Elemento 3
```

1. Elemento 1
   1. Sub elemento 1
      1. Sub sub elemento 1
   2. Sub elemento 2
2. Elemento 3

:::

---

<!-- _class: cols-2 -->

# Contenidos

## Listas

### Listas numeradas

::: left
Si se requiere, se puede cambiar el tipo de numeración y el número de inicio de las listas numeradas utilizando HTML.

```html
<ol type="A">
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ol>
```

```html
<ol start="3">
  <li>Elemento 3</li>
  <li>Elemento 4</li>
</ol>
```

:::
::: right

Ejemplo con `type="A"`:

<ol type="A">
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ol>

Ejemplo con `start="3"`:

<ol start="3">
  <li>Elemento 3</li>
  <li>Elemento 4</li>
</ol>

:::

::: warning
Se sugiere limitar su uso a casos específicos.
:::

---

<!-- _class: cols-2 -->

# Contenidos

## Listas

### Listas de definición

::: left

Estas listas son útiles para definir términos o conceptos.

```md
Término 1
: Definición

**Término 2**
: Es posible utilizar negritas para resaltar un término.
: Además de una definición con múltiples párrafos.

Término 3
: Definición
```

:::
::: right

Término 1
: Definición

**Término 2**
: Es posible utilizar negritas para resaltar un término.
: Además de una definición con múltiples párrafos.

Término 3
: Definición

:::

::: warning
Debido a su estructura y estilo, no es recomendable anidar listas de definición.
:::

---

# Contenidos

## Citas

Las citas se utilizan para resaltar un texto que no es propio, y se pueden presentar de dos formas:

1. Citas en línea
2. Citas en foco

La diferencia principal radica en la estructura que se requiere para cada una.

---

# Contenidos

## Citas

### Citas en línea

Se utilizan para resaltar una cita dentro de un párrafo y deben llevar un autor al final.

> _En igualdad de condiciones, la solución más simple suele ser la más probable_
> <cite>William of Ockham</cite>

```md
> _En igualdad de condiciones, la solución más simple suele ser la más probable_
> <cite>William of Ockham</cite>
```

Si no se agrega la etiqueta `<cite>`, el párrafo se estiliza como un párrafo resaltado.

---

# Contenidos

## Citas

### Citas en línea

Es posible utilizar citas en línea con una estructura ligeramente diferente, pero que produce el mismo resultado.

::: quote
_En igualdad de condiciones, la solución más simple suele ser la más probable_
<cite>William of Ockham</cite>
:::

```md
::: quote
_En igualdad de condiciones, la solución más simple suele ser la más probable_
<cite>William of Ockham</cite>
:::
```

- Esta estructura permite resaltar la cita de forma más notoria.

---

# Contenidos

## Citas

### Citas en línea

Ambos estilos ofrecen la misma funcionalidad, pero con una presentación ligeramente diferente, por lo que se puede elegir el que mejor se adapte al contenido.

::::: flex
:::: col 1/2 px-2

> _En igualdad de condiciones, la solución más simple suele ser la más probable_
> <cite>William of Ockham</cite>

::::
:::: col 1/2 px-2

::: quote
_En igualdad de condiciones, la solución más simple suele ser la más probable_
<cite>William of Ockham</cite>
:::

::::
:::::

---

# Contenidos

## Citas

### Citas en foco

Las citas en foco se utilizan para resaltar una cita en una diapositiva independiente, para ello, se requiere que la diapositiva incluya únicamente la cita y el autor.

```md
> _En igualdad de condiciones, la solución más simple suele ser la más probable_
> <cite>William of Ockham</cite>
```

Adicionalmente, deberá incluirse una directiva `_class` con las clases `primary` y `centered` para centrar la cita en la diapositiva.

Puede incluirse una imagen junto a la cita para darle un contexto visual, se sugiere una proporción de 70/30.

---

<!-- _class: primary centered -->

> _En igualdad de condiciones, la solución más simple suele ser la más probable_
> <cite>William of Ockham</cite>

![bg right:30% w:50%](../src/assets/avatar.png)

---

# Contenidos

## Tablas

Las tablas se pueden crear de forma sencilla utilizando Markdown, y tienen un estilo simple y limpio.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

Aunque es posible cambiar la alineación de las columnas, los encabezados siempre se alinean al centro.

Dado que las tablas se adaptan al ancho del contenido, es recomendable no utilizar tablas con muchas columnas o con contenido extenso.

---

# Contenidos

## Imágenes

Para incluir imágenes en línea se utiliza:

:::: flex
::: col 2/3 px-2

```md
![alt](ruta/a/la/imagen.png)
```

Se sugiere utilizarlas a modo de fondo con la directiva `bg` para evitar que el contenido se vea afectado por la imagen.

```md
![bg](ruta/a/la/imagen.png)
```

![bg right:40% cover](../src/assets/pattern-alt.svg)

Las propiedades `right` y `left` ajustan la posición de la imagen; `fit`, `cover`, `w` y `h` ajustan el tamaño.

---
<!-- _class: lead -->

# Layouts

---

# Layouts

En general, los _layouts_ pueden ser tan simples o complejos como se requiera, y se pueden combinar con otros elementos para crear diapositivas más dinámicas.

Sin embargo, se sugiere que los _layouts_ sean sencillos y limpios para mantener la atención en el contenido.

Se puede variar la cantidad de encabezados, columnas y la alineación general de los elementos.

---

# Encabezado 1

La alineación general es desde la parte superior izquierda de la diapositiva, con un encabezado principal, en el color primario del tema.

Pueden incluirse listas, citas, tablas, imágenes y otros elementos.

Así también puede incluir una imagen a la izquierda o derecha del contenido, recordando que la diapositiva ajusta el contenido al ancho restante.

![bg left:40%](../src/assets/pattern-alt.svg)

---

# Encabezado 1

## Encabezado 2

Las diapositivas pueden incluir un encabezado secundario, que se muestra en un tamaño de fuente ligeramente menor y en color obscuro.

Igualmente, se pueden incluir listas, citas, tablas, imágenes y otros elementos.

![bg right:40%](../src/assets/pattern-alt.svg)

---

# Encabezado 1

## Encabezado 2

### Encabezado 3

Las diapositivas pueden incluir un encabezado terciario, que se muestra en un tamaño de fuente aún menor, pero en color primario, alineado a la derecha.

Este encabezado se utiliza para resaltar un punto importante o una sección específica.

Debido a que se alinea a la par del encabezado secundario, se sugiere que ambos encabezados sean breves.

---

# Encabezado 1

## Encabezado 2

### Encabezado 3

Si se requiere, se pueden incluir más encabezados, aunque se sugiere no hacerlo más allá de tres niveles.

#### Encabezado 4

##### Encabezado 5

###### Encabezado 6

Los encabezados de nivel 4 - 6 alternan entre el color secundario y el primario, reduciendo su tamaño de fuente progresivamente.

Pueden ser útiles para resaltar puntos específicos, aunque se sugiere no abusar de ellos.

---

# Layouts

## Columnas

### Flex

Es posible utilizar una cantidad arbitraria de columnas mediante una sintaxis específica que permite dividir la diapositiva en dos o más columnas.

Para ello, se utiliza un contenedor personalizado de tipo `flex`.

```md
:::: flex

<!-- Definición de columnas -->

::::
```

::: warning
El bloque superior siempre debe tener un número mayor de dos puntos `:` que el bloque inferior.
:::

---

# Layouts

## Columnas

### Distribución

Las columnas se declaran dentro del bloque `flex` y se definen con la directiva `col` seguida de la proporción que ocupará la columna.

```md
:::: flex
::: col 1/2
Contenido de la columna 1
:::
::: col 1/2
Contenido de la columna 2
:::
::::
```

Donde la proporción puede variar entre `1/2`, `1/3`, `2/3`, e incluso `1/4`, `3/4`, aunque se sugiere **no** utilizar más de tres columnas.

---

# Layouts

## Columnas

### Espaciado

Se puede agregar un espaciado a las columnas con la directiva `px` seguida de un número que indica el tamaño del espaciado.

```md
::: col 1/2 px-2
```

Este espaciado es especialmente útil para separar el contenido de las columnas y evitar que se vea saturado.

Se sugiere utilizar un espaciado de `2` o `3` para mantener una separación adecuada, por defecto el espaciado es `0`.

---

# Layouts

## Columnas

Las columnas puede incluir encabezados, listas, citas, tablas, imágenes y otros elementos, sin mayor restricción que la proporción de la columna.

Sin embargo cuando se requieren bloques particulares, se debe tener en mente la cantidad de "dos puntos" que se utilizan para definir los bloques.

Se sugiere evitar anidar bloques, ya que puede resultar en una estructura confusa y difícil de mantener.

---

# Layouts

Un estilo alternativo para aplicar _layouts_ personalizados a las diapositivas es mediante el uso de clases de _scope_ local, mediante la directiva `<!-- _class: layout -->`, donde `layout` puede ser:

- `cols-2` para un diseño a 2 columnas, se combina con los contenedores `left` y `right`.
- `cols-3` para un diseño a 3 columnas, se combina con los contenedores `left`, `center` y `right`.
- `rows-2` para un diseño a 2 filas, se combina con los contenedores `top` y `bottom`.
<!-- - `row` para un diseño de una sola fila, se combina con los contenedores `left`, `center` y `right`. -->

---
<!-- _class: cols-2 display-->
# Layouts

## Diseño a 2 columnas

::: left
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: right
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

---

<!-- _class: cols-2 debug-->

# Layouts

## Diseño a 2 columnas

### Imagen a la izquierda

::: left
![placeholder](https://unsplash.it/400/400)
:::

::: right
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

---

<!-- _class: cols-2 debug-->

# Layouts

## Diseño a 2 columnas

### Imagen a la derecha

::: left
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: right
![placeholder](https://unsplash.it/400/400)
:::

---

<!-- _class: cols-3 debug-->

# Layouts

## Diseño a 3 columnas

::: left
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: center
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: right
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

---

<!-- _class: cols-3 debug-->

# Layouts

## Diseño a 3 columnas

### Imagen a la izquierda

::: left
![placeholder](https://unsplash.it/400/400)
:::

::: center
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: right
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

---

<!-- _class: cols-3 debug-->

# Layouts

## Diseño a 3 columnas

### Imagen al centro

::: left
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: center
![placeholder](https://unsplash.it/400/400)
:::

::: right
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

---

<!-- _class: cols-3 debug-->

# Layouts

## Diseño a 3 columnas

### Imagen a la derecha

::: left
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: center
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::

::: right
![placeholder](https://unsplash.it/400/400)
:::

---

<!-- _class: rows-2 debug-->

# Layouts

## Diseño a 2 filas

::: top
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.

- Si se incluyen imágenes en alguna de las filas, estas se distribuirán de forma automática desde el centro de la fila

:::

::: bottom
![placeholder](https://unsplash.it/200)
![placeholder](https://unsplash.it/200)
![placeholder](https://unsplash.it/200)
![placeholder](https://unsplash.it/200)
![placeholder](https://unsplash.it/200)
:::

---

# Layouts

## Temas

El diseño general utiliza un fondo claro con un color de fuente oscuro para generar contraste y facilitar la lectura, pero igualmente se incluyen temas alternativos para adaptarse a diferentes estilos.

:::: flex
::: col 1/3 px-2

<div class="w-full bg-primary text-center rounded py-8">

`primary`

</div>
:::
::: col 1/3 px-2
<div class="w-full bg-secondary text-center rounded py-8">

`secondary`

</div>
:::
::: col 1/3 px-2
<div class="w-full bg-inverted text-center rounded py-8">

`inverted`

</div>
:::
::::

Adicionalmente, se puede aplicar un patrón al color de fondo de la diapositiva para darle un estilo único, con la clase `pattern`.

:::: flex
::: col 1/3 px-2

<div class="w-full bg-primary text-center rounded py-8 pattern">

`primary`

</div>
:::
::: col 1/3 px-2
<div class="w-full bg-secondary text-center rounded py-8 pattern">

`secondary`

</div>
:::
::: col 1/3 px-2
<div class="w-full bg-inverted text-center rounded py-8 pattern">

`inverted`

</div>
:::
::::

---

# Layouts

## Temas

La alineación general de los elementos se mantiene a la izquierda desde la parte superior.

Cada tema se adapta al color de fondo de la diapositiva, y se puede combinar con otros elementos como tablas, citas, listas y bloques de contenido que se adaptan al tema de la diapositiva.

Adicionalmente se puede añadir la clase `centered` para centrar el contenido de la diapositiva.

---

<!-- _class: inverted -->

# Estilo `inverted`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

---

<!-- _class: inverted centered-->

# Estilo `inverted centered`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

El texto se centra verticalmente, pero no horizontalmente.

---

<!-- _class: primary -->

# Estilo `primary`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

---

<!-- _class: primary centered -->

# Estilo `primary centered`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

El texto se centra horizontal y verticalmente.

---

<!-- _class: secondary -->

# Estilo `secondary`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

---

<!-- _class: secondary centered -->

# Estilo `secondary centered`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

Se centra el texto horizontal y verticalmente.

---

<!-- _class: lead -->

# Código

---

# Código

## Código en línea

Las diapositivas pueden incluir código fuente ya sea en línea o en bloques, y se pueden resaltar con un estilo específico.

Para incluir código en línea se utiliza la tilde invertida (\`) para delimitar el código: `` `hello world` ``, puede usarse más de una tilde invertida, pero siempre en número par.

Es importante notar que el código en línea no resalta ninguna sintaxis, por lo que se sugiere utilizarlo para fragmentos cortos de código.

---

# Código

## Bloques de código

Para incluir bloques de código se utilizan tres tildes invertidas (` ``` `), para delimitar el bloque de código.

````python
```python
def hello_world():
    print("Hello, world!")
```
````

Cada bloque de código debe incluir la etiqueta del lenguaje de programación para que se resalte la sintaxis correctamente.

- El resaltado de sintaxis lo provee el plugin [Shiki](https://shiki.matsu.io/), y soporta una amplia variedad de lenguajes de programación.

---

# Código

## Bloques de código

Los bloques de código pueden contener comentarios en su interior, mismos que reciben un estilo diferente al del código.

````python
```python
# Este es un comentario
def hello_world():
    print("Hello, world!")
```
````

Es importante que los comentarios y las líneas en general no sean demasiado largas, para evitar que el tamaño de la fuente sea muy pequeño.

```python
# Este es un ejemplo de una línea de código que excede los 100 caracteres de longitud, forzando a que la línea se "desborde" hacia la siguiente línea.
hello_world()
# Cuando una línea se "desborda", su contenido avanza hacia la siguiente línea, sin incrementar la númeración.
```

---

```python {4,11,15}
# Se sugiere no exceder los 80 ~ 85 caracteres por línea, y no exceder las 25 líneas
# por bloque para mantener el contenido dentro de la diapositiva.
for i in range(1, 11):
  print(f"Line {i}")

  if i % 2 == 0:
    print("Even number")
  else:
    print("Odd number")

numbers = [1, 2, 3, 4, 5]
for number in numbers:
  print(number)

hello_world()

def hello_world():
  print("Hello, world!")
  print("This is an example of a code block")
  print("It can contain multiple lines")
  print("And it will adjust to the slide width")

def another_fn():
  # Some code here
  pass
```

---

# Código

## Bloques de código

### Columnas

Los bloques de código pueden incluirse en columnas, y se sugiere que no se utilicen más de dos columnas para evitar que el contenido se vea saturado.

:::: flex
::: col 1/2 px-2

```python
def hello_world():
    print("Hello, world!")
```

:::
::: col 1/2 px-2

```python
def hello_world():
    print("Hello, world!")
```

:::
::::

Cuando se usa código en columnas es especialmente importante mantener un espaciado adecuado para lograr un equilibrio visual.

---

<!-- _class: lead -->

# Bloques

---

# Bloques

Es posible incluir bloques de contenido en las diapositivas, y se pueden combinar con otros elementos para crear diapositivas más dinámicas.

:::: flex
::: col 1/2 px-2

Los bloques disponibles para mensajes son:

- OK `ok`
- Información `info`
- Advertencia `warning`
- Error `error`
- Nota `note`

:::
::: col 1/2 px-2

Así también se pueden utilizar bloques de tema:

- Primario `primary`
- Secundario `secondary`

Y un bloque especial para citas:

- Cita `quote`

:::
::::

---

# Bloques

## Mensajes

Los bloques de mensajes pueden contener contenido diverso, pero se sugiere limitar a un párrafo o dos para mantener la atención en el mensaje.

::: ok
Este es un mensaje afirmativo
:::

::: info
Este es un mensaje informativo
:::

::: warning
Este es un mensaje de advertencia
:::

::: error
Este es un mensaje de error
:::

Si el bloque se utiliza en alguna diapositiva con diseño `cols-2`, `cols-3`, `rows-2`, `rows-3` o `rows`, el bloque se posicionará en la parte inferior central de la diapositiva.

---

# Bloques

## Tema

Los bloques de tema adaptan su color de resaltado según el tema de la diapositiva, y pueden contener contenido diverso.

::: primary
Este es un bloque de tema primario
:::

::: secondary
Este es un bloque de tema secundario
:::

El resaltado de estos bloques consiste en una cinta en la parte izquierda del bloque.

---

# Bloques

## Citas

Los bloques de citas se utilizan para resaltar un mensaje o contenido específico, y pueden incluir un autor al final.

::: quote
_La simplicidad es la máxima sofisticación_
<cite>Leonardo da Vinci</cite>
:::

::: quote
_Si nadie conoce la cita, seguramente no tendrá autor_
:::

---

# Bloques

## Notas

Este tipo de bloque se usan en conjunto con `<note>*</note>` para especificar el contenido de la nota<note>\*</note>.

- A diferencia del resto de bloques, este se posiciona en la parte inferior central de la diapositiva.

::: note
Aunque se sugiere que la nota sea breve, si se requiere, el diseño del bloque permite notas de hasta 2 líneas. Sin embargo, se debe ser cuidadoso para evitar que la nota salga de la diapositiva.
:::

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

<script src="https://unpkg.com/@phosphor-icons/web"></script>

---

<!-- paginate: skip -->
<!-- class: references -->

# Referencias

- Autor (Fecha). _Título del artículo_. <https://www.example.com>

```md
- Autor (Fecha). _Título del artículo_. <https://www.example.com>
```

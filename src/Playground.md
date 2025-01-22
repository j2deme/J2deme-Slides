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
  }
---

<!-- _class: cover -->
<!-- _paginate: false -->

# Nombre de la unidad

## Asignatura

Dr. Jaime Jesús Delgado Meraz

### Unidad 99

#### ABC - 1234

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
: Nombre de la asignatura

Carrera
: Carrera 1 a la que aplica
: Carrera 2 a la que aplica
:::
::: right
Clave
: ABC - 1234

SATCA
: 9 - 9 - 9
:::

---

<!-- _class: toc -->

# Secciones

1. [Contenidos](#contenidos)
2. [Colores](#colores)
3. [Bloques](#bloques)
4. [Layouts](#layouts)
5. [Código](#código)

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
```

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
>
> <cite>William of Ockham</cite>

```md
> _En igualdad de condiciones, la solución más simple suele ser la más probable_
>
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

> _En igualdad de condiciones, la solución más simple suele ser la más probable_.
>
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
>
> <cite>William of Ockham</cite>
```

Adicionalmente, deberá incluirse una directiva `_class` con las clases `primary` y `centered` para centrar la cita en la diapositiva.

Puede incluirse una imagen junto a la cita para darle un contexto visual, se sugiere una proporción de 70/30.

---

<!-- _class: primary centered -->

> _En igualdad de condiciones, la solución más simple suele ser la más probable_
>
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

Se pueden combinar con algunas directivas para ajustar las dimensiones de la imagen:

- Para el ancho `w`:
  - _p.e._ `w:50` para pixeles, `w:50%` para porcentaje.
- Para el alto `h`:
  - _p.e._ `h:50` para pixeles, `h:50%` para porcentaje.

:::
::: col 1/3 px-2
[w:100] ![w:100](../src/assets/avatar.png)
[w:30 h:35] ![w:30 h:35](../src/assets/avatar.png)
[h:200] ![h:200](../src/assets/avatar.png)
:::
::::

---

# Contenidos

## Imágenes

### Directivas

Se pueden agregar directivas a las imagenes para ajustar su visualización.

```md
![bg](ruta/a/la/imagen.png)
```

![bg right:40% cover](../src/assets/pattern-alt.svg)

Se pueden usar las directivas:

- `bg` para poner la imagen como fondo
- `right` y `left` para ajustar la posición
- `cover` ajusta los bordes superiores e inferiores de la imagen
- `fit` ajusta la imagen dentro de los bordes

---

# Contenidos

## Imágenes

### Flotantes

En algunos casos se puede requerir que las imágenes se mezclen con el texto, para lo que se utilizan _flotantes_.

![Imagen izquierda #l](https://unsplash.it/100/100) Flotando a la izquierda con la directiva `[#l]`, por otro lado si se requiere que la imagen quede entre entre las líneas del texto ![Imagen centrada #c](https://unsplash.it/100/100) se utiliza la directiva `[#c]`, y si se requiere que la imagen flote a la derecha se usa la directiva `[#r]`. ![Imagen derecha  #r](https://unsplash.it/100/100)
El uso de estas directivas para imágenes flotantes resalta el contenido de la diapositiva.

---

# Contenidos

## Imágenes

### Flotantes

![#l](https://unsplash.it/200/100) ![#l](https://unsplash.it/200/200) ![#l](https://unsplash.it/400/200) ![#l](https://unsplash.it/200/200) ![#l](https://unsplash.it/200/100)

---

# Contenidos

## Iconos

Los iconos se pueden incluir en las diapositivas utilizando la directiva `icon`[*:Función incluída en el `engine` de la plantilla].

```md
:icon:icon-name:{clase1 ...}
```

Donde:

- `icon-name` es el nombre del icono, de acuerdo a la librería de iconos [Tabler Icons](https://tablericons.com/).
- `clase1 ...` son las clases adicionales que se pueden aplicar al icono (opcional), para cambiar su tamaño o color. _p.e._ `xl blue-500`.

---

# Contenidos

## Iconos

### Ejemplos

#### Tamaños

|      `xs`       |      `sm`       |     `-`     |      `lg`       |      `xl`       |      `xxl`       |      `xxxl`       |
| :-------------: | :-------------: | :---------: | :-------------: | :-------------: | :--------------: | :---------------: |
| :icon:lego:{xs} | :icon:lego:{sm} | :icon:lego: | :icon:lego:{lg} | :icon:lego:{xl} | :icon:lego:{xxl} | :icon:lego:{xxxl} |

#### Colores

| Icono                  | Clase                     |                   Resultado                   |
| ---------------------- | ------------------------- | :-------------------------------------------: |
| `brand-twitter-filled` | `azure-300`               |    :icon:brand-twitter-filled:{azure-300}     |
| `brand-facebook`       | `bg-blue-500`             |      :icon:brand-facebook:{bg-blue-500}       |
| `brand-youtube`        | `bg-red rounded-full p-1` | :icon:brand-youtube:{bg-red rounded-full p-1} |

---

<!-- _class: lead -->

# Colores

---

# Colores

## Paleta base

A partir del color primario base, se generan los colores de la plantilla:

<div class="grid grid-cols-3 gap-2 py-1 text-center">
  <div class="bg-primary light rounded py-4">
    Primary light
  </div>
  <div class="bg-primary rounded py-4">
    Primary
  </div>
  <div class="bg-primary dark rounded py-4">
    Primary dark
  </div>
</div>

<div class="grid grid-cols-3 gap-2 py-1 text-center">
  <div class="bg-secondary light rounded py-4">
    Secondary light
  </div>
  <div class="bg-secondary rounded py-4">
    Secondary
  </div>
  <div class="bg-secondary dark rounded py-4">
    Secondary dark
  </div>
</div>

<div class="grid grid-cols-3 gap-2 py-1 text-center">
  <div class="bg-accent light rounded py-4">
    Accent lighter
  </div>
  <div class="bg-accent rounded py-4">
    Accent
  </div>
  <div class="bg-accent dark rounded py-4">
    Accent darker
  </div>
</div>

- El color de la tipografía se adapta automáticamente a cada tema y escala de color:

```css
:root {
  --primary: #1274c5;
  --l-threshold: 0.7;
  --l: clamp(0, (l / var(--l-threshold) - 1) * -infinity, 1);
  color: oklch(from var(--primary) var(--l) 0 h) !important;
}
```

---

# Colores

## Paleta extendida

Adicionalmente se pueden utilizar los colores:

<div class="grid grid-cols-10 gap-1 py-1 text-center">
  <div class="bg-red py-2 rounded">red</div>
  <div class="bg-pink py-2 rounded">pink</div>
  <div class="bg-fuchsia py-2 rounded">fuchsia</div>
  <div class="bg-purple py-2 rounded">purple</div>
  <div class="bg-violet py-2 rounded">violet</div>
  <div class="bg-indigo py-2 rounded">indigo</div>
  <div class="bg-blue py-2 rounded">blue</div>
  <div class="bg-azure py-2 rounded">azure</div>
  <div class="bg-cyan py-2 rounded">cyan</div>
  <div class="bg-jade py-2 rounded">jade</div>
</div>

<div class="grid grid-cols-10 gap-1 py-1 text-center">
  <div class="bg-green py-2 rounded">green</div>
  <div class="bg-lime py-2 rounded">lime</div>
  <div class="bg-yellow py-2 rounded">yellow</div>
  <div class="bg-amber py-2 rounded">amber</div>
  <div class="bg-pumpkin py-2 rounded">pumpkin</div>
  <div class="bg-orange py-2 rounded">orange</div>
  <div class="bg-sand py-2 rounded">sand</div>
  <div class="bg-gray py-2 rounded">gray</div>
  <div class="bg-zinc py-2 rounded">zinc</div>
  <div class="bg-slate py-2 rounded">slate</div>
</div>

<div class="grid grid-cols-2 gap-1 py-1 text-center">
  <div class="bg-dark py-2 rounded">dark</div>
  <div class="bg-light py-2 rounded border border-solid border-black">light</div>
</div>

Estos colores pueden usarse como:

- Variables CSS: `--color`, `--color-shade`, `--bg-color` o `--bg-color-shade`.
- Clases: `.color`, `.color-shade`, `.bg-color` o `.bg-color-shade`.

::: note
Adaptado de la paleta de colores de Pico CSS ✨.
:::

---

# Colores

## Paleta extendida

### _Shades_

Las escalas de colores van de 50 a 950 (en escalas +50), indicando la luminancia del color.

<div class="boxes full text-center text-sm">
  <div class="bg-red w-32 rounded">red</div>
  <div class="bg-red-50 rounded">50</div>
  <div class="bg-red-100 rounded">100</div>
  <div class="bg-red-150 rounded">150</div>
  <div class="bg-red-200 rounded">200</div>
  <div class="bg-red-250 rounded">250</div>
  <div class="bg-red-300 rounded">300</div>
  <div class="bg-red-350 rounded">350</div>
  <div class="bg-red-400 rounded">400</div>
  <div class="bg-red-450 rounded">450</div>
  <div class="bg-red-500 rounded">500</div>
  <div class="bg-red-550 rounded">550</div>
  <div class="bg-red-600 rounded">600</div>
  <div class="bg-red-650 rounded">650</div>
  <div class="bg-red-700 rounded">700</div>
  <div class="bg-red-750 rounded">750</div>
  <div class="bg-red-800 rounded">800</div>
  <div class="bg-red-850 rounded">850</div>
  <div class="bg-red-900 rounded">900</div>
  <div class="bg-red-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-pink w-32 rounded">pink</div>
  <div class="bg-pink-50 rounded">50</div>
  <div class="bg-pink-100 rounded">100</div>
  <div class="bg-pink-150 rounded">150</div>
  <div class="bg-pink-200 rounded">200</div>
  <div class="bg-pink-250 rounded">250</div>
  <div class="bg-pink-300 rounded">300</div>
  <div class="bg-pink-350 rounded">350</div>
  <div class="bg-pink-400 rounded">400</div>
  <div class="bg-pink-450 rounded">450</div>
  <div class="bg-pink-500 rounded">500</div>
  <div class="bg-pink-550 rounded">550</div>
  <div class="bg-pink-600 rounded">600</div>
  <div class="bg-pink-650 rounded">650</div>
  <div class="bg-pink-700 rounded">700</div>
  <div class="bg-pink-750 rounded">750</div>
  <div class="bg-pink-800 rounded">800</div>
  <div class="bg-pink-850 rounded">850</div>
  <div class="bg-pink-900 rounded">900</div>
  <div class="bg-pink-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-fuchsia w-32 rounded">fuchsia</div>
  <div class="bg-fuchsia-50 rounded">50</div>
  <div class="bg-fuchsia-100 rounded">100</div>
  <div class="bg-fuchsia-150 rounded">150</div>
  <div class="bg-fuchsia-200 rounded">200</div>
  <div class="bg-fuchsia-250 rounded">250</div>
  <div class="bg-fuchsia-300 rounded">300</div>
  <div class="bg-fuchsia-350 rounded">350</div>
  <div class="bg-fuchsia-400 rounded">400</div>
  <div class="bg-fuchsia-450 rounded">450</div>
  <div class="bg-fuchsia-500 rounded">500</div>
  <div class="bg-fuchsia-550 rounded">550</div>
  <div class="bg-fuchsia-600 rounded">600</div>
  <div class="bg-fuchsia-650 rounded">650</div>
  <div class="bg-fuchsia-700 rounded">700</div>
  <div class="bg-fuchsia-750 rounded">750</div>
  <div class="bg-fuchsia-800 rounded">800</div>
  <div class="bg-fuchsia-850 rounded">850</div>
  <div class="bg-fuchsia-900 rounded">900</div>
  <div class="bg-fuchsia-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-purple w-32 rounded">purple</div>
  <div class="bg-purple-50 rounded">50</div>
  <div class="bg-purple-100 rounded">100</div>
  <div class="bg-purple-150 rounded">150</div>
  <div class="bg-purple-200 rounded">200</div>
  <div class="bg-purple-250 rounded">250</div>
  <div class="bg-purple-300 rounded">300</div>
  <div class="bg-purple-350 rounded">350</div>
  <div class="bg-purple-400 rounded">400</div>
  <div class="bg-purple-450 rounded">450</div>
  <div class="bg-purple-500 rounded">500</div>
  <div class="bg-purple-550 rounded">550</div>
  <div class="bg-purple-600 rounded">600</div>
  <div class="bg-purple-650 rounded">650</div>
  <div class="bg-purple-700 rounded">700</div>
  <div class="bg-purple-750 rounded">750</div>
  <div class="bg-purple-800 rounded">800</div>
  <div class="bg-purple-850 rounded">850</div>
  <div class="bg-purple-900 rounded">900</div>
  <div class="bg-purple-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-violet w-32 rounded">violet</div>
  <div class="bg-violet-50 rounded">50</div>
  <div class="bg-violet-100 rounded">100</div>
  <div class="bg-violet-150 rounded">150</div>
  <div class="bg-violet-200 rounded">200</div>
  <div class="bg-violet-250 rounded">250</div>
  <div class="bg-violet-300 rounded">300</div>
  <div class="bg-violet-350 rounded">350</div>
  <div class="bg-violet-400 rounded">400</div>
  <div class="bg-violet-450 rounded">450</div>
  <div class="bg-violet-500 rounded">500</div>
  <div class="bg-violet-550 rounded">550</div>
  <div class="bg-violet-600 rounded">600</div>
  <div class="bg-violet-650 rounded">650</div>
  <div class="bg-violet-700 rounded">700</div>
  <div class="bg-violet-750 rounded">750</div>
  <div class="bg-violet-800 rounded">800</div>
  <div class="bg-violet-850 rounded">850</div>
  <div class="bg-violet-900 rounded">900</div>
  <div class="bg-violet-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-indigo w-32 rounded">indigo</div>
  <div class="bg-indigo-50 rounded">50</div>
  <div class="bg-indigo-100 rounded">100</div>
  <div class="bg-indigo-150 rounded">150</div>
  <div class="bg-indigo-200 rounded">200</div>
  <div class="bg-indigo-250 rounded">250</div>
  <div class="bg-indigo-300 rounded">300</div>
  <div class="bg-indigo-350 rounded">350</div>
  <div class="bg-indigo-400 rounded">400</div>
  <div class="bg-indigo-450 rounded">450</div>
  <div class="bg-indigo-500 rounded">500</div>
  <div class="bg-indigo-550 rounded">550</div>
  <div class="bg-indigo-600 rounded">600</div>
  <div class="bg-indigo-650 rounded">650</div>
  <div class="bg-indigo-700 rounded">700</div>
  <div class="bg-indigo-750 rounded">750</div>
  <div class="bg-indigo-800 rounded">800</div>
  <div class="bg-indigo-850 rounded">850</div>
  <div class="bg-indigo-900 rounded">900</div>
  <div class="bg-indigo-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-blue w-32 rounded">blue</div>
  <div class="bg-blue-50 rounded">50</div>
  <div class="bg-blue-100 rounded">100</div>
  <div class="bg-blue-150 rounded">150</div>
  <div class="bg-blue-200 rounded">200</div>
  <div class="bg-blue-250 rounded">250</div>
  <div class="bg-blue-300 rounded">300</div>
  <div class="bg-blue-350 rounded">350</div>
  <div class="bg-blue-400 rounded">400</div>
  <div class="bg-blue-450 rounded">450</div>
  <div class="bg-blue-500 rounded">500</div>
  <div class="bg-blue-550 rounded">550</div>
  <div class="bg-blue-600 rounded">600</div>
  <div class="bg-blue-650 rounded">650</div>
  <div class="bg-blue-700 rounded">700</div>
  <div class="bg-blue-750 rounded">750</div>
  <div class="bg-blue-800 rounded">800</div>
  <div class="bg-blue-850 rounded">850</div>
  <div class="bg-blue-900 rounded">900</div>
  <div class="bg-blue-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-azure w-32 rounded">azure</div>
  <div class="bg-azure-50 rounded">50</div>
  <div class="bg-azure-100 rounded">100</div>
  <div class="bg-azure-150 rounded">150</div>
  <div class="bg-azure-200 rounded">200</div>
  <div class="bg-azure-250 rounded">250</div>
  <div class="bg-azure-300 rounded">300</div>
  <div class="bg-azure-350 rounded">350</div>
  <div class="bg-azure-400 rounded">400</div>
  <div class="bg-azure-450 rounded">450</div>
  <div class="bg-azure-500 rounded">500</div>
  <div class="bg-azure-550 rounded">550</div>
  <div class="bg-azure-600 rounded">600</div>
  <div class="bg-azure-650 rounded">650</div>
  <div class="bg-azure-700 rounded">700</div>
  <div class="bg-azure-750 rounded">750</div>
  <div class="bg-azure-800 rounded">800</div>
  <div class="bg-azure-850 rounded">850</div>
  <div class="bg-azure-900 rounded">900</div>
  <div class="bg-azure-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-cyan w-32 rounded">cyan</div>
  <div class="bg-cyan-50 rounded">50</div>
  <div class="bg-cyan-100 rounded">100</div>
  <div class="bg-cyan-150 rounded">150</div>
  <div class="bg-cyan-200 rounded">200</div>
  <div class="bg-cyan-250 rounded">250</div>
  <div class="bg-cyan-300 rounded">300</div>
  <div class="bg-cyan-350 rounded">350</div>
  <div class="bg-cyan-400 rounded">400</div>
  <div class="bg-cyan-450 rounded">450</div>
  <div class="bg-cyan-500 rounded">500</div>
  <div class="bg-cyan-550 rounded">550</div>
  <div class="bg-cyan-600 rounded">600</div>
  <div class="bg-cyan-650 rounded">650</div>
  <div class="bg-cyan-700 rounded">700</div>
  <div class="bg-cyan-750 rounded">750</div>
  <div class="bg-cyan-800 rounded">800</div>
  <div class="bg-cyan-850 rounded">850</div>
  <div class="bg-cyan-900 rounded">900</div>
  <div class="bg-cyan-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-jade w-32 rounded">jade</div>
  <div class="bg-jade-50 rounded">50</div>
  <div class="bg-jade-100 rounded">100</div>
  <div class="bg-jade-150 rounded">150</div>
  <div class="bg-jade-200 rounded">200</div>
  <div class="bg-jade-250 rounded">250</div>
  <div class="bg-jade-300 rounded">300</div>
  <div class="bg-jade-350 rounded">350</div>
  <div class="bg-jade-400 rounded">400</div>
  <div class="bg-jade-450 rounded">450</div>
  <div class="bg-jade-500 rounded">500</div>
  <div class="bg-jade-550 rounded">550</div>
  <div class="bg-jade-600 rounded">600</div>
  <div class="bg-jade-650 rounded">650</div>
  <div class="bg-jade-700 rounded">700</div>
  <div class="bg-jade-750 rounded">750</div>
  <div class="bg-jade-800 rounded">800</div>
  <div class="bg-jade-850 rounded">850</div>
  <div class="bg-jade-900 rounded">900</div>
  <div class="bg-jade-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-green w-32 rounded">green</div>
  <div class="bg-green-50 rounded">50</div>
  <div class="bg-green-100 rounded">100</div>
  <div class="bg-green-150 rounded">150</div>
  <div class="bg-green-200 rounded">200</div>
  <div class="bg-green-250 rounded">250</div>
  <div class="bg-green-300 rounded">300</div>
  <div class="bg-green-350 rounded">350</div>
  <div class="bg-green-400 rounded">400</div>
  <div class="bg-green-450 rounded">450</div>
  <div class="bg-green-500 rounded">500</div>
  <div class="bg-green-550 rounded">550</div>
  <div class="bg-green-600 rounded">600</div>
  <div class="bg-green-650 rounded">650</div>
  <div class="bg-green-700 rounded">700</div>
  <div class="bg-green-750 rounded">750</div>
  <div class="bg-green-800 rounded">800</div>
  <div class="bg-green-850 rounded">850</div>
  <div class="bg-green-900 rounded">900</div>
  <div class="bg-green-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-lime w-32 rounded">lime</div>
  <div class="bg-lime-50 rounded">50</div>
  <div class="bg-lime-100 rounded">100</div>
  <div class="bg-lime-150 rounded">150</div>
  <div class="bg-lime-200 rounded">200</div>
  <div class="bg-lime-250 rounded">250</div>
  <div class="bg-lime-300 rounded">300</div>
  <div class="bg-lime-350 rounded">350</div>
  <div class="bg-lime-400 rounded">400</div>
  <div class="bg-lime-450 rounded">450</div>
  <div class="bg-lime-500 rounded">500</div>
  <div class="bg-lime-550 rounded">550</div>
  <div class="bg-lime-600 rounded">600</div>
  <div class="bg-lime-650 rounded">650</div>
  <div class="bg-lime-700 rounded">700</div>
  <div class="bg-lime-750 rounded">750</div>
  <div class="bg-lime-800 rounded">800</div>
  <div class="bg-lime-850 rounded">850</div>
  <div class="bg-lime-900 rounded">900</div>
  <div class="bg-lime-950 rounded">950</div>
</div>

---

# Colores

## Paleta extendida

### _Shades_

<div class="boxes full text-center text-sm">
  <div class="bg-yellow w-32 rounded">yellow</div>
  <div class="bg-yellow-50 rounded">50</div>
  <div class="bg-yellow-100 rounded">100</div>
  <div class="bg-yellow-150 rounded">150</div>
  <div class="bg-yellow-200 rounded">200</div>
  <div class="bg-yellow-250 rounded">250</div>
  <div class="bg-yellow-300 rounded">300</div>
  <div class="bg-yellow-350 rounded">350</div>
  <div class="bg-yellow-400 rounded">400</div>
  <div class="bg-yellow-450 rounded">450</div>
  <div class="bg-yellow-500 rounded">500</div>
  <div class="bg-yellow-550 rounded">550</div>
  <div class="bg-yellow-600 rounded">600</div>
  <div class="bg-yellow-650 rounded">650</div>
  <div class="bg-yellow-700 rounded">700</div>
  <div class="bg-yellow-750 rounded">750</div>
  <div class="bg-yellow-800 rounded">800</div>
  <div class="bg-yellow-850 rounded">850</div>
  <div class="bg-yellow-900 rounded">900</div>
  <div class="bg-yellow-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-amber w-32 rounded">amber</div>
  <div class="bg-amber-50 rounded">50</div>
  <div class="bg-amber-100 rounded">100</div>
  <div class="bg-amber-150 rounded">150</div>
  <div class="bg-amber-200 rounded">200</div>
  <div class="bg-amber-250 rounded">250</div>
  <div class="bg-amber-300 rounded">300</div>
  <div class="bg-amber-350 rounded">350</div>
  <div class="bg-amber-400 rounded">400</div>
  <div class="bg-amber-450 rounded">450</div>
  <div class="bg-amber-500 rounded">500</div>
  <div class="bg-amber-550 rounded">550</div>
  <div class="bg-amber-600 rounded">600</div>
  <div class="bg-amber-650 rounded">650</div>
  <div class="bg-amber-700 rounded">700</div>
  <div class="bg-amber-750 rounded">750</div>
  <div class="bg-amber-800 rounded">800</div>
  <div class="bg-amber-850 rounded">850</div>
  <div class="bg-amber-900 rounded">900</div>
  <div class="bg-amber-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-pumpkin w-32 rounded">pumpkin</div>
  <div class="bg-pumpkin-50 rounded">50</div>
  <div class="bg-pumpkin-100 rounded">100</div>
  <div class="bg-pumpkin-150 rounded">150</div>
  <div class="bg-pumpkin-200 rounded">200</div>
  <div class="bg-pumpkin-250 rounded">250</div>
  <div class="bg-pumpkin-300 rounded">300</div>
  <div class="bg-pumpkin-350 rounded">350</div>
  <div class="bg-pumpkin-400 rounded">400</div>
  <div class="bg-pumpkin-450 rounded">450</div>
  <div class="bg-pumpkin-500 rounded">500</div>
  <div class="bg-pumpkin-550 rounded">550</div>
  <div class="bg-pumpkin-600 rounded">600</div>
  <div class="bg-pumpkin-650 rounded">650</div>
  <div class="bg-pumpkin-700 rounded">700</div>
  <div class="bg-pumpkin-750 rounded">750</div>
  <div class="bg-pumpkin-800 rounded">800</div>
  <div class="bg-pumpkin-850 rounded">850</div>
  <div class="bg-pumpkin-900 rounded">900</div>
  <div class="bg-pumpkin-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-orange w-32 rounded">orange</div>
  <div class="bg-orange-50 rounded">50</div>
  <div class="bg-orange-100 rounded">100</div>
  <div class="bg-orange-150 rounded">150</div>
  <div class="bg-orange-200 rounded">200</div>
  <div class="bg-orange-250 rounded">250</div>
  <div class="bg-orange-300 rounded">300</div>
  <div class="bg-orange-350 rounded">350</div>
  <div class="bg-orange-400 rounded">400</div>
  <div class="bg-orange-450 rounded">450</div>
  <div class="bg-orange-500 rounded">500</div>
  <div class="bg-orange-550 rounded">550</div>
  <div class="bg-orange-600 rounded">600</div>
  <div class="bg-orange-650 rounded">650</div>
  <div class="bg-orange-700 rounded">700</div>
  <div class="bg-orange-750 rounded">750</div>
  <div class="bg-orange-800 rounded">800</div>
  <div class="bg-orange-850 rounded">850</div>
  <div class="bg-orange-900 rounded">900</div>
  <div class="bg-orange-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-sand w-32 rounded">sand</div>
  <div class="bg-sand-50 rounded">50</div>
  <div class="bg-sand-100 rounded">100</div>
  <div class="bg-sand-150 rounded">150</div>
  <div class="bg-sand-200 rounded">200</div>
  <div class="bg-sand-250 rounded">250</div>
  <div class="bg-sand-300 rounded">300</div>
  <div class="bg-sand-350 rounded">350</div>
  <div class="bg-sand-400 rounded">400</div>
  <div class="bg-sand-450 rounded">450</div>
  <div class="bg-sand-500 rounded">500</div>
  <div class="bg-sand-550 rounded">550</div>
  <div class="bg-sand-600 rounded">600</div>
  <div class="bg-sand-650 rounded">650</div>
  <div class="bg-sand-700 rounded">700</div>
  <div class="bg-sand-750 rounded">750</div>
  <div class="bg-sand-800 rounded">800</div>
  <div class="bg-sand-850 rounded">850</div>
  <div class="bg-sand-900 rounded">900</div>
  <div class="bg-sand-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-gray w-32 rounded">gray</div>
  <div class="bg-gray-50 rounded">50</div>
  <div class="bg-gray-100 rounded">100</div>
  <div class="bg-gray-150 rounded">150</div>
  <div class="bg-gray-200 rounded">200</div>
  <div class="bg-gray-250 rounded">250</div>
  <div class="bg-gray-300 rounded">300</div>
  <div class="bg-gray-350 rounded">350</div>
  <div class="bg-gray-400 rounded">400</div>
  <div class="bg-gray-450 rounded">450</div>
  <div class="bg-gray-500 rounded">500</div>
  <div class="bg-gray-550 rounded">550</div>
  <div class="bg-gray-600 rounded">600</div>
  <div class="bg-gray-650 rounded">650</div>
  <div class="bg-gray-700 rounded">700</div>
  <div class="bg-gray-750 rounded">750</div>
  <div class="bg-gray-800 rounded">800</div>
  <div class="bg-gray-850 rounded">850</div>
  <div class="bg-gray-900 rounded">900</div>
  <div class="bg-gray-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-zinc w-32 rounded">zinc</div>
  <div class="bg-zinc-50 rounded">50</div>
  <div class="bg-zinc-100 rounded">100</div>
  <div class="bg-zinc-150 rounded">150</div>
  <div class="bg-zinc-200 rounded">200</div>
  <div class="bg-zinc-250 rounded">250</div>
  <div class="bg-zinc-300 rounded">300</div>
  <div class="bg-zinc-350 rounded">350</div>
  <div class="bg-zinc-400 rounded">400</div>
  <div class="bg-zinc-450 rounded">450</div>
  <div class="bg-zinc-500 rounded">500</div>
  <div class="bg-zinc-550 rounded">550</div>
  <div class="bg-zinc-600 rounded">600</div>
  <div class="bg-zinc-650 rounded">650</div>
  <div class="bg-zinc-700 rounded">700</div>
  <div class="bg-zinc-750 rounded">750</div>
  <div class="bg-zinc-800 rounded">800</div>
  <div class="bg-zinc-850 rounded">850</div>
  <div class="bg-zinc-900 rounded">900</div>
  <div class="bg-zinc-950 rounded">950</div>
</div>

<div class="boxes full text-center text-sm">
  <div class="bg-slate-500 w-32 rounded">500</div>
  <div class="bg-slate-50 rounded">50</div>
  <div class="bg-slate-100 rounded">100</div>
  <div class="bg-slate-150 rounded">150</div>
  <div class="bg-slate-200 rounded">200</div>
  <div class="bg-slate-250 rounded">250</div>
  <div class="bg-slate-300 rounded">300</div>
  <div class="bg-slate-350 rounded">350</div>
  <div class="bg-slate-400 rounded">400</div>
  <div class="bg-slate-450 rounded">450</div>
  <div class="bg-slate rounded">slate</div>
  <div class="bg-slate-550 rounded">550</div>
  <div class="bg-slate-600 rounded">600</div>
  <div class="bg-slate-650 rounded">650</div>
  <div class="bg-slate-700 rounded">700</div>
  <div class="bg-slate-750 rounded">750</div>
  <div class="bg-slate-800 rounded">800</div>
  <div class="bg-slate-850 rounded">850</div>
  <div class="bg-slate-900 rounded">900</div>
  <div class="bg-slate-950 rounded">950</div>
</div>

- Estos colores pueden usarse para el texto, fondos e iconos.

---

# Colores

## _Swatches_ 🎨

Es posible que algunos ejemplos requieran mostrar paletas de colores, y para ello se pueden utilizar _swatches_ para mostrar los colores disponibles o seleccionados.

```html
<div class="swatch">
  <div class="bg-red"></div>
  <div class="bg-yellow"></div>
  <div class="bg-green"></div>
  <div class="bg-blue"></div>
  <div class="bg-indigo"></div>
  <div class="bg-purple"></div>
  <div class="bg-pink"></div>
</div>
```

<div class="swatch">
  <div class="bg-red"></div>
  <div class="bg-yellow"></div>
  <div class="bg-green"></div>
  <div class="bg-blue"></div>
  <div class="bg-indigo"></div>
  <div class="bg-purple"></div>
  <div class="bg-pink"></div>
</div>

Por default, se crea una fila de _blobs_ centrados en la fila.

---

# Colores

## _Swatches_ 🎨

### Estilos

Se pueden usar estilos alternativos para los _swatches_.

| Clase         | Resultado                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| `.swatch`     | <div class="swatch"><div class="bg-red"></div><div class="bg-yellow"></div><div class="bg-blue"></div></div>     |
| `.boxes`      | <div class="boxes"><div class="bg-red"></div><div class="bg-yellow"></div><div class="bg-blue"></div></div>      |
| `.dots`       | <div class="dots"><div class="bg-red"></div><div class="bg-yellow"></div><div class="bg-blue"></div></div>       |
| `.dots.mini`  | <div class="dots mini"><div class="bg-red"></div><div class="bg-yellow"></div><div class="bg-blue"></div></div>  |
| `.boxes.mini` | <div class="boxes mini"><div class="bg-red"></div><div class="bg-yellow"></div><div class="bg-blue"></div></div> |

- Si se requiere, es posible que el _swatch_ ocupe todo el ancho disponible, agregando la clase `.full`.
  - _p.e._ `.swatch.full`.

---

# Colores

## _Swatches_

### Dots & Boxes

Si se requiere mostrar sólo un color dentro del texto al usar Markdown, se tienen disponibles algunas directivas:

|   Directiva    |  Resultado   | Descripción                                                                           |
| :------------: | :----------: | ------------------------------------------------------------------------------------- |
|  `[o:--red]`   |  [o:--red]   | Muestra un _dot_ de color `var(--red)` [*:Colores disponibles en la paleta extendida] |
| `[o:#1274c5]`  | [o:#1274c5]  | Muestra un _dot_ de color `#1274c5`                                                   |
| `[o2:--blue]`  | [o2:--blue]  | Muestra un _box_ de color `var(--blue)` <note>\*</note>                               |
| `[o2:#ff0off]` | [o2:#ff00ff] | Muestra un _box_ de color `#ff0off`                                                   |

- También se tienen disponibles las versiones _mini_ de ambos estilos, agregando un `-` al final de la directiva.
  - _p.e._ `[o-:--amber-200]` [o-:--amber-200] o `[o2-:#45bb45]` [o2-:#45bb45].

---

<!-- _class: lead -->

# Bloques

---

# Bloques

Es posible incluir bloques de contenido en las diapositivas, y se pueden combinar con otros elementos para crear diapositivas más dinámicas.

:::: flex
::: col 1/2 px-2

Los bloques disponibles para mensajes son:

- OK `ok` [o:--ok]
- Información `info` [o:--info]
- Advertencia `warning` [o:--warning]
- Error `error` o `danger` [o:--error]

:::
::: col 1/2 px-2

Así también se pueden utilizar bloques de tema:

- Primario `primary` [o:--primary]
- Secundario `secondary` [o:--secondary]

Y bloques especiales para:

- Cita `quote` [o:--gray-600]
- Nota `note` [o:--note]
- Tip `tip` [o:--tip]

:::
::::

---

# Bloques

## Sintaxis

- Los bloques se crean con la sintaxis:

```md
::: tipo
Contenido que puede incluir **Markdown** y HTML.
:::
```

- Una sintaxis alternativa para bloques flotantes es:

```md
[tipo:Contenido que puede incluir **Markdown** y HTML.]
```

[info:La sintaxis alternativa solo esta disponible para `ok`, `info`, `warning`, `error`, `danger` y `tip`]

---

# Bloques

## Tipos

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

## Mensajes

::: ok

# Mensaje afirmativo

Este es un mensaje afirmativo muy largo, que además incluye un título y una viñeta, y que se utiliza para resaltar un mensaje positivo.

- Viñeta que contiene código `hello world`

:::

::: info

# Mensaje informativo

Este es un mensaje informativo
:::

::: warning

# Mensaje de advertencia

Este es un mensaje de advertencia
:::

::: error

# Mensaje de error

Este es un mensaje de error
:::

---

# Bloques

## Notas

Un bloque de nota se utiliza para especificar contenido adicional o notas al pie de la diapositiva, se sugiere que sea breve.

- Puede incluirse mediante HTML, ya que la plantilla incluye un estilo específico para notas.
  - La nota siempre se ajusta al pie de la diapositiva y puede contener **Markdown**.

```html
Este texto tiene una nota <note>*</note>

<div class="note">Texto de la nota</div>
```

- Adicionalmente, el `engine` de la plantilla incluye una directiva más sencilla para incluir notas[*:Sólo puede haber **1** nota por slide].

```md
Aquí va una nota simple[*:Sólo puede haber **1** nota por slide]
```

- Por compatibilidad con plantillas previas, se mantiene la sintaxis de `::: note`.

---

# Bloques

## Tips

Los bloques de tip se utilizan para resaltar un consejo o sugerencia, y pueden incluir contenido diverso.

- Por defecto se ajustan al pie de la diapositiva y pueden contener Markdown.

Su sintaxis es similar a la de los bloques flotantes:

```md
[tip:Este es un mensaje de tipo `tip`]
```

[tip:Este es un mensaje de tipo `tip`]

- Pueden ser muy útiles para proporcionar información adicional o sugerencias a los lectores.

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

Los encabezados de nivel 4 - 6 alternan entre el color primario, cuerpo y secundario, reduciendo su tamaño de fuente progresivamente.

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

- `split` para un diseño a 3 filas, la fila superior `top`, la fila intermedia dividida en `left`, `center`, y la fila inferior `bottom`.
  - Los contenedores `top` y `bottom` se ajustan al contenido, pero sino se requieren, se sugiere usar un diseño de tipo `cols-2`.
- `cols-2` para un diseño a 2 columnas, se combina con los contenedores `left` y `right`.
- `cols-3` para un diseño a 3 columnas, se combina con los contenedores `left`, `center` y `right`.
- `rows-2` para un diseño a 2 filas, se combina con los contenedores `top` y `bottom`.

---

<!-- _class: split debug -->

# Layouts

## Diseño a 3 filas

### Split

::: top
Fila superior (Se ajusta al contenido)
:::
::: left
Columna izquierda

```js
var body = document.querySelector("body");
body.style.backgroundColor = "red";
body.style.color = "white";
```

:::
::: right
Columna derecha

Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repudiandae voluptatibus rerum sit, praesentium dignissimos ratione molestias laborum vel! Iure mollitia, omnis nulla quam eum hic sunt. Reprehenderit dolorum accusamus quos.
:::
::: bottom
Fila inferior (Se ajusta al contenido)

Útil para algún contenido breve de cierre.

:::

---

<!-- _class: cols-2 debug-->

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

<div class="grid grid-cols-3 gap-2">
  <div class="bg-primary text-center rounded py-8">
    <code>primary</code>
  </div>
  <div class="bg-secondary text-center rounded py-8">
    <code>secondary</code>
  </div>
  <div class="bg-inverted text-center rounded py-8">
    <code>inverted</code>
  </div>
</div>

Adicionalmente, se puede aplicar un patrón al color de fondo de la diapositiva para darle un estilo único, con la clase `pattern`.

<div class="grid grid-cols-3 gap-2">
  <div class="bg-primary pattern text-center rounded py-8">
    <code>primary pattern</code>
  </div>
  <div class="bg-secondary pattern text-center rounded py-8">
    <code>secondary pattern</code>
  </div>
  <div class="bg-inverted pattern text-center rounded py-8">
    <code>inverted pattern</code>
  </div>
</div>

---

# Layouts

## Temas

La alineación general de los elementos se mantiene a la izquierda desde la parte superior.

Cada tema se adapta al color de fondo de la diapositiva, y se puede combinar con otros elementos como tablas, citas, listas y bloques de contenido que se adaptan al tema de la diapositiva.

Adicionalmente se puede añadir la clase `centered` para centrar el contenido de la diapositiva.

---

<!-- _class: primary -->

# Estilo `primary`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

- Un item
- Otro más
- Un último item

---

<!-- _class:  primary pattern -->

# Estilo `primary pattern`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

- Un item
- Otro más
- Un último item

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

- Un item
- Otro más
- Un último item

---

<!-- _class: secondary pattern -->

# Estilo `secondary pattern`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

- Un item
- Otro más
- Un último item

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

<!-- _class: inverted -->

# Estilo `inverted`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

- Un item
- Otro más
- Un último item

---

<!-- _class: inverted pattern -->

# Estilo `inverted pattern`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

- Un item
- Otro más
- Un último item

---

<!-- _class: inverted centered-->

# Estilo `inverted centered`

lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
| ------------ | :----------: | -----------: |
| Celda 1      |   Celda 2    |      Celda 3 |
| Celda 4      |   Celda 5    |      Celda 6 |

El texto se centra verticalmente, pero **no** horizontalmente.

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

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

---

<!-- paginate: skip -->
<!-- class: references -->

# Referencias

- Autor (Fecha). _Título del artículo_. <https://www.example.com>

```md
- Autor (Fecha). _Título del artículo_. <https://www.example.com>
```

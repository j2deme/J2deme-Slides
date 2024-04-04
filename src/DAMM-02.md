---
marp: true
title: DAMM - U2 - Desarrollo Multiplataforma
author: Jaime Jesús Delgado Meraz
header: Desarrollo de Aplicaciones Móviles Multiplataforma - U2
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

# Unidad 2 <br> Desarrollo Multiplataforma

## Desarrollo de Aplicaciones Móviles Multiplataforma

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

1. [Diseño de la interfaz de usuario (UI)](#diseño-de-la-interfaz-de-usuario-ui)
2. [Componentes de la interfaz de usuario](#componentes-de-la-interfaz-de-usuario)
3. [Interacción con el usuario (UX)](#interacción-con-el-usuario-ux)
4. [Navegación](#navegación)

---

# Introducción

- Una vez que se han revisado los conceptos básicos de la programación multiplataforma, como las herramientas, lenguajes de programación y entornos que se pueden utilizar para desarrollar aplicaciones móviles multiplataforma es necesario abordar el diseño de la interfaz de usuario.
- La interfaz de usuario (UI) es el punto de contacto entre el usuario y la aplicación, por lo que debe ser intuitiva, fácil de usar y atractiva.
- El diseño de la interfaz de usuario es una de las tareas más importantes en el desarrollo de aplicaciones móviles, ya que una interfaz de usuario bien diseñada puede hacer que una aplicación sea más fácil de usar y más atractiva para los usuarios.

---

# Introducción

- Las interfaces de usuario bien diseñadas son esenciales para el éxito de una aplicación, ya que los usuarios tienden a abandonar las aplicaciones que no son fáciles de usar.
- Adicional al diseño de la interfaz de usuario, es necesario abordar la interacción con el usuario (UX) y la navegación, con el fin de proporcionar una experiencia de usuario óptima.
- La combinación de una interfaz de usuario bien diseñada, una interacción con el usuario intuitiva y una navegación eficiente puede hacer que una aplicación sea más atractiva para los usuarios y aumentar su tasa de retención.

---
<!-- _class: lead -->
# Diseño de la interfaz de usuario (UI)

---

# Diseño de la interfaz de usuario (UI)

> La interfaz de usuario (UI) se define como el medio a través del cual un usuario interactúa con una aplicación o un sitio web.

- La interfaz de usuario es también el punto de contacto entre el usuario y la aplicación.
- Desde las interfaces de consola hasta las interfaces gráficas de usuario (GUI), todas han evolucionado a lo largo de los años para proporcionar una experiencia de usuario más intuitiva y atractiva.
- Actualmente, con la incorporación de las interfaces táctiles y la realidad aumentada, el diseño de la interfaz de usuario se ha convertido en un aspecto crítico del desarrollo de aplicaciones.

---

# Diseño de la interfaz de usuario (UI)

- En el contexto de las aplicaciones móviles, la interfaz de usuario se ha vuelto fundamental para incrementar las tasas de retención, ya que los usuarios tienden a abandonar las aplicaciones que no son fáciles de usar o que no son atractivas visualmente.
- Lo que hace que una interfaz de usuario sea buena o mala es subjetivo, ya que depende de las preferencias de cada usuario, sin embargo, hay ciertos principios de diseño que se pueden seguir para crear una interfaz de usuario que sea considerada buena por la mayoría de los usuarios.
- Estos principios suelen establecerse en los patrones y guías de diseño de las distintas plataformas.

---

# Diseño de la interfaz de usuario (UI)

## Patrones de diseño visual

> Los patrones de diseño visual son un conjunto de reglas y guías que se utilizan para crear una interfaz de usuario atractiva y fácil de usar.

- Se utilizan para establecer la estructura visual de una aplicación, como la disposición de los elementos en la pantalla, el uso de colores, tipografías, iconos, etc.
- Son fundamentales para la creación de interfaces de usuario, ya que proporcionan una estructura visual coherente y predecible que los usuarios pueden entender y utilizar de manera eficiente.

---

# Diseño de la interfaz de usuario (UI)

## Patrones de diseño visual

- Los patrones o guías de diseño visual suelen establecerse por las plataformas de desarrollo, como Android, iOS, Windows, etc.
- Por ejemplo, Android utiliza Material Design, iOS utiliza Human Interface Guidelines y Windows utiliza Fluent Design System.
- Cada uno de estos patrones de diseño visual logra el mismo objetivo, proporcionar una estructura visual coherente.
- Sin embargo, cada uno de ellos tiene sus señas de identidad y características propias.

---

# Diseño de la interfaz de usuario (UI)

## Material Design

- Fue desarrollado por Google en 2014, con el objetivo de proporcionar una estructura visual coherente para las aplicaciones de Android.
- Actualmente, Material Design se utiliza en todas las plataformas de Google (<https://m3.material.io/>).
- Se basa en los conceptos de simplicidad, capas y uso de la metáfora de los materiales y se caracteriza por el uso de colores vibrantes, tipografías grandes, tarjetas y sombras.
- Material Design es uno de los patrones de diseño visual más populares y se utiliza en una gran cantidad de aplicaciones de Android y la web.

---

![bg fit](../src/assets/DAMM/material-design-kit.png)

---

# Diseño de la interfaz de usuario (UI)

## Human Interface Guidelines

- Fue desarrollado por Apple en 1984, con el objetivo de proporcionar una estructura visual coherente para las primeras aplicaciones de Mac OS.
- Con la llegada del iPhone en 2007, se adaptaron para las aplicaciones de iOS, pasando por conceptos como el _skeumorfismo_ y el _flat design_ y se han convertido en un estándar para el diseño de interfaces de usuario en todas las plataformas de Apple (<https://developer.apple.com/design/>).
- Se basa en una jerarquía visual clara, el uso del espacio en blanco, una tipografía legible y colores claros.

---

![bg cover](../src/assets/DAMM/human-interface-guidelines.jpg)

---

# Diseño de la interfaz de usuario (UI)

## Fluent Design System

- De origen más reciente, fue propuesto por Microsoft en 2017, con el objetivo de proporcionar una estructura visual coherente para las aplicaciones de Windows 10 (<https://fluent2.microsoft.design/>).
- Se basa en el uso de materiales acrílicos, profundidad y transiciones animadas.
- Busca que sus interfaces evoquen una sensación de movimiento y fluidez.
- Su paleta de colores es un tanto más vibrante que la de Human Interface Guidelines, pero no tanto como la de Material Design.

---

![bg cover](../src/assets/DAMM/fluent-design-system.jpeg)

---

# Diseño de la interfaz de usuario (UI)

## Comparación de patrones de diseño visual

| Característica | Material Design | Human Interface Guidelines | Fluent Design System |
|----------------|-----------------|----------------------------|----------------------|
| Enfoque | Simplicidad, capas, materiales | Claridad, consistencia, facilidad de uso | Adaptabilidad, fluidez, movimiento |
| Elementos clave | Colores vibrantes, tipografía robusta, tarjetas, sombras |  Jerarquía visual, espacio en blanco, tipografía legible | Material acrílico, profundidad, transiciones animadas |
| Ejemplos | Aplicaciones de Google | iOS y aplicaciones nativas | Windows 11 y Office 365 |

---

# Diseño de la interfaz de usuario (UI)

## Comparación de patrones de diseño visual

| Característica | Material Design | Human Interface Guidelines | Fluent Design System |
|----------------|-----------------|----------------------------|----------------------|
| Tipografía | Roboto, Noto | San Francisco (SF) | Segoe UI |
| Colores | Paleta de colores vibrantes | Paleta de colores claros | Paleta de colores vibrantes |
| Iconos | Material Icons | SF Symbols | Segoe MDL2 Assets |

---

# Diseño de la interfaz de usuario (UI)

## Otras consideraciones

- En general, no se recomienda mezclar patrones de diseño visual, ya que puede resultar en una interfaz de usuario incoherente y confusa.
- Cada patrón de diseño ofrece su propio conjunto de elementos visuales, como colores, tipografías, iconos, etc., que se deben utilizar de manera coherente en toda la aplicación.
- De hecho, durante algunos años, las tiendas de aplicaciones llegaron a rechazar aplicaciones que no seguían los patrones de diseño visual de sus plataformas; actualmente dejan más libertad a los desarrolladores, pero siguen recomendando seguirlos.

---

<!-- _class: inverted -->

# Nota

- Considerando que para fines didácticos se tomará como base el framework de desarrollo Flutter, es importante mencionar que este se basa en _Material Design_, por lo que los conceptos y principios de diseño de interfaz de usuario que se revisarán a continuación tomarán como base este patrón de diseño visual.
- Es importante mencionar que los conceptos y principios de diseño de interfaz de usuario son aplicables a cualquier patrón de diseño visual.
- Adicionalmente, Flutter también soporta otros patrones de diseño como el _Human Interface Guidelines_.

---
<!-- _class: lead -->
# Componentes de la interfaz de usuario

---

# Componentes de la interfaz de usuario

- En Flutter, la interfaz de usuario se construye utilizando **widgets**.
  > Un widget es un componente visual o funcional que se utiliza para construir la interfaz de usuario de una aplicación.
- Se utilizan principalmente para construir la interfaz de usuario de una aplicación, como botones, campos de texto, listas, tarjetas, etc.
- Es importante entender que en Flutter, todo es un widget, por lo que los mismos, no se limitan a los componentes visuales, sino que también incluyen elementos como el diseño, el espaciado, la alineación, etc.

---

# Componentes de la interfaz de usuario

Los widgets en Flutter se dividen en dos categorías principales:

Widgets de diseño
: Se utilizan para construir la estructura visual de la aplicación, como el diseño, el espaciado, la alineación, etc.
  
Widgets funcionales
: Se utilizan para construir los componentes visuales de la aplicación, como botones, campos de texto, listas, tarjetas, etc.

---

# Componentes de la interfaz de usuario

- La estructura básica de una aplicación en Flutter está compuesta por un árbol de widgets.

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Hello App'),
        ),
        body: Center(
          child: Text('Hola Mundo!'),
        ),
      ),
    );
  }
}
```

---

# Componentes de la interfaz de usuario

## Widgets de diseño

- Los widgets de diseño se utilizan para construir la estructura visual de la aplicación, pero no tienen una representación visual en la pantalla.
  - Column
  - Row
  - Container
  - Padding
  - Center
  - Align
  - Stack
  - Scaffold

---

## Widgets de diseño

:::: flex
::: col 1/2 px-2

### Column

- Se utiliza para organizar los widgets en una columna vertical.

```dart
Column(
  children: [
    Text('Item 1'),
    Text('Item 2'),
    Text('Item 3'),
  ],
)
```

:::

::: col 1/2 px-2

### Row

- Se utiliza para organizar los widgets en una fila horizontal.

```dart
Row(
  children: [
    Text('Item 1'),
    Text('Item 2'),
    Text('Item 3'),
  ],
)
```

:::
::::

---

## Widgets de diseño

:::: flex
::: col 1/2 px-2

### Container

- Se utiliza para _contener_ otros widgets y aplicar estilos.

```dart
Container(
  color: Colors.blue,
  child: Text('Hola Mundo!'),
)
```

:::

::: col 1/2 px-2

### Padding

- Se utiliza para agregar relleno a un widget.

```dart
Padding(
  padding: EdgeInsets.all(16.0),
  child: Text('Hola Mundo!'),
)
```

:::
::::

---

## Widgets de diseño

:::: flex
::: col 1/2 px-2

### Center

- Se utiliza para centrar un widget en la pantalla, el centrado es tanto vertical como horizontal.

```dart
Center(
  child: Text('Hola Mundo!'),
)
```

:::

::: col 1/2 px-2

### Align

- Se utiliza para alinear un widget en la pantalla.

```dart
Align(
  alignment: Alignment.center,
  child: Text('Hola Mundo!'),
)
```

- La propiedad `alignment` puede tomar valores como `Alignment.topLeft`, `Alignment.bottomRight`, etc.

:::
::::

---

## Widgets de diseño

:::: flex

::: col 1/2 px-2

### Stack

- Se utiliza para apilar widgets uno encima del otro.

```dart
Stack(
  children: [
    Container(
      color: Colors.blue,
      height: 100,
      width: 100,
    ),
    Container(
      color: Colors.red,
      height: 50,
      width: 50,
    ),
  ],
)
```

:::

::: col 1/2 px-2

### Scaffold

- Se utiliza para crear la estructura básica de una aplicación, como la barra de aplicación, la barra de navegación, etc.

```dart
Scaffold(
  appBar: AppBar(
    title: Text('Hello App'),
  ),
  body: Center(
    child: Text('Hola Mundo!'),
  ),
)
```

:::
::::

---

## Widgets de diseño

### Ejemplo 1: Un cara del cubo Rubik

- Se inicia con una estructura básica utilizando el widget `Scaffold`.

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Cubo Rubik'),
        ),
        body: Center(
          child: Text('Cara 1'),
        ),
      ),
    );
  }
}
```

---

## Widgets de diseño

### Ejemplo 1: Un cara del cubo Rubik

![bg right:40% fit](../src/assets/DAMM/Rubiks_cube.svg)

- Para poder crear una cara del cubo, se combinarán los widgets `Column` y `Row`, para poder organizar la estructura en una columna vertical y 3 filas horizontales, que a su vez contengan 3 contenedores cada una.
- Igualmente se pueden combinar otros widgets como `Container` y `Center` para agregar tamaño, color y alineación a los elementos.

---

## Widgets de diseño

### Ejemplo 1: Un cara del cubo Rubik

```dart
Column(
  children: [
    Row(
      children: [
        Container(color: Colors.green, height: 100, width: 100),
        Container(color: Colors.blue, height: 100, width: 100),
        Container(color: Colors.white, height: 100, width: 100),
      ],
    ),
    // ... (2 filas más)
  ],
)
```

---

## Widgets de diseño

### Ejemplo 1: Un cara del cubo Rubik

```dart
// Filas 2 y 3
Column(
  children: [
    // ... (fila 2)
    Row(
      children: [
        Container(color: Colors.blue, height: 100, width: 100),
        Container(color: Colors.orange, height: 100, width: 100),
        Container(color: Colors.red, height: 100, width: 100),
      ],
    ),
    Row(
      children: [
        Container(color: Colors.yellow, height: 100, width: 100),
        Container(color: Colors.white, height: 100, width: 100),
        Container(color: Colors.blue, height: 100, width: 100),
      ],
    ),
  ],
)
```

---

## Widgets de diseño

### Ejemplo 1: Un cara del cubo Rubik

- Adicionalmente, se puede entre otras opciones, agregar un estilo a los contenedores, como bordes redondeados, sombras, etc.

```dart
Container(
  decoration: BoxDecoration(
    color: Colors.green,
    borderRadius: BorderRadius.circular(10),
    border: Border.all(
      color: Colors.black.opacity(0.8),
      width: 2,
    ),
  ),
  height: 100,
  width: 100,
)
```

---

## Widgets de diseño

### Ejemplo 2: Una calculadora

- Nuevamente se inicia creando una estructura básica de una aplicación, utilizando el widget `Scaffold`.

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Calculadora'),
        ),
        body: Center(
          child: Text('0'),
        ),
      ),
    );
  }
}
```

---

## Widgets de diseño

### Ejemplo 2: Una calculadora

- Para este ejemplo también se combinarán los widgets `Column` y `Row`.

```dart
Column(
  children: [
    Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(
          '1234567890',
          style: TextStyle(
            fontSize: 25,
            fontWeight: FontWeight.bold,
          ),
        ),
      ],
    ),
    // ... 
  ],
)
```

![bg right:40% fit](../src/assets/DAMM/Calculadora.jpg)

---

## Widgets de diseño

### Ejemplo 2: Una calculadora

- En este caso, se utilizará el widget `ElevatedButton` para crear los botones de la calculadora.
  
```dart
ElevatedButton(child: Text('7'), onPressed: () { /* ... */ }),
```

- El atributo `onPressed` es un _callback_ que se ejecuta cuando el botón es presionado, por el momento no se implementará ninguna acción, sin embargo, es necesario agregarlo para que el botón funcione.

---

## Widgets de diseño

### Ejemplo 2: Una calculadora

:::: flex
::: col 1/2 px-2

```dart
// Teclado numérico
Column(
  children: [
    // Fila del display
    Row(
      children: [
        //.. ElevatedButton 7, 8, 9, /
      ],
    ),
    Row(
      children: [
        //.. ElevatedButton 4, 5, 6, x
      ],
    ),
    Row(
      children: [
        //.. ElevatedButton 1, 2, 3, -
      ],
    ),
  ],
),
```

:::
::: col 1/2 px-2

- Se utiliza el atributo `mainAxisAlignment.center` para alinear los botones en el centro de la fila.
- Igualmente, se añade una fila para los símbolos: `.`, `0`, `=` y `+`.

:::
::::

---

## Widgets de diseño

### Ejemplo 2: Una calculadora

- Para diferenciar los botones de las operaciones, se puede utilizar el atributo `style` para cambiar los colores de los botones.

```dart
ElevatedButton(
  child: Text('/'),
  style: ElevatedButton.styleFrom(
    foregroundColor: Theme.of(context).colorScheme.onPrimary,
    backgroundColor: Theme.of(context).colorScheme.primary,
  ),
  onPressed: () { /* ... */ },
),
```

- La propiedad `styleFrom` toma como referencia el tema de la aplicación, por lo que se puede utilizar para cambiar los colores de los botones de acuerdo al tema.

---

# Componentes de la interfaz de usuario

## Widgets de diseño

- Los widgets de diseño también se utilizan para aplicar estilos a los componentes visuales de la aplicación, como colores, tipografías, bordes, sombras, etc.
- _P.e._
  - TextStyle, FontWeight, FontStyle
  - BoxDecoration, Color, Gradient, BoxShadow
  - Border, BorderRadius, BorderSide
- Igualmente incluyen widgets como `ListView`, `GridView`, `SingleChildScrollView`, `Expanded`, `Spacer`, etc.

---

# Componentes de la interfaz de usuario

## Widgets funcionales

- Los widgets funcionales se utilizan para construir los componentes visuales de la aplicación, como botones, campos de texto, listas, tarjetas, etc.
  - Text
  - Image
  - Icon
  - Button
  - TextField
  - Checkbox
  - Radio
  - Switch
  - Slider
  - DatePicker
  - TimePicker
- Snackbar
- Dialog
- BottomSheet
:::
::::

---

## Widgets funcionales

:::: flex
::: col 1/2 px-2

### Text

- Se utiliza para mostrar texto en la pantalla.

```dart
Text('Hola Mundo!')

// Puede aplicarse estilo
Text(
  'Hola Mundo!',
  style: TextStyle(
    fontSize: 25,
    fontWeight: FontWeight.bold,
  ),
)
```

:::
::: col 1/2 px-2

### Icon

- Se utiliza para mostrar iconos en la pantalla.

```dart
Icon(Icons.star)

// Puede aplicarse estilo
Icon(
  Icons.star,
  color: Colors.yellow,
  size: 50,
)
```

- Los iconos default son de [Material Design](https://fonts.google.com/icons), pero se pueden utilizar otros conjuntos de iconos.
:::
::::

---

## Widgets funcionales

:::: flex
::: col 1/2 px-2

### Image

- Se utiliza para mostrar imágenes locales y remotas en la pantalla.

```dart
Image.asset('assets/logo.png')

Image.network('https://example.com/logo.png')
```

- Las imágenes pueden ser de cualquier formato soportado por Flutter, como `PNG`, `JPEG`, `GIF`, etc.

:::
::: col 1/2 px-2

- Las imágenes locales deben estar dentro de la carpeta `assets` y deben declararse en el archivo `pubspec.yaml`.

```bash
Proyecto
├──📂 android
├──📂 ios
├──📂 lib
├──📂 assets # Se debe crear
│   └── logo.png
└── pubspec.yaml
```

```yaml
flutter:
  assets:
    - assets/logo.png
```

:::
::::

---

## Widgets funcionales

### Button

- Flutter proporciona varios tipos de botones, como `ElevatedButton`, `TextButton`, `OutlinedButton`, `IconButton`, etc., cada uno con su propio estilo y comportamiento.

:::: flex
::: col 1/2 px-2

```dart
ElevatedButton(
  child: Text('Aceptar'),
  onPressed: () { /* ... */ },
)
```

```dart
TextButton(
  child: Text('Cancelar'),
  onPressed: () { /* ... */ },
)
```

:::
::: col 1/2 px-2

```dart
OutlinedButton(
  child: Text('Cancelar'),
  onPressed: () { /* ... */ },
)
```

```dart
IconButton(
  icon: Icon(Icons.star),
  onPressed: () { /* ... */ },
)
```

:::
::::

---

## Widgets funcionales

### Button

- Los botones también pueden aplicar estilos, como colores, bordes, sombras, etc.

```dart
ElevatedButton(
  child: Text('Aceptar'),
  style: ElevatedButton.styleFrom(
    foregroundColor: Colors.blue,
    backgroundColor: Colors.white,
  ),
  onPressed: () { /* ... */ },
)
```

- Flutter también incluye otros widgets de botones como `FloatingActionButton`, `PopupMenuButton`, `DropdownButton`, etc.

---

## Widgets funcionales

:::: flex
::: col 1/2 px-2

### TextField

- Se utiliza para obtener texto del usuario.

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Nombre',
    hintText: 'Escribe tu nombre',
  ),
)

TextField(
  decoration: InputDecoration(
    labelText: 'Contraseña',
    hintText: 'Escribe tu contraseña',
  ),
  obscureText: true,
)
```

:::
::: col 1/2 px-2

- También es común utilizar `TextFormField` para obtener texto del usuario y validar la entrada.

```dart
TextFormField(
  decoration: InputDecoration(
    labelText: 'Correo',
    hintText: 'Escribe tu correo',
  ),
  validator: (value) {
    if (value.isEmpty) {
      return 'El correo es requerido';
    }
    return null;
  },
)
```

:::
::::

---

## Widgets funcionales

:::: flex
::: col 1/2 px-2

### Checkbox

- Se utiliza para activar o desactivar una opción.

```dart
Checkbox(
  value: true,
  checkColor: Colors.white,
  onChanged: (value) { /* ... */ },
)
```

- Si se requiere una etiqueta, se puede utilizar `CheckboxListTile`.

```dart
CheckboxListTile(
  title: Text('Acepto los términos y condiciones'),
  value: true,
  onChanged: (value) { /* ... */ },
)
```

:::
::: col 1/2 px-2

- Para grupos de opciones, se puede utilizar una lista de `CheckboxListTile`.

```dart
List<CheckboxListTile> opciones = [
  CheckboxListTile(
    title: Text('Opción 1'),
    value: true,
    onChanged: (value) { /* ... */ },
  ),
  CheckboxListTile(
    title: Text('Opción 2'),
    value: false,
    onChanged: (value) { /* ... */ },
  ),
];
```

:::
::::

---

## Widgets funcionales

:::: flex
::: col 1/2 px-2

### Radio

- Se utiliza para seleccionar una opción de un grupo.

```dart
enum tamanio { chico, mediano, grande }

Radio(
  title: 'Chico',
  value: tamanio.chico,
  groupValue: tamanio,
  onChanged: (value) { /* ... */ },
)
```

- Si se requiere una etiqueta, se puede utilizar `RadioListTile`.

:::
::: col 1/2 px-2

- Si se requiere una etiqueta, se puede utilizar `RadioListTile`.

```dart
RadioListTile(
  title: Text('Chico'),
  subtitle: Text('10 oz'),
  value: tamanio.chico,
  groupValue: tamanio,
  onChanged: (value) { /* ... */ },
)
```

:::
::::

---

## Widgets funcionales

:::: flex
::: col 1/2 px-2

### Switch

- Se utiliza para activar o desactivar una opción.

```dart
Switch(
  value: true,
  onChanged: (value) { /* ... */ },
)
```

- Si se requiere una etiqueta, se puede utilizar `SwitchListTile`.

```dart
SwitchListTile(
  title: Text('Activar notificaciones'),
  value: true,
  onChanged: (value) { /* ... */ },
)
```

:::
::: col 1/2 px-2

### Slider

- Se utiliza para seleccionar un valor de un rango.

```dart
Slider(
  value: 50,
  min: 0,
  max: 100,
  divisions: 10,
  onChanged: (value) { /* ... */ },
)
```

:::
::::

---
<!-- _class: inverted -->

# WidgetListTile

- Los widgets `CheckboxListTile`, `RadioListTile` y `SwitchListTile` son ejemplos de `ListTile`.
- `ListTile` es un widget que se utiliza para mostrar información en una lista, como un título, un subtítulo, un icono, etc.
- Además de proporcionar una estructura visual coherente, incrementa el área de interacción del usuario con el respectivo widget.
- Se sugiere utilizar la versión `ListTile` de los widgets `Checkbox`, `Radio` y `Switch` para proporcionar una mejor experiencia de usuario.

---

## Widgets funcionales

### DatePicker

- Se inicia con un _callback_ que se ejecuta desde un TextField o un botón.

:::: flex
::: col 1/2 px-2

```dart
TextFormField(
  decoration: InputDecoration(
    labelText: 'Fecha de nacimiento',
    hintText: 'Selecciona tu fecha de nacimiento',
  ),
  onTap: () {
    // Se ejecuta el callback
  },
)
```

:::
::: col 1/2 px-2

```dart
showDatePicker(
  context: context,
  initialDate: DateTime.now(),
  firstDate: DateTime(DateTime.now().year - 1),
  lastDate: DateTime(DateTime.now().year + 1),
  builder: (BuildContext context, Widget child) {
    return Theme(
      data: ThemeData.light(),
      child: child,
    );
  },
);
```

:::
::::

---

## Widgets funcionales

### TimePicker

- Se utiliza de manera similar al `DatePicker`, para seleccionar una hora.

```dart
showTimePicker(
  context: context,
  initialTime: TimeOfDay.now(),
  builder: (BuildContext context, Widget child) {
    return Theme(
      data: ThemeData.light(),
      child: child,
    );
  },
);
```

- Ambos _pickers_ son diálogos que se muestran en la pantalla, por lo que se deben utilizar en conjunto con el método `showDatePicker` y `showTimePicker`.

---

## Widgets funcionales

### Snackbar

- Se utiliza para mostrar mensajes temporales en la pantalla, se muestra en la parte inferior de la pantalla y desaparece después de un tiempo.

```dart
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: Text('Mensaje temporal'),
  ),
);
```

- El método `showSnackBar` se utiliza para mostrar el _snackbar_ en la pantalla, se debe utilizar en conjunto con el widget `Scaffold`.

---

## Widgets funcionales

### Snackbar

```dart
Scaffold(
  appBar: AppBar(
    title: Text('Snackbar'),
  ),
  body: Center(
    child: ElevatedButton(
      child: Text('Mostrar Snackbar'),
      onPressed: () {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Mensaje temporal'),
          ),
        );
      },
    ),
  ),
)
```

---

## Widgets funcionales

### Dialog

- Se utiliza para mostrar un diálogo centrado en la pantalla.

```dart
showDialog(
  context: context,
  builder: (BuildContext context) {
    return AlertDialog(
      title: Text('Título del diálogo'),
      content: Text('Contenido del diálogo'),
      actions: [
        TextButton(
          child: Text('Aceptar'),
          onPressed: () {
            Navigator.of(context).pop();
          },
        ),
      ],
    );
  },
);
```

---

## Widgets funcionales

### Dialog

- Los diálogos se utilizan para mostrar mensajes importantes al usuario, como confirmaciones, alertas, etc.
- El método `showDialog` se utiliza para mostrar el diálogo en la pantalla, se debe utilizar en conjunto con el widget `Scaffold`.
- El diálogo puede contener cualquier widget, como texto, botones, campos de texto, listas, etc.
- Los diálogos tienen la característica de ser modales, es decir, bloquean la interacción con el resto de la aplicación hasta que se cierran.

---

## Widgets funcionales

### BottomSheet

- Se utiliza para mostrar un diálogo que se desliza desde la parte inferior de la pantalla.

```dart
showModalBottomSheet(
  context: context,
  builder: (BuildContext context) {
    return Container(
      child: Text('Contenido del bottom sheet'),
    );
  },
);
```

- El método `showModalBottomSheet` se utiliza para mostrar el _bottom sheet_ en la pantalla, se debe utilizar en conjunto con el widget `Scaffold`.

---

## Widgets funcionales

### BottomSheet

```dart
Scaffold(
  appBar: AppBar(
    title: Text('BottomSheet'),
  ),
  body: Center(
    child: ElevatedButton(
      child: Text('Mostrar BottomSheet'),
      onPressed: () {
        showModalBottomSheet(
          context: context,
          builder: (BuildContext context) {
            return Container(
              child: Text('Contenido del bottom sheet'),
            );
          },
        );
      },
    ),
  ),
)
```

---

# Componentes de la interfaz de usuario

- Los widgets funcionales también se utilizan para manejar eventos, como toques, deslizamientos, cambios, etc.
- Además de los widgets revisados, Flutter proporciona una gran cantidad de widgets funcionales, como `PopupMenuButton`, `DropdownButton`, `Tooltip`, `Stepper`, `ExpansionPanel`, `Chip`, `TabBar`, `Drawer`, `AppBar`, etc., cada uno con su propio estilo y comportamiento.
- Los widgets funcionales también se utilizan para manejar la navegación, como botones de navegación, barras de navegación, pestañas, cajones de navegación, etc.

---
<!-- _class: lead -->
# Interacción con el usuario (UX)

---

# Interacción con el usuario (UX)

- Eventos
- Respuesta a usuarios

---
<!-- _class: lead -->
# Navegación

---

# Navegación

- Métodos de navegación
- Compartir información entre vistas

---

<!-- _class: inverted -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

# Guía para agentes automatizados (LLMs) que interactúan con J2deme-Slides

## Propósito

Este documento sirve como referencia para modelos LLM (agentes automatizados) que interactúen con el repositorio "J2deme-Slides". Describe la intención del proyecto, archivos y rutas clave, contratos de entrada/salida para acciones comunes, comandos útiles para desarrollo y pruebas, restricciones de seguridad y ejemplos de prompts que el agente puede y no puede ejecutar.

## Resumen del proyecto

J2deme-Slides es una colección de plantillas, plugins y utilidades para crear y exportar presentaciones Markdown usando Marp. Contiene:

- Un motor personalizado `engine.js` (plugins `markdown-it`) que extiende la sintaxis Markdown.
- Una CLI en Python `slides.py` para crear, gestionar y exportar presentaciones.
- Archivos fuente `src/` con plantillas, estilos y las presentaciones en formato Markdown.
- `package.json` controla dependencias Node y la configuración de Marp.

## Archivos y rutas clave

- `engine.js` — Plugin/engine para Marp. Punto de entrada definido en `package.json`.
- `slides.py` — CLI Python para crear/gestionar/exportar presentaciones.
- `package.json` — Dependencias Node y configuración global de Marp.
- `requirements.txt` — Paquetes Python requeridos (questionary, rich, click).
- `src/` — Carpeta principal de contenidos: `.md` (presentaciones), `assets/`, `styles/`, `templates/`.
- `src/subjects.json` — Datos estructurados de materias/unidades que la CLI puede usar para generar slides.
- `src/templates/Clase.md`, `src/templates/Ponencia.md` — Plantillas base para generación.
- `dist/` — (Salida prevista) archivos exportados (PDF, HTML, imágenes).

## Estructura de las presentaciones

- Cada presentación es un archivo Markdown (`.md`) en `src/`, dividido en slides por separadores `---`.
- Cada presentación incluye metadatos YAML al inicio para configuración (título, autor, tema, etc.) estos metadatos son procesados por Marp y `engine.js` y se utilizan para personalizar la apariencia y funcionalidad de la presentación.
- Los metadatos YAML se generan automáticamente al crear nuevas presentaciones usando `slides.py` y pueden ser editados manualmente para ajustes específicos.
- Los slides pueden contener código, imágenes y otros elementos multimedia, que son procesados por Marp durante la exportación.
- Los slides pueden tener diferentes estructuras que se especifican mediante decoradores (comentarios HTML como `<!-- _class: lead -->`), que son interpretados por `engine.js` para aplicar estilos o comportamientos específicos (por ejemplo, secciones destacadas, listas numeradas, etc.).

### Estructuras comunes en slides

#### cover

- Uso: `<!-- _class: cover -->`
- Propósito: Indica que el slide es una portada o título principal.
- Efecto: Aplica un estilo de portada (tipografía grande, centrado, etc.).
- Solo puede haber un slide con esta clase por presentación.
- Su estructura clásica incluye:

```markdown
<!-- _class: cover -->
<!-- _paginate: false -->

# {Nombre de la unidad}

## {Nombre de la materia}

Dr. Jaime Jesús Delgado Meraz

### Unidad {01, 02, ...}

#### {Clave de la materia}

<img class="logo" alt="TecNM" src="../src/assets/Logo-TECNM.svg" />

---
```

#### toc

- Uso: `<!-- _class: toc -->`
- Propósito: Indica que el slide es una tabla de contenidos (TOC).
- Efecto: Aplica un estilo de tabla de contenidos (lista de secciones, numerada o con viñetas).
- Su estructura clásica incluye:

```markdown
<!-- _class: toc -->

# Contenidos

1. {Sección 1}
2. {Sección 2}
3. {Sección 3}

---
```

#### lead

- Uso: `<!-- _class: lead -->`
- Propósito: Indica que el slide es una diapositiva de introducción / título / sección.
- Efecto: Aplica un estilo destacado (tipografía más grande, centrado, etc.).
- Su estructura clásica incluye:

```markdown
<!-- _class: lead -->

# {Título del slide}

## {Subtítulo o descripción opcional}

---
```

#### cols-2

- Uso: `<!-- _class: cols-2 -->`
- Propósito: Divide el slide en dos columnas simétricas.
- Efecto: Aplica un diseño de dos columnas para organizar el contenido.
- La segunda columna se usa regularmente para imágenes, gráficos, listas o snippets cortos de código (no más de 5 líneas).
- Su estructura clásica incluye:

```markdown
<!-- _class: cols-2 -->

::: left
{Contenido de la columna izquierda}
:::
::: right
{Contenido de la columna derecha}
:::

---
```

#### cols-3

- Uso: `<!-- _class: cols-3 -->`
- Propósito: Divide el slide en tres columnas simétricas.
- Efecto: Aplica un diseño de tres columnas para organizar el contenido.
- Su estructura clásica incluye:

```markdown
<!-- _class: cols-3 -->

::: left
{Contenido de la columna izquierda}
:::
::: center
{Contenido de la columna central}
:::
::: right
{Contenido de la columna derecha}
:::

---
```

#### Callouts / Admonitions (note, warning, primary, centered, etc.)

- Uso: `::: note`, `::: warning`, `::: quote`, o clases adicionales `<!-- _class: primary centered -->` en combinación con bloque de cita.
- Propósito: Crear bloques destacados (notas, advertencias, citas en foco) con estilo consistente en la plantilla.
- Ejemplo clásico:

```markdown
::: note
Texto breve de nota que se muestra con estilo y una pequeña cinta lateral.
:::

::: warning
Texto de advertencia que se destaca visualmente.
:::

<!-- _class: primary centered -->

> _Cita en foco para una diapositiva independiente_

---
```

Notas:

- Los bloques `::: note` y `::: warning` son soportados por el motor `engine.js` y aplican estilos CSS específicos.
- Para citas en foco se recomienda usar la directiva `_class` con `primary centered` y un bloque de cita `>` para centrar y destacar la cita.

#### Flex layout y columnas avanzadas

- Uso: `::::: flex` junto con `:::: col <fracción> [clases]` para layouts flexibles y responsivos.
- Propósito: Permitir layouts personalizados con columnas de anchos relativos y espaciado.
- Ejemplo:

```markdown
::::: flex
:::: col 1/2 px-2

Contenido de la columna 1

::::
:::: col 1/2 px-2

Contenido de la columna 2

::::
:::::

---
```

Notas:

- Esta sintaxis es utilizada en `Playground.md` para demostrar combinaciones de columnas con padding (`px-2`) y funciona bien para comparaciones lado a lado.

#### Directivas e indicaciones para imágenes

- Sintaxis enriquecida: `![bg right:40% w:50%](ruta)` o `![#l]` / `![#c]` / `![#r]` para imágenes flotantes.
- Propósito: ajustar posición, tamaño y comportamiento (fondo, cover, fit) directamente desde Markdown.
- Opciones comunes:

  - `bg` — coloca la imagen como fondo de la diapositiva.
  - `right`, `left` — posición relativa (puede combinarse con `w:50%` para ancho).
  - `w:<n>` o `w:<n>%` — ancho absoluto o porcentual.
  - `h:<n>` — altura en píxeles.
  - `cover`, `fit` — modos de ajuste.
  - `[#l]`, `[#c]`, `[#r]` — atajos para imágenes flotantes a la izquierda/centro/derecha.

Ejemplos:

```markdown
![bg right:30% w:50%](../src/assets/pattern-alt.svg)

![#l](https://unsplash.it/200/100)

![w:100](../src/assets/avatar.png)

---
```

Notas:

- Estas directivas son interpretadas por el `engine.js` para generar los atributos y estilos adecuados en la salida HTML/PDF.

#### Inline notes y etiquetas especiales

- Uso: tag inline `<note>...</note>` para pequeñas marcas en una línea o dentro de párrafos.
- Propósito: proporcionar una nota embebida que se estiliza de forma discreta.

Ejemplo:

```markdown
Texto con nota <note>\*</note>
```

#### Paginado y saltos (paginate)

- Uso en portada u otras diapositivas: `<!-- _paginate: false -->` para desactivar la paginación en una diapositiva; `<!-- paginate: skip -->` para saltar en el índice/tabla de contenidos.
- Propósito: controlar la numeración y el comportamiento de paginación en slides específicos.

Ejemplo:

```markdown
<!-- _paginate: false -->

# Portada

---

<!-- paginate: skip -->
<!-- class: references -->
```

Notas:

- Usar estas directivas en slides tipo portada o referencias ayuda a mantener la numeración correcta en el material exportado.

## Contrato (inputs/outputs) — acciones comunes

1. Exportar una presentación a PDF

   - Input: nombre del archivo sin extensión (ej. "FP-01")
   - Acción: ejecutar Marp (o `npx marp`) sobre `src/{slide}.md` con flags para PDF
   - Output: archivo `{dist}/{slide}.pdf` si éxito. Mensaje de error si falla.

2. Crear una nueva presentación desde JSON

   - Input: selección de `subjects.json` y unidad
   - Acción: Combinar plantilla `Clase.md` o `Ponencia.md` con datos y escribir `src/{filename}.md`
   - Output: nuevo archivo Markdown en `src/` y mensaje de confirmación.

3. Previsualizar una presentación
   - Input: nombre del archivo
   - Acción: ejecutar `marp --preview` con `--html` para generar vista previa local
   - Output: servidor local o archivo HTML en `dist/`

## Comandos y utilidades útiles

(El agente puede sugerirlos o ejecutarlos si se le autoriza a operar en terminal.)

- npm install — instalar dependencias Node y crear lockfile
- npx marp src/<slide>.md --output dist/<slide>.pdf --allow-local-files --pdf-outlines --pdf-notes
- python slides.py --pdf <slide>
- python slides.py --preview <slide>
- node engine.js (no es un binario; `engine.js` se usa desde Marp)

Scripts npm útiles añadidos al repositorio:

- `npm run slides` — ejecuta la CLI Python (`python slides.py`) para interactuar con el gestor de slides.
- `npm run slides:pdf -- <slide>` — ejecuta `python slides.py --pdf <slide>` (usa `--` para pasar argumentos después de npm).
- `npm run slides:preview -- <slide>` — ejecuta `python slides.py --preview <slide>`.
- `npm run install:all` — instala dependencias Node y Python (ejecuta `npm install && pip install -r requirements.txt`).
- `npm run check:shiki` — verifica si `markdown-it-shiki` está instalado en node_modules.

## Guía de seguridad y límites

- No exfiltrar secretos. Evitar leer archivos fuera del repositorio.
- No ejecutar comandos de red (curl, git push a repos remotos) sin autorización explícita.
- No instalar paquetes globales sin permiso del mantenedor.
- Evitar cambiar código de producción sin pruebas o sin permiso explícito.
- Los agentes deben abstenerse de modificar grandes cantidades de archivos sin aprobación humana.

## Reglas para ediciones automáticas

- Hacer cambios atómicos y documentados: un cambio lógico por commit/PR.
- Añadir tests o validaciones mínimas si se cambia comportamiento crítico (ej. generación de slides).
- Ejecutar validaciones locales (lint/sintaxis/tests) luego de editar. Reportar fallos.
- Siempre actualizar `AGENTS.md` si se introducen nuevas convenciones o scripts.

## Ejemplos de uso y notas sobre el plugin Shiki

---

- Para previsualizar slides sin cargar `shiki` (modo recomendado durante edición):

```powershell
$env:MARP_PREVIEW = 'true'
npx marp --preview src/YourSlide.md
```

- Para exportar a PDF y permitir que `engine.js` cargue `markdown-it-shiki` (resaltado con Shiki):

```powershell
Remove-Item Env:\MARP_PREVIEW -ErrorAction SilentlyContinue
npx marp src/YourSlide.md --output dist/YourSlide.pdf --allow-local-files --pdf-outlines --pdf-notes
```

O, usando los scripts npm añadidos:

```powershell
npm run slides:pdf -- YourSlide
```

Nota: `engine.js` detecta flags comunes (`--preview`, `--watch`, `--server`, `--serve`) y las variables de entorno `MARP_PREVIEW` o `MARP_WATCH`. Si detecta modo preview, evita cargar `markdown-it-shiki` para reducir errores por renderizado frecuente.

## Preguntas frecuentes que el agente puede responder automáticamente

- "¿Qué dependencias requiere el proyecto?" → Revisar `package.json` y `requirements.txt`.
- "¿Dónde están las plantillas?" → `src/templates/`.
- "¿Cómo genero un PDF de la presentación X?" → Proveer comando `npx marp` o `python slides.py --pdf X`.
- "¿Cómo previsualizo la presentación X?" → Proveer comando `npx marp` o `python slides.py --preview X`.
- "¿Cómo creo una nueva presentación para la unidad Y?" → Usar `slides.py` con datos de `subjects.json`.

## Ejemplos de prompts (para LLMs)

- Permitidos (responsable):

  - "Crea un PR que añada un script `npm run build` en `package.json` para exportar todas las slides a PDF usando Marp. Añade también un `README` breve con el comando."
  - "Corrige el bug en `slides.py` donde se llama `main` en vez de `main()` y añade una prueba sintáctica rápida."

- No permitidos (sin aprobación humana):
  - "Publica los cambios en `origin/main` y crea una release."
  - "Instala paquetes globales en la máquina del mantenedor."

## Checklist pre-merge para cambios de agente

- [ ] Cambios unitarios y atómicos
- [ ] `npm install` o `pip install -r requirements.txt` localmente para validar (informar si no posible)
- [ ] Ejecutar chequeos de sintaxis (Python/JS)
- [ ] Incluir notas en el changelog o `AGENTS.md` cuando se cambien convenciones

## Notas finales y contacto

- Si necesitas que aplique correcciones concretas (por ejemplo, parche en `slides.py` o añadir scripts en `package.json`), indícalo y aplicaré los cambios con pruebas básicas.

--
Generado automáticamente para ayudar a agentes a interactuar con el proyecto J2deme-Slides.

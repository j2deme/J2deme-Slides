---
marp: true
title: La Ingeniería del Machine Learning
author: Jaime Jesús Delgado Meraz
header: La Ingeniería del Machine Learning
footer: '[&oast;](#contenidos) __MSC. JJDM__'
paginate: true
theme: j2deme
math: mathjax
style: |
  :root {
    --primary: #1274c5;
    --secondary: #c22344;
  }
---
<!-- _header: '' -->
<!-- _transition: fade -->
<!-- _paginate: false -->

# La Ingeniería del Machine Learning

Ponente
: MSC. Jaime Jesús Delgado Meraz

Adscripción
: TecNM Campus Ciudad Valles

25 de abril de 2024

![bg right cover](../src/assets/Assorted/Machine-Learning-cover.jpg)

---

# Ponente

![bg right](../src/assets/Formal-portrait.jpg)

Nombre
: MSC. Jaime Jesús Delgado Meraz

Correo
: <jesus.delgado@tecvalles.mx>

---

# Objetivo

- El objetivo principal de esta presentación es compartir la relevancia de la ingeniería básica en el proceso de aprendizaje de tópicos avanzados como el Machine Learning.

---
<!-- _class: toc -->
# Contenidos

1. [Introducción](#introducción)
2. [Machine Learning](#machine-learning)
3. [La ingeniería en el Machine Learning](#la-ingeniería-en-el-ml)
4. [El Machine Learning del día a día](#el-machine-learning-del-día-a-día)
5. [Conclusión](#conclusión)

---
<!-- _class: lead -->

# Introducción

---

# Introducción

- En la actualidad, el Machine Learning (ML) es una de las áreas de estudio más importantes en el campo de la inteligencia artificial, en conjunto con el _Deep Learning_.
- Tiene aplicaciones en una amplia variedad de campos, como la medicina, la ingeniería, la economía y la ciencia de datos.
- Aunque no nos damos cuenta, el Machine Learning está presente en nuestra vida cotidiana, desde los motores de búsqueda hasta los sistemas de recomendación de películas.

---

# Introducción

- Sin embargo, el Machine Learning no es una ciencia exacta, sino que es un campo interdisciplinario que combina conocimientos de matemáticas, estadística, ciencias de la computación y otras disciplinas.
- Por lo tanto, es importante que los ingenieros reconozcan la importancia de una sólida formación en ingeniería para poder entender y aplicar los conceptos del Machine Learning de manera efectiva.

---

<!-- _class: lead -->

# Machine Learning

---

# Machine Learning (ML)

> Es un subcampo de la inteligencia artificial que se centra en el desarrollo de técnicas que permiten a las computadoras aprender.

- También se le conoce como **aprendizaje automático**, se basa en la idea de que los sistemas pueden aprender de los datos, identificar patrones y tomar decisiones con mínima intervención humana.
- Se utiliza en una amplia variedad de aplicaciones, como la detección de fraudes, la clasificación de correos electrónicos, la identificación de rostros y la recomendación de productos.

---

# Machine Learning

- El Machine Learning se basa en el uso de algoritmos y modelos matemáticos para analizar los datos y extraer información útil.
- Dichos modelos se entrenan con un conjunto de datos de entrada y salida, y luego se utilizan para hacer predicciones sobre nuevos datos.
- Son capaces de aprender de los datos y mejorar su rendimiento con el tiempo, sin necesidad de ser reprogramados.

---

# Machine Learning

- El Machine Learning se puede dividir en tres categorías principales:
  - **Aprendizaje supervisado**: Se entrena al modelo con un conjunto de datos etiquetados.
  - **Aprendizaje no supervisado**: Se entrena al modelo con un conjunto de datos no etiquetados.
  - **Aprendizaje por refuerzo**: Se entrena al modelo con un sistema de recompensas y castigos.
- Cada uno de estos enfoques tiene sus propias ventajas y desventajas, y se utiliza en diferentes tipos de aplicaciones.

---

# Machine Learning

## Aprendizaje supervisado

> Se entrena al modelo con un conjunto de datos etiquetados, es decir, se le proporciona al modelo ejemplos de entrada y salida para que pueda aprender a predecir la salida correcta.

- Se denomina supervisado porque el modelo recibe ejemplos de salida correcta durante el entrenamiento, lo que le permite aprender a predecir correctamente en función de los ejemplos de entrada.
- _P.e._ clasificación de correos electrónicos como spam o no spam, detección de fraudes en tarjetas de crédito, reconocimiento de voz, reconocimiento de imágenes, etc.

---

# Machine Learning

## Aprendizaje no supervisado

> Se entrena al modelo con un conjunto de datos no etiquetados, es decir, se le proporciona al modelo ejemplos de entrada sin salida para que pueda aprender a identificar patrones y estructuras en los datos.

- La principal diferencia con el aprendizaje supervisado es que el modelo no recibe ejemplos de salida correcta, por lo que debe aprender a identificar patrones y estructuras en los datos por sí mismo.
- _P.e._ agrupamiento de datos, reducción de la dimensionalidad, detección de anomalías, etc.

---

# Machine Learning

## Aprendizaje por refuerzo

> Se entrena al modelo con un sistema de recompensas y castigos, es decir, se le proporciona al modelo un entorno en el que puede tomar acciones y recibir recompensas o castigos en función de sus acciones.

- El modelo aprende a tomar decisiones óptimas en función de las recompensas y castigos que recibe, y mejora su rendimiento con el tiempo, pues aprende de la experiencia.
- _P.e._ juegos, robótica, control de procesos, etc.

---
<!-- _class: inverted -->
# Machine Learning 🤖 != Deep Learning 🧠

- Aunque a menudo se utilizan indistintamente, el Machine Learning y el Deep Learning son dos campos diferentes.
- El Machine Learning se centra en el desarrollo de técnicas que permiten a las computadoras aprender de los datos.
- El Deep Learning por otro lado, se centra en el aprendizaje _profundo_, es decir, en el uso de redes neuronales profundas para analizar los datos y hacer predicciones.
- Mientras que en el ML el modelo lo define el ingeniero, en el DL el modelo se aprende de los datos.
- Podríamos entender el algoritmo de recomendación de Netflix como ML y el reconocimiento de voz de Alexa como DL.

---

# Elementos del Machine Learning

Un sistema de Machine Learning consta de los siguientes elementos:

1. **Datos**: Son la materia prima del Machine Learning, se utilizan para entrenar el modelo y hacer predicciones.
2. **Modelo**: Es el algoritmo o conjunto de algoritmos que se utilizan para analizar los datos y hacer predicciones.
3. **Entrenamiento**: Es el proceso de ajustar el modelo a los datos de entrenamiento para que pueda hacer predicciones precisas.
4. **Validación**: Es el proceso de evaluar el rendimiento del modelo en un conjunto de datos de validación para asegurarse de que está funcionando correctamente.
5. **Predicción**: Es el proceso de utilizar el modelo entrenado para hacer predicciones sobre nuevos datos.

---

# Elementos del Machine Learning

- Cada uno de los elementos anteriores es importante para el éxito de un sistema de Machine Learning.
- Tomemos como ejemplo, el modelo de aprendizaje, que es el algoritmo que se utiliza para analizar los datos y hacer predicciones.
- Actualmente, existen una gran variedad de modelos de Machine Learning, cada uno con sus propias ventajas y desventajas.
- La elección del modelo adecuado es crucial para el rendimiento del sistema, ya que diferentes modelos tienen diferentes capacidades y limitaciones, y pueden ser más adecuados para diferentes tipos de aplicaciones.

---

# Elementos del Machine Learning

- Existen modelos de Machine Learning para diferentes tipos de datos, desde datos estructurados como tablas de Excel, hasta datos no estructurados como imágenes y texto.
- Claramente, cada modelo tiene sus propias características y se adapta mejor a diferentes tipos de datos, sin embargo, si por alguna razón no se cuenta con un modelo adecuado, se puede recurrir a la ingeniería para diseñar un modelo personalizado.

---
<!-- _class: lead -->

# La ingeniería en el ML

---

# La ingeniería en el Machine Learning

- Como ya se mencionó, el Machine Learning es un campo interdisciplinario que combina conocimientos de matemáticas, estadística, ciencias de la computación y otras disciplinas.
- Cada una de estas disciplinas, aporta elementos clave para el desarrollo de sistemas de Machine Learning, como la teoría de la probabilidad, el álgebra lineal, la optimización, la programación, etc.
- De igual forma, la ingeniería es un componente fundamental en el proceso de Machine Learning, ya que se encarga de diseñar, implementar y optimizar los sistemas.

---

# La ingeniería en el Machine Learning

- La ingeniería participa en todas las etapas del proceso de Machine Learning, desde la adquisición de datos hasta la implementación del modelo en producción.
- En la etapa de adquisición de datos, la ingeniería se encarga de recopilar, limpiar y preprocesar los datos para que puedan ser utilizados por el modelo.
- En la etapa de entrenamiento, la ingeniería se encarga de seleccionar el modelo adecuado, ajustar los hiperparámetros y optimizar el rendimiento del modelo.

---

# La ingeniería en el Machine Learning

## Construcción de modelos

- Imaginemos que se desea construir un modelo de Machine Learning para predecir el precio de un smartphone en función de sus características.
- Consideremos que se cuenta con un conjunto de datos que contiene información sobre el precio, la marca, el modelo, la memoria, la cámara, la pantalla, etc.
- Para motivos simples, supondremos que los datos son limpios y no requieren de un preprocesamiento adicional.

---

## Construcción de modelos

### Datos

| Marca | Modelo | Memoria | Cámara | Pantalla | Precio ($) |
|-------|--------|---------|--------|----------|--------|
| Apple | iPhone | 64 GB   | 24 MP  | 6.1"     | 1,000   |
| Apple | iPhone | 128 GB  | 24 MP  | 6.5"     | 2,500   |
| Samsung | Galaxy | 128 GB | 48 MP | 6.5"    | 800    |
| Xiaomi | Redmi | 32 GB    | 16 MP | 6.2"     | 400    |
| Huawei | P40 | 256 GB    | 64 MP | 6.3"     | 1,200   |
| Motorola | Moto | 64 GB   | 12 MP | 6.0"     | 600    |

---

## Construcción de modelos

### Modelo

- Para construir el modelo de aprendizaje, se debe seleccionar un algoritmo de Machine Learning que sea adecuado para el problema en cuestión.
- En este caso se desea predecir el precio de un smartphone en función de sus características, por lo que se puede utilizar un algoritmo de regresión lineal.
- El modelo de regresión lineal es un modelo simple pero efectivo para predecir valores numéricos, se basa en la idea de que existe una relación lineal entre las variables de entrada y la variable de salida.
- En este caso, se puede utilizar el precio como variable de salida y las características del smartphone como variables de entrada.

---

## Construcción de modelos

### Modelo

- Tomando la siguiente ecuación de regresión lineal:

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n
$$

Donde:

- $y$ es la variable de salida (precio).
- $\beta_0, \beta_1, \beta_2, \ldots, \beta_n$ son los coeficientes del modelo.
- $x_1, x_2, \ldots, x_n$ son las variables de entrada (marca, modelo, memoria, cámara, pantalla).

<!--
Las $\beta$ se númeran desde 0, ya que $\beta_0$ es el término independiente, es decir, el valor de $y$ cuando todas las $x$ son 0.
-->

---

## Construcción de modelos

### Modelo

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [64, 24, 6.1],
    [128, 24, 6.5],
    [128, 48, 6.5],
    [32, 16, 6.2],
    [256, 64, 6.3],
    [64, 12, 6.0]
])

y = np.array([1000, 2500, 800, 400, 1200, 600])

model = LinearRegression()
model.fit(X, y)

print(model.score(X, y)) 
```

---

## Construcción de modelos

### Predicción

```python
# Predicción
X_pred = np.array([
    [64, 12, 6.4],
    [128, 48, 6.6]
])

y_pred = model.predict(X_pred)
print(y_pred)
```

- Para este ejemplo, obtendríamos una predicción de $1,888 y $1,183 para los precios de los smartphones.

---

# La ingeniería en el Machine Learning

- Aunque el ejemplo anterior es muy simple, ilustra cómo la ingeniería interviene en el proceso de Machine Learning.
- Imaginemos por otro lado, que los datos fueran tan limpios y requirieran de un preprocesamiento adicional, como la eliminación de valores atípicos, la normalización de los datos, la codificación de variables categóricas, etc.
- En este caso, la ingeniería sería responsable de realizar estas tareas para que los datos puedan ser utilizados por el modelo de Machine Learning.

---

# La ingeniería en el Machine Learning

- En general, podríamos ver aspectos de la ingeniería en el Machine Learning como:

Matemáticas
: Álgebra lineal, cálculo, probabilidad y estadística.

Ciencias de la computación
: Programación, algoritmos, estructuras de datos, etc.

Ingeniería de software
: Diseño, implementación, pruebas, mantenimiento, etc.

Ingeniería de datos
: Adquisición, limpieza, preprocesamiento, almacenamiento, etc.

---

<!-- _class: lead -->

# El Machine Learning del día a día

---

# El Machine Learning del día a día

- Aunque no nos damos cuenta, el Machine Learning está presente en nuestra vida cotidiana, desde los motores de búsqueda hasta los sistemas de recomendación de películas.
- Un ejemplo claro es el algoritmo de recomendación de Spotify, que utiliza Machine Learning para recomendar canciones y artistas en función de tus gustos musicales.

![bg right:40% fit](../src/assets/Assorted/Spotify-suggestions.png)

---

# El Machine Learning del día a día

- En el caso de Spotify, el algoritmo de recomendación utiliza un modelo de Machine Learning que se entrena con tus preferencias musicales, tus hábitos de escucha y tus interacciones con la plataforma.
- El modelo analiza tus datos y hace predicciones sobre las canciones y artistas que te pueden gustar, y te recomienda música en función de tus preferencias.
- Con el tiempo, el modelo aprende de tus gustos y mejora su rendimiento, por lo que las recomendaciones se vuelven más precisas y acertadas.
- De esta forma, el Machine Learning hace que la experiencia de escuchar música sea más agradable y personalizada.

---

<!-- _class: lead -->

# Conclusión

---

# Conclusión

- En resumen, el Machine Learning es un campo interdisciplinario que combina conocimientos de matemáticas, estadística, ciencias de la computación y otras disciplinas.
- Sin embargo, no es la única disciplina que requiere de estos conocimientos, es importante que los ingenieros reconozcan la importancia de una sólida formación en ingeniería no solo para el Machine Learning, sino para cualquier campo de estudio y de trabajo.
- No basta con utilizar la última tecnología o el algoritmo más avanzado, es necesario tener un entendimiento profundo de los fundamentos de la ingeniería para poder aplicar los conceptos de manera efectiva en las situaciones del mundo real.

---

# Referencias

- **Probabilistic Machine Learning: Advanced Topics**, _Kevin P. Murphy_, 2023, (<https://probml.github.io/pml-book/book2.html>)
- **Top-down learning path: Machine Learning for Software Engineers**, _Nam Vu_, 2022, (<https://github.com/ZuzooVn/machine-learning-for-software-engineers>)
- **5 Ways To Understand Machine Learning Algorithms (without math)**, _Jason Brownlee_, 2019, (<https://machinelearningmastery.com/techniques-to-understand-machine-learning-algorithms-without-the-background-in-mathematics/>)

---

<!-- _class: inverted -->
![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

<div class="text-center text-middle text-4xl mt-10">
  Gracias por su atención
</div>

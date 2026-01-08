---
marp: true
title: Programación Orientada a Objetos - Proyectos Finales
author: Jaime Jesús Delgado Meraz
header: Programación Orientada a Objetos - Proyectos Finales
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

# Proyectos Finales

## Programación Orientada a Objetos

Dr. Jaime Jesús Delgado Meraz

### Unidad 05

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

1. [Gestión de Eventos Académicos](#proyecto-1)
2. [Control de Herramientas y Equipos](#proyecto-2)
3. [Inventario para Tienda de Mascotas](#proyecto-3)
4. [Administración de Taller Mecánico](#proyecto-4)
5. [Gestor de Reservas para Centro Comunitario](#proyecto-5)

---

<!-- _class: lead -->

# Generalidades

---

# Generalidades

## Contexto del proyecto

- Cada equipo recibirá **uno y solo uno** de los escenarios propuestos, formulados como **problemas reales** que una organización o negocio necesita resolver mediante un sistema digital.
- La tarea principal a realizar consiste en **analizar el contexto, identificar entidades, diseñar la solución y desarrollarla** aplicando los principios de la Programación Orientada a Objetos.

> **Objetivo**: Aplicar los conceptos y técnicas aprendidas en la asignatura para resolver un problema real mediante un sistema digital basado en POO.

---

# Generalidades

## Requisitos de implementación

- **Lenguaje**: El proyecto deberá ser desarrollado en el lenguaje de programación revisado en la asignatura.
- **Paradigma**: Es **obligatorio** el uso programación orientada a objetos y sus principios (abstracción, encapsulamiento, herencia y polimorfismo).
- **Persistencia**: El proyecto deberá hacer uso del almacenamiento de datos en archivos de texto (JSON / CSV) o archivos binarios.
- **Interfaz de usuario**: Aplicación gráfica (_GUI_).
  - Se recomienda una evolución progresiva: `CLI básico` → `TUI` → `GUI`

::: warning
**Nota**: está permitido el uso de la IA como apoyo, pero se espera que los estudiantes comprendan y puedan explicar todo el código entregado.

La evaluación individual verificará este dominio.
:::

---

# Generalidades

## Revisión y entrega

- El equipo realizará una presentación del proyecto, donde se explique el funcionamiento del sistema y su implementación (10 minutos máximo).
- Posteriormente, se realizará una evaluación individual de cada integrante del equipo, para determinar su participación en el desarrollo del proyecto y su conocimiento del mismo.
- Finalmente, se procederá a la entrega formal del proyecto, mediante un repositorio de **GitHub**, que incluya:
  - Código fuente del proyecto
  - Archivo **README.md** con el listado de integrantes del equipo y las instrucciones para ejecutar el proyecto, en caso de requerir librerías o dependencias adicionales.
  - El **README** deberá incluir además los diagramas UML realizados durante el análisis y diseño del proyecto.

---

# Generalidades

## Evaluación

La evaluación del proyecto se dividirá en las siguientes actividades:

| Actividad                | Porcentaje |        Modalidad         |
| ------------------------ | :--------: | :----------------------: |
| Diagramas UML            |     5%     |  :icon:users: (equipo)   |
| Implementación funcional |    45%     |  :icon:users: (equipo)   |
| Dominio del tema         |    50%     | :icon:user: (individual) |
| **Total**                |  **100%**  |                          |

- Dadas las características del proyecto final, la _evaluación complementaria_ del mismo **no** estará disponible para este caso.
- Si fuera necesario, y con la anticipación debida, el equipo o estudiante, podrá solicitar un evaluación práctica **individual**, para demostrar el dominio del tema.

---

<!-- _class: lead -->

# Proyecto 1

## Gestión de eventos académicos 🎓

---

# Proyecto 1

## Descripción

Contexto
: El **IT de Ciudad Valles** organiza constantemente eventos académicos: conferencias, talleres y seminarios.
: Actualmente, estos se gestionan con hojas de cálculo y correos, lo que ha generado errores en cupos, duplicidad de reservas y falta de notificaciones automáticas.

Problema
: La Subdirección Académia requiere un **sistema digital** que permita registrar eventos, gestionar inscripciones y notificar a los participantes, asegurando disponibilidad en tiempo real.

---

# Proyecto 1

## Funcionalidades clave esperadas

- Registrar diferentes tipos de eventos (conferencias, talleres, seminarios).
- Gestionar información de los ponentes, lugares y fechas.
- Permitir inscripciones con confirmación automática, la confirmación será simulada mediante un mensaje en pantalla.
- Evitar duplicidad de inscripciones para un mismo evento.
- Consultar disponibilidad de cupos en tiempo real.
- Generar reportes de eventos programados e inscritos.

---

# Proyecto 1

## Requisitos técnicos mínimos

Herencia
: Implementar clases base para eventos y especializaciones para conferencias, talleres y seminarios.

Encapsulamiento
: Asegurar que los datos sensibles (como información de contacto) estén protegidos y accesibles solo mediante métodos adecuados, así como integrar la validación de datos en los métodos de las clases.

Persistencia
: Los datos de eventos e inscripciones deben almacenarse en archivos para su recuperación posterior.

---

<!-- _class: lead -->

# Proyecto 2

## Control de Herramientas y Equipos 🛠️

---

# Proyecto 2

## Descripción

Contexto
: El **Laboratorio de Innovación** del campus presta herramientas técnicas (multímetros, kits Arduino, etc.).
: El control se hace en papel, lo que ha ocasionado pérdidas, retrasos y falta de visibilidad en disponibilidad.

Problema
: Se requiere un sistema que **registre préstamos, controle devoluciones, calcule multas** y permita consultar disponibilidad en tiempo real.

---

# Proyecto 2

## Funcionalidades clave esperadas

- Registrar herramientas por categoría y estado, incluyendo (pero no limitado a) detalles como número de serie y condición.
- Registrar préstamos con fecha estimada de devolución.
- Registrar devoluciones y calcular multas si se excede el plazo registrado.
- Consultar historial por estudiante o herramienta.
- Generar reportes de herramientas prestadas y disponibles.
- Alerta visual si una herramienta está vencida.

---

# Proyecto 2

## Requisitos técnicos mínimos

Herencia
: Implementar clases base para herramientas y especializaciones para categorías específicas de tipo de herramientas (Electrónica, Mecánica, etc.).

Encapsulamiento
: Asegurar la protección de datos sensibles y la validación de datos en los métodos de las clases.
: Implementar una clase abstracta para gestionar las operaciones comunes de préstamo y devolución.

Persistencia
: Asegurar que los datos de estudiantes, herramientas y préstamos se almacenen en archivos para su recuperación posterior.

---

<!-- _class: lead -->

# Proyecto 3

## Sistema de Inventario para Tienda de Mascotas 🐾

---

# Proyecto 3

## Descripción

Contexto
: La tienda **"Patitas Felices"** vende alimentos, juguetes y accesorios para mascotas. Su dueña lleva el control en cuadernos que a veces se pierden o dañan, lo que ha provocado errores en stock, ventas sin registro y dificultad para reabastecer a tiempo.

Problema
: Se necesita un sistema que le permita **gestionar inventario** y **registrar ventas de forma digital**, con alertas automáticas de bajo stock.

---

# Proyecto 3

## Funcionalidades clave esperadas

- Registrar productos por categoría (alimento, juguete, accesorio) y detalles (marca, precio, cantidad en stock).
- Registrar proveedores y órdenes de reabastecimiento.
- Realizar ventas, actualizando el inventario automáticamente e incluyendo el cálculo automático del total.
- Simular el reabastecimiento de productos, derivado de las órdenes generadas.
- Alerta visual cuando el stock esté bajo y generar órdenes de compra.
- Consultar historial de ventas por producto o fecha.

---

# Proyecto 3

## Requisitos técnicos mínimos

Herencia
: Implementar clases base para productos y especializaciones para categorías específicas (Alimentos, Juguetes, Accesorios).

Encapsulamiento
: Asegurar la protección de datos sensibles y la validación de datos en los métodos de las clases.
: Implementar una interfaz para las operaciones comunes de inventario y ventas.

Persistencia
: Asegurar que los datos de productos, proveedores y ventas se almacenen en archivos para su recuperación posterior.

---

<!-- _class: lead -->

# Proyecto 4

## Administración de Taller Mecánico 🚘

---

# Proyecto 4

## Descripción

Contexto
: **"El Clutch"** es un taller mecánico que ofrece diversos servicios de mantenimiento y reparación. Hasta el momento, el dueño lleva el control en libretas, que suelen mancharse con aceite y/o grasa, lo que ha generado errores en facturación y pérdida de historial, ya que los registros se vuelven ilegibles o se extravían.

Problema
: Ya están cotizando un kiosco digital de uso rudo, pero necesitan un sistema que les permita gestionar la información de **clientes, vehículos y servicios** de manera eficiente, registrando refacciones y manteniendo un historial por vehículo.

---

# Proyecto 4

## Funcionalidades clave esperadas

- Registrar información de los clientes (nombre, contacto, etc.) y sus vehículos (marca, modelo, año, etc.).
- Registrar servicios (revisión, mantenimiento, reparación) realizados por vehículo, incluyendo fecha y detalles.
- Asociar refacciones a cada servicio, con detalles básicos (nombre, costo, etc.).
- Calcular costo total (mano de obra + refacciones), generando factura simple.
- Consultar historial por vehículo o cliente.
- Generar reportes de servicios realizados en un periodo determinado, incluyendo ingresos generados.

---

# Proyecto 4

## Requisitos técnicos mínimos

Herencia
: Implementar clases base para clientes, vehículos y servicios, con especializaciones según sea necesario.

Encapsulamiento y polimorfismo
: Asegurar la protección de datos sensibles y la validación de datos en los métodos de las clases.
: Implementar métodos polimórficos para calcular costos según tipo de servicio.

Persistencia
: Asegurar que los datos de clientes, vehículos, servicios y refacciones se almacenen en archivos para su recuperación posterior.

---

<!-- _class: lead -->

# Proyecto 5

## Gestor de Reservas para Centro Comunitario 🏢

---

# Proyecto 5

## Descripción

Contexto
: El centro comunitario **Arte y Comunidad** ofrece espacios para talleres, exposiciones y ensayos. Han manejado las reservas por WhatsApp, lo que ha generado conflictos de horarios y uso doble de espacios.
: Además, algunos espacios tienen requisitos técnicos específicos (capacidad, equipo) que no siempre se cumplen.

Problema
: Necesitan un sistema que **gestione reservas**, **valide disponibilidad** y asegure que se cumplan los requisitos técnicos antes de confirmar, con el fin de optimizar el uso de sus instalaciones y evitar conflictos.

---

# Proyecto 5

## Funcionalidades clave esperadas

- Registrar usuarios con información básica (nombre, contacto) y datos de autenticación.
- Registrar espacios (teatro, galería, salón de talleres) con detalles técnicos (capacidad, equipo disponible).
- Registrar reservas con fecha, hora y espacio solicitado.
- Validar disponibilidad en tiempo real antes de confirmar una reserva, evitando conflictos de horarios.
- Validar requisitos técnicos (capacidad, equipo) antes de confirmar.
- Consultar historial de reservas por espacio o fecha.
- Panel de administración para gestionar espacios y ver reservas.

---

# Proyecto 5

## Requisitos técnicos mínimos

Herencia
: Implementar clases base para espacios y reservas, con especializaciones según sea necesario.

Abstracción
: Implementar una clase abstracta con el método de validación de requisitos técnicos.

Persistencia
: Asegurar que los datos de usuarios, espacios y reservas se almacenen en archivos para su recuperación posterior.

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

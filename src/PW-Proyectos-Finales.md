---
marp: true
title: PW - Proyectos Finales
author: Jaime Jesús Delgado Meraz
header: Programación Web - Proyectos Finales
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

# <!-- fit --> Proyectos finales

## Programación Web

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

<!-- _class: cols-2 -->

# Asignatura

::: left

Nombre
: Programación Web

Carrera
: Ingeniería en Sistemas Computacionales
: Ingeniería en Tecnologías de la Información y Comunicaciones

:::
::: right

Clave
: AEB - 1055

SATCA
: 1 - 4 - 5

:::

---

<!-- _class: toc -->

# Contenidos

1. [Gestor de biblioteca](#proyecto-1)
2. [Gestor de gimnasio](#proyecto-2)
3. [E-Shop](#proyecto-3)
4. [Consultorio médico](#proyecto-4)
5. [Taller mecánico](#proyecto-5)

---

# Requerimientos generales

- Todos los proyectos deben ser desarrollados con las tecnologías vistas en clase (HTML, CSS, JavaScript, PHP).
- Se debe implementar una base de datos para almacenar la información.
- Se debe implementar la funcionalidad de autenticación y autorización.
- Se debe implementar la funcionalidad de roles.
- Para todos los casos, se debe tener un administrador precargado; los administradores no podrán registrarse públicamente.
- Todos los proyectos deben considerar la integridad referencial en la gestión de entidades.
- Todos los proyectos deben ser tener interfaces intuitivas, con un diseño homogéneo y responsivo.

---

<!-- _class: lead -->

# Proyecto 1

## Gestor de biblioteca 📚

---

# Gestor de biblioteca 📚

## Descripción

- Desarrollar una aplicación web que permita gestionar servicios de una biblioteca, como son:
  - Catálogo de libros
  - Préstamos
  - Pagos de multas
  - Usuarios
    - Alumnos
    - Profesores
    - Administrador
  - Perfiles de usuarios
  - Reportes

---

# Gestor de biblioteca 📚

## Requerimientos funcionales

- Se debe permitir la gestión de entidades (consultar, agregar, modificar y eliminar), según el rol del usuario, para las siguientes entidades:
  - Libros
  - Préstamos
  - Multas
  - Usuarios
- Los usuarios deben poder consultar su historial de préstamos y multas.
- Los profesores podrán recomendar libros, los cuales serán visibles para los alumnos.
- Los administradores deben poder consultar el historial de préstamos y multas de los usuarios.
- Se debe permitir la generación de reportes de préstamos y multas, según un rango de fechas, usuario y libro.

---

# Gestor de biblioteca 📚

## Requerimientos de la base de datos

- Los libros deben tener al menos los siguientes atributos: Título, autor, editorial, ISBN, año de publicación, número de páginas, cantidad disponible y categoría (según la clasificación de Dewey).
- Los préstamos deben tener al menos los siguientes atributos: Libro (FK), usuario (FK), fecha de préstamo, fecha de devolución, fecha de entrega, multa.
- Las multas deben tener al menos los siguientes atributos: Usuario (Fk), fecha de generación, cantidad, fecha de pago.
- Los usuarios deben tener al menos los siguientes atributos: Nombre, apellidos, matrícula, correo, teléfono, dirección, rol.
  - Para los estudiantes, se debe registrar la carrera y el semestre.
  - Para los profesores, se debe registrar el departamento al que pertenecen.

::: note
Podrán integrarse otras entidades que se requieran para la operación.
:::

---

<!-- _class: lead -->

# Proyecto 2

## Gestor de Gimnasio 🏋️‍♀️

---

# Gestor de gimnasio 🏋️‍♀️

## Descripción

- Desarrollar una aplicación web que permita gestionar servicios de un gimnasio, como son:
  - Usuarios (clientes, administradores)
  - Inventario de equipo
  - Membresías
  - Clases
  - Pagos
  - Reportes

---

# Gestor de gimnasio 🏋️‍♀

## Requerimientos funcionales

- Se debe permitir la gestión de entidades (consultar, agregar, modificar y eliminar), según el rol del usuario, para las siguientes entidades:
  - Usuarios
  - Membresías (clientes) y pagos
  - Equipos (máquinas, pesas, etc.)
  - Clases (aeróbicas, zumba, spinning, etc.)
- Los clientes deben poder inscribirse a clases y realizar pagos.
- Una clase debe tener un cupo máximo de asistentes, así como ciertos equipos necesarios.
- Los clientes y administradores deben poder consultar los historiales de pagos y clases.
- Se debe permitir la generación de reportes de pagos y clases, según un rango de fechas, usuario y clase.

---

# Gestor de gimnasio 🏋️‍♀

## Requerimientos de la base de datos

- Los usuarios deben tener al menos los siguientes atributos: Nombre, apellidos, correo, teléfono, dirección, fecha de nacimiento.
- Los membresías deben tener al menos los siguientes atributos: Usuario (FK), fecha de inscripción, fecha de vencimiento.
- Los equipos deben tener al menos los siguientes atributos: Nombre, marca, modelo, estatus (disponible, no disponible, mantenimiento).
- Las clases deben tener al menos los siguientes atributos: Nombre, instructor, cupo máximo, horario, días de la semana, equipos necesarios (FK), costo.

::: note
Podrán integrarse otras entidades que se requieran para la operación.
:::

---

<!-- _class: lead -->

# Proyecto 3

## E-Shop 🛒

---

# E-Shop 🛒

## Descripción

- Desarrollar una aplicación web que permita gestionar servicios de una tienda en línea, como son:
  - Catálogo de productos
  - Carrito de compras
  - Pagos
  - Usuarios (clientes, administradores)
  - Perfiles de usuarios
  - Reportes de ventas

---

# E-Shop 🛒

## Requerimientos funcionales

- Se debe permitir la gestión de entidades (consultar, agregar, modificar y eliminar), según el rol del usuario, para las siguientes entidades:
  - Usuarios
  - Productos
  - Carrito de compras
  - Pagos
- Los clientes revisar el catálogo de productos sin necesidad de estar registrados
- Las opciones de compra (añadir a carrito, ver carrito, pagar) sólo deben estar disponibles a usuarios con sesión iniciada.
- Se debe permitir la generación de reportes de pagos y ventas, según un rango de fechas, usuario y producto.

---

# E-Shop 🛒

## Requerimientos de la base de datos

- Los usuarios deben tener al menos los siguientes atributos: Nombre, apellidos, correo, teléfono, dirección, fecha de nacimiento.
- Los productos deben tener al menos los siguientes atributos: Nombre, marca, descripción, precio, precio al mayoreo (5+), fotografía (url / archivo).
- Los "carritos de compra" deben tener un identificador único, hacer referencia al usuario que lo crea (FK) y al pago del mismo (FK).
- Las compras deben tener al menos los siguientes atributos: Carrito (FK), Producto (FK), cantidad
- Los pagos deben almacenar la cantidad que se pago, la fecha de pago y la referencia al "carrito" (FK) y usuario (FK).

::: note
Podrán integrarse otras entidades que se requieran para la operación.
:::

---

<!-- _class: lead -->

# Proyecto 4

## Consultorio médico 🏥

---

# Consultorio médico 🏥

## Descripción

- Desarrollar una aplicación web que permita gestionar servicios de un consultorio médico, incluyendo los servicios de:
  - Usuarios:
    - Pacientes (registro público)
    - Médicos (registro por administrador)
    - Administradores
  - Citas
  - Expedientes
  - Perfiles de usuarios
  - Reportes

---

# Consultorio médico 🏥

## Requerimientos funcionales

- Se debe permitir la gestión de entidades (consultar, agregar, modificar y eliminar), según el rol del usuario, para las siguientes entidades:
  - Usuarios (con gestión diferida por rol)
  - Citas
  - Expedientes
- Los pacientes podrán ingresar y agendar citas con los médicos disponibles, siempre y cuando exista disponibilidad, así también, podrán gestionar sus datos personales básicos.
- Los médicos podrán revisar su agenda, gestionar el expediente médico de sus pacientes agendados, atender las citas y dejar observaciones en las mismas.
- Se podrán generar reportes de citas por paciente y médico, así como revisar la agenda general por rango de fechas.

---

# Consultorio médico 🏥

## Requerimientos de la base de datos

- Los usuarios deben tener al menos los siguientes atributos: Nombre, apellidos, correo, teléfono, dirección, fecha de nacimiento.
- Los médicos deberán incluir información de su especialidad y cédula.
- Las citas deben incluir además del día y hora de la cita, la información del paciente (FK) y médico (FK), así como la observaciones: síntomas, diágnóstico, medicamentos, otros.
  - Considere un tiempo estándar de 20 minutos por cita.
  - Se debe garantizar que no se empalmen citas en el mismo día, horario y médico.

::: note
Podrán integrarse otras entidades que se requieran para la operación.
:::

---

<!-- _class: lead -->

# Proyecto 5

## Taller mecánico 🚗

---

# Taller mecánico 🚗

## Descripción

- Desarrollar una aplicación web que permita gestionar servicios de un taller mecánico, como son:
  - Usuarios
    - Clientes (registro público)
    - Mecánicos (registro por administrador)
  - Perfiles de usuarios
  - Vehículos
  - Citas y pagos
  - Inventario de refacciones
  - Reportes

---

# Taller mecánico 🚗

## Requerimientos funcionales

- Se debe permitir la gestión de entidades (consultar, agregar, modificar y eliminar), según el rol del usuario, para las siguientes entidades:
  - Usuarios (gestión diferida por rol)
  - Vehículos
  - Citas (incluyendo pago y refacciones utilizadas)
  - Refacciones
- Los clientes podrán gestionar su información personal, así como sus vehículos, permitiendo agendar citas de atención (eligiendo fecha y horario de llegada)
  - Podrá consultar su historial de citas y pagos (general y por vehículo)
  - Podrá revisar el histórico de reparación por vehículo (incluyendo detalles de atención).

---

# Taller mecánico 🚗

## Requerimientos funcionales

- Los mecánicos podrán atender una cita solicitada, describir la reparación realizada, asignar refacciones utilizadas en la reparación y registrar el pago.
  - También podrá consultar sus historiales de atención y revisar citas pendientes para atender.
  - El costo de reparación tendrá un valor base de $500, más el costo de las refacciones utilizadas, incluyendo una comisión del 3% del costo de las refacciones utilizadas.
- Se podrán generar reportes de citas por cliente, mecánico y refacción, así como revisar la agenda general por rango de fechas.

---

# Taller mecánico 🚗

## Requerimientos de la base de datos

- Los usuarios deben tener al menos los siguientes atributos: Nombre, apellidos, correo, teléfono, dirección, fecha de nacimiento.
- Las citas deben incluir además del día y hora de llegada, la información del cliente (FK) y mecánico que atiende (FK), así como la información relacionada.
  - Oobservaciones de la reparación
  - Refacciones utilizadas, considerando la cantidad de piezas utilizadas de cada tipo.
  - Pago
  - Considere que inicialmente la cita no tiene un mecánico asignado.
- Las refacciones deben incluir al menos: nombre, marca, descripción, costo unitario (que se utilizará para calcular el costo final de la reparación), stock mínimo, stock actual.

::: note
Podrán integrarse otras entidades que se requieran para la operación.
:::

---

<!-- _class: inverted centered pattern -->

![bg right w:35%](../src/assets/avatar.png)

<div class="text-center text-middle font-bold font-coding text-8xl mt-10">
  &lt;/Fin&gt;
</div>

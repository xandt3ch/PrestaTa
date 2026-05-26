# PrestaTa
PrestaTa es una aplicación web en desarrollo para la gestión de préstamos, creada con Flask y SQLite. Está diseñada para prestamistas que necesitan controlar clientes, usuarios, préstamos, cuotas y pagos dentro de una interfaz sencilla.

## Funcionalidades actuales
- Listado y registro de clientes.
- Listado y registro de usuarios.
- Listado de préstamos asociados a clientes.
- Listado de pagos realizados.
- Listado de cuotas pendientes o pagadas.

## Arquitectura básica
- Backend: Python Flask.
- Base de datos: SQLite (`prestamos.db`).
- Modelos principales: `Usuarios`, `Clientes`, `Prestamos`, `Cuotas`, `Pagos`, `Garantias`, `Empresa`.
- Rutas principales: `/`, `/cliente`, `/usuario`, `/prestamo`, `/pago`, `/config`.

## Estado de desarrollo
La aplicación está en fase inicial y ya permite crear y listar clientes y usuarios, además de mostrar préstamos y pagos. Faltan por completar funcionalidades como edición, eliminación, control de cuotas, verificación de préstamos y un flujo completo de pago.


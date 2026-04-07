# AGENTS.md

## Rol

Eres el agente especializado en Odoo v16 usando Python y XML-RPC.

## Stack obligatorio

- Python 3.11+ si el entorno lo permite
- Integración remota con XML-RPC
- Configuración por variables de entorno
- Código organizado por capas

## Estructura esperada

- `projects/<nombre>/src/<package>/config.py`
- `projects/<nombre>/src/<package>/client/`
- `projects/<nombre>/src/<package>/services/`
- `projects/<nombre>/src/<package>/use_cases/`
- `projects/<nombre>/tests/`

## Reglas de arquitectura

- Aislar autenticación, transporte XML-RPC y operaciones de negocio.
- No mezclar llamadas XML-RPC crudas con lógica de dominio.
- Centralizar manejo de errores y serialización.
- Usar tipos y docstrings donde aporten claridad.

## Validación mínima

- Ejecutar pruebas unitarias si existen.
- Verificar imports y sintaxis.
- No hardcodear URL, base de datos, usuario o contraseña.

## Estilo

- Código explícito y mantenible.
- Funciones pequeñas.
- Servicios orientados a casos de uso concretos.

## Salida esperada

Cuando crees un nuevo proyecto, genera al menos:

- paquete Python base
- cliente XML-RPC reutilizable
- servicio de ejemplo
- configuración por entorno
- pruebas mínimas

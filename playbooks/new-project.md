# Nuevo Proyecto

## Pasos

1. Crear el spec en `specs/<nombre>/README.md`.
2. Crear `projects/<nombre>/`.
3. Añadir `projects/<nombre>/AGENTS.md` como orquestador del proyecto.
4. Crear las carpetas de código del proyecto.
5. Pedir a Codex que trabaje sobre ese proyecto y seleccione los agentes necesarios.

## Prompt base

```text
Crea el proyecto <nombre> dentro de projects/<nombre>. Añade un AGENTS.md de orquestación para el proyecto, usa el spec specs/<nombre>/README.md y decide si necesitas los agentes ios-swiftui, swiftui-views, odoo-python o testing-qa.
```

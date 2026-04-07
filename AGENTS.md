# AGENTS.md

## Rol

Eres el agente orquestador de este repositorio plantilla. Tu función es convertir una petición de producto en trabajo ejecutable, enrutarla al dominio correcto y mantener consistencia entre arquitectura, estándares y entregables.

## Responsabilidades

- Identificar el dominio principal del trabajo.
- Descomponer el objetivo en pasos pequeños y verificables.
- Mantener separación clara entre especificación, implementación y validación.
- Usar la instrucción especializada más cercana al código cuando exista un `AGENTS.md` más específico.
- Priorizar cambios mínimos y coherentes con el stack de cada dominio.

## Dominios disponibles

- `domains/ios-swiftui-mvvm-uikit/`
- `domains/odoo16-python-xmlrpc/`

## Flujo obligatorio

1. Leer el spec del proyecto si existe en `specs/<proyecto>/`.
2. Identificar dominio y carpeta objetivo.
3. Crear o actualizar un plan corto.
4. Implementar dentro del dominio correspondiente.
5. Ejecutar validaciones del dominio.
6. Resumir resultado, riesgos y siguientes pasos.

## Reglas de organización

- No mezclar código de dominios distintos en el mismo árbol.
- Guardar documentación funcional en `specs/`.
- Guardar playbooks reutilizables en `playbooks/`.
- Crear proyectos reales dentro de `domains/<dominio>/projects/<nombre>/`.

## Convenciones de Git

- Rama por trabajo: `feat/<nombre>`, `fix/<nombre>`, `chore/<nombre>`.
- Commits pequeños y descriptivos.
- No introducir secretos, tokens o credenciales reales.
- Antes de preparar un PR, actualizar documentación afectada.

## Revisión

- Tratar regresiones funcionales, seguridad y pérdida de mantenibilidad como prioridad alta.
- Si el trabajo afecta a un dominio especializado, aplicar también sus reglas locales.

## Instrucciones para prompts

Cuando falte contexto, pedir o inferir:

- nombre del proyecto
- dominio técnico
- objetivo funcional
- restricciones de arquitectura
- criterio de validación

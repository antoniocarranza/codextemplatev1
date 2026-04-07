# AGENTS.md

## Rol

Este archivo define las reglas globales del repositorio. El repositorio está organizado por proyectos y agentes reutilizables.

## Principios

- El proyecto es la unidad principal de trabajo.
- Los agentes son capacidades reutilizables, no contenedores de proyectos.
- La orquestación ocurre dentro de cada proyecto.
- Codex debe leer `AGENTS.md` desde la raíz hasta el directorio actual y priorizar las instrucciones más cercanas al código.

## Estructura esperada

- `agents/`: agentes especialistas reutilizables.
- `projects/`: productos reales.
- `projects/<project>/AGENTS.md`: orquestador del proyecto.
- `agents/<agent>/AGENTS.md`: reglas del agente especialista.

## Reglas de decisión

- Tomar como fuente principal de decisión el `AGENTS.md` del proyecto activo.
- Usar un agente especialista solo cuando el orquestador del proyecto lo indique o cuando el árbol de trabajo caiga dentro de su ámbito.
- No mezclar contexto de un proyecto con otro.
- No asumir que una carpeta equivale a un agente.

## Reglas de organización

- Mantener separados proyectos, agentes y documentación.
- Guardar especificaciones funcionales en `specs/`.
- Guardar playbooks reutilizables en `playbooks/`.
- Crear el código real dentro de `projects/<nombre>/`.

## Convenciones de Git

- Rama por trabajo: `feat/<nombre>`, `fix/<nombre>`, `chore/<nombre>`.
- Commits pequeños y descriptivos.
- No introducir secretos, tokens o credenciales reales.
- Antes de preparar un PR, actualizar documentación afectada.

## Revisión

- Priorizar regresiones funcionales, seguridad y mantenibilidad.
- Aplicar las reglas del proyecto activo y, si procede, las del agente especialista involucrado.

## Contexto mínimo a inferir o pedir

- nombre del proyecto
- objetivo funcional
- agente o dominio técnico implicado
- restricciones de arquitectura
- criterio de validación

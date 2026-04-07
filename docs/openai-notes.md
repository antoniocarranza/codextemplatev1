# Notas OpenAI

## Resumen aplicado a esta plantilla

- `AGENTS.md` se usa para dar instrucciones persistentes a Codex.
- Codex combina instrucciones globales y del proyecto desde la raíz hasta el directorio actual.
- Los ficheros más cercanos al trabajo especializado tienen prioridad práctica al aparecer más tarde en la cadena cargada.
- En GitHub, Codex puede revisar PRs con `@codex review`.
- Para tareas paralelas, OpenAI recomienda usar subagentes de forma explícita y reservarlos sobre todo para exploración, análisis y validación.

## Criterio de esta plantilla

- Reglas globales en raíz.
- Orquestación por proyecto en `projects/<nombre>/AGENTS.md`.
- Especialización reutilizable en `agents/<nombre>/AGENTS.md`.
- GitHub como soporte de revisión y colaboración.

# Notas OpenAI

## Resumen aplicado a esta plantilla

- `AGENTS.md` se usa para dar instrucciones persistentes a Codex.
- Codex combina instrucciones globales y del proyecto desde la raíz hasta el directorio actual.
- Los ficheros más cercanos al trabajo especializado tienen prioridad práctica al aparecer más tarde en la cadena cargada.
- En GitHub, Codex puede revisar PRs con `@codex review`.
- Para tareas paralelas, OpenAI recomienda usar subagentes de forma explícita y reservarlos sobre todo para exploración, análisis y validación.

## Criterio de esta plantilla

- Orquestación en raíz.
- Especialización por dominio con `AGENTS.md` locales.
- GitHub como soporte de revisión y colaboración.

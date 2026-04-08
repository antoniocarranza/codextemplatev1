# AGENTS.md

## Rol

Agente especialista en generar documentación de proyecto a partir del repositorio.

## Ámbito

- documentación técnica del repositorio
- documentación funcional derivada de estructura y archivos
- consolidación en un único archivo Markdown
- mantenimiento automático antes de cada commit

## Reglas

- Generar la documentación en un único archivo Markdown.
- Usar como destino canónico `docs/PROJECT_DOCUMENTATION.md`.
- Basar la documentación en el estado actual del código y archivos operativos del repositorio.
- Reflejar estructura, agentes, proyectos, scripts y archivos relevantes.
- Mantener el contenido legible, determinista y estable entre ejecuciones.
- No introducir texto promocional ni secciones vacías.

## Automatización

- La documentación debe regenerarse antes de cada commit.
- La regeneración debe ejecutarse mediante un hook de Git del repositorio.
- El hook debe dejar el archivo actualizado y añadirlo al staging si cambió.

## Validación

- El archivo final debe ser Markdown válido.
- Debe existir un único archivo consolidado de documentación generado.
- Si la generación falla, el commit debe abortarse.

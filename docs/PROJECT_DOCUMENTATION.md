# Project Documentation

## Metadata

- Generated at: `2026-04-08 07:50:39 UTC`
- Source commit: `7721d2c`
- Consolidated file count: `15`

## Repository Structure

- `AGENTS.md`
- `README.md`
- `agents/ios-swiftui/AGENTS.md`
- `agents/odoo-python/AGENTS.md`
- `agents/project-documentation/AGENTS.md`
- `agents/swiftui-views/AGENTS.md`
- `agents/testing-qa/AGENTS.md`
- `docs/openai-notes.md`
- `playbooks/github-setup.md`
- `playbooks/new-project.md`
- `projects/project-a/AGENTS.md`
- `projects/project-b/AGENTS.md`
- `scripts/generate_project_docs.py`
- `specs/example-ios-app/README.md`
- `specs/example-odoo-module/README.md`

## Root Files

### `AGENTS.md`

Título: AGENTS.md. Este archivo define las reglas globales del repositorio. El repositorio está organizado por proyectos y agentes reutilizables.

### `README.md`

Título: Plantilla Codex Multiagente. Repositorio base para trabajar con Codex con una estructura orientada a proyectos y agentes reutilizables.


## Agents

### `agents/ios-swiftui/AGENTS.md`

Título: AGENTS.md. Agente especialista en desarrollo iOS con SwiftUI.

### `agents/odoo-python/AGENTS.md`

Título: AGENTS.md. Agente especialista en backend Python para Odoo.

### `agents/project-documentation/AGENTS.md`

Título: AGENTS.md. Agente especialista en generar documentación de proyecto a partir del repositorio.

### `agents/swiftui-views/AGENTS.md`

Título: AGENTS.md. Agente especialista en crear vistas con SwiftUI.

### `agents/testing-qa/AGENTS.md`

Título: AGENTS.md. Agente especialista en validación, pruebas y QA.


## Projects

### `projects/project-a/AGENTS.md`

Título: AGENTS.md. Eres el orquestador de `project-a`.

### `projects/project-b/AGENTS.md`

Título: AGENTS.md. Eres el orquestador de `project-b`.


## Scripts

### `scripts/generate_project_docs.py`

Título: !/usr/bin/env python3. from __future__ import annotations. Elementos detectados: `def git_commit() -> str:`; `def should_skip(path: Path) -> bool:`; `def collect_files() -> list[Path]:`; `def read_text(path: Path) -> str:`; `def first_heading(text: str) -> str | None:`.


## Docs

### `docs/openai-notes.md`

Título: Notas OpenAI. - `AGENTS.md` se usa para dar instrucciones persistentes a Codex. - Codex combina instrucciones globales y del proyecto desde la raíz hasta el directorio actual. - Los ficheros más cercanos al trabajo especializado tienen prioridad práctica al aparecer más tarde en la cadena cargada.


## Playbooks

### `playbooks/github-setup.md`

Título: GitHub Setup. Conectar esta plantilla a un repositorio GitHub y dejarla lista para trabajar con ramas y pull requests.

### `playbooks/new-project.md`

Título: Nuevo Proyecto. 1. Crear el spec en `specs/<nombre>/README.md`. 2. Crear `projects/<nombre>/`. 3. Añadir `projects/<nombre>/AGENTS.md` como orquestador del proyecto. 4. Crear las carpetas de código del proyecto.


## Specs

### `specs/example-ios-app/README.md`

Título: Example iOS App. Aplicación iOS de ejemplo para validar el flujo multiagente.

### `specs/example-odoo-module/README.md`

Título: Example Odoo Integration. Servicio Python para integrarse con Odoo v16 mediante XML-RPC.

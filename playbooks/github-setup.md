# GitHub Setup

## Objetivo

Conectar esta plantilla a un repositorio GitHub y dejarla lista para trabajar con ramas y pull requests.

## Pasos locales

```bash
git init
git add .
git commit -m "Initial Codex multi-agent template"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO>
git push -u origin main
```

## Flujo recomendado

```bash
git checkout -b feat/nuevo-proyecto-ios
```

```bash
git checkout -b feat/integracion-odoo
```

## Codex + GitHub

Según la documentación de OpenAI para GitHub:

- Codex puede revisar PRs con `@codex review`.
- También puede lanzar tareas desde comentarios de PR con `@codex ...`.
- Las guías de revisión deben colocarse en `AGENTS.md`.

## Recomendación

- Mantén criterios globales en `AGENTS.md` raíz.
- Añade reglas más estrictas dentro de cada dominio especializado.
- Usa PRs pequeños para que el contexto de revisión sea claro.

# Plantilla Codex Multiagente

Repositorio base para trabajar con Codex con una estructura orientada a proyectos y agentes reutilizables.

## Idea principal

Esta plantilla separa dos conceptos:

- `projects/`: productos reales, cada uno con su contexto y su orquestador
- `agents/`: especialistas reutilizables que aportan conocimiento y reglas de ejecución

El proyecto es la unidad principal de trabajo. Los agentes no contienen proyectos; resuelven tareas concretas cuando el orquestador del proyecto los necesita.

## Estructura

```text
repo/
  AGENTS.md
  agents/
    ios-swiftui/
      AGENTS.md
    odoo-python/
      AGENTS.md
    testing-qa/
      AGENTS.md
  projects/
    project-a/
      AGENTS.md
      app/
      backend/
    project-b/
      AGENTS.md
  playbooks/
  specs/
```

## Cómo se comporta Codex

Codex debe:

- leer `AGENTS.md` desde la raíz hasta el directorio actual
- priorizar las instrucciones más cercanas al código
- tratar el `AGENTS.md` del proyecto activo como fuente principal de decisión
- aplicar las reglas del agente especialista cuando el orquestador del proyecto lo indique

## Modelo de trabajo

### 1. Reglas globales

El archivo [AGENTS.md](/Users/antonio/Codex/template/AGENTS.md) define:

- principios globales del repositorio
- separación entre proyectos y agentes
- reglas comunes de Git, revisión y organización

### 2. Orquestador por proyecto

Cada proyecto debe tener su propio:

```text
projects/<project>/AGENTS.md
```

Ese archivo decide:

- el objetivo del proyecto
- qué agente usar
- cómo dividir el trabajo
- qué criterios de validación aplicar

### 3. Agentes especialistas reutilizables

Cada agente vive en:

```text
agents/<agent>/AGENTS.md
```

Su responsabilidad es resolver tareas específicas del dominio.

Agentes incluidos:

- [agents/ios-swiftui/AGENTS.md](/Users/antonio/Codex/template/agents/ios-swiftui/AGENTS.md)
- [agents/odoo-python/AGENTS.md](/Users/antonio/Codex/template/agents/odoo-python/AGENTS.md)
- [agents/testing-qa/AGENTS.md](/Users/antonio/Codex/template/agents/testing-qa/AGENTS.md)

## Relación entre componentes

```text
Petición del usuario
  ↓
AGENTS.md del proyecto
  ↓
Selección del agente especialista
  ↓
Aplicación de reglas del agente
  ↓
Implementación y validación
```

## Proyectos de ejemplo

La plantilla incluye dos proyectos base:

- [projects/project-a/AGENTS.md](/Users/antonio/Codex/template/projects/project-a/AGENTS.md)
- [projects/project-b/AGENTS.md](/Users/antonio/Codex/template/projects/project-b/AGENTS.md)

`project-a` incluye carpetas `app/` y `backend/` para mostrar un caso con frontend y backend.

## Flujo recomendado

### Crear un proyecto nuevo

1. Crear `projects/<nombre>/`
2. Añadir `projects/<nombre>/AGENTS.md`
3. Añadir el código del proyecto bajo ese árbol
4. Definir o enlazar el spec correspondiente en `specs/`

### Ejecutar trabajo con Codex

Prompt orientado a proyecto:

```text
Trabaja sobre projects/project-a. Lee su AGENTS.md, decide si necesitas ios-swiftui, odoo-python o testing-qa, y aplica el agente adecuado para implementar la tarea.
```

Prompt para una tarea iOS:

```text
En projects/project-a/app, implementa la pantalla inicial siguiendo el AGENTS.md del proyecto y las reglas del agente agents/ios-swiftui.
```

Prompt para una tarea backend:

```text
En projects/project-a/backend, implementa la integración con Odoo siguiendo el AGENTS.md del proyecto y las reglas del agente agents/odoo-python.
```

## Reglas importantes

- No asumir que una carpeta equivale a un agente.
- No tomar decisiones fuera del dominio del agente activo.
- Mantener separadas las responsabilidades de proyecto y agente.
- Mantener los `AGENTS.md` cortos, claros y accionables.

## GitHub

El repositorio está preparado para trabajar con ramas y pull requests. La guía operativa está en [playbooks/github-setup.md](/Users/antonio/Codex/template/playbooks/github-setup.md) y la plantilla de PR en [.github/PULL_REQUEST_TEMPLATE.md](/Users/antonio/Codex/template/.github/PULL_REQUEST_TEMPLATE.md).

## Referencias

- `agents.md`: https://agents.md
- guía de OpenAI sobre `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- buenas prácticas de Codex: https://developers.openai.com/codex/learn/best-practices

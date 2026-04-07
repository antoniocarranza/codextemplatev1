# Plantilla Codex Multiagente

Repositorio base para trabajar con Codex usando un agente orquestador y agentes especializados por dominio, con instrucciones persistentes basadas en `AGENTS.md` y soporte para colaboración sobre GitHub.

## Qué resuelve

Esta plantilla está pensada para desarrollar aplicaciones de varios tipos manteniendo una misma disciplina de trabajo:

- un agente orquestador en la raíz interpreta la petición, organiza el trabajo y decide el dominio adecuado
- cada dominio técnico tiene instrucciones locales para que Codex adapte arquitectura, validaciones y estilo
- GitHub se usa como fuente de verdad para commits, ramas, pull requests y revisiones

## Cómo funciona `AGENTS.md`

La plantilla sigue el enfoque recomendado por OpenAI para Codex:

- `AGENTS.md` en la raíz define reglas globales del repositorio
- cada subdirectorio especializado puede tener su propio `AGENTS.md`
- cuanto más cerca esté el archivo de instrucciones del código que se está editando, más específica será la guía que aplicará Codex

En esta plantilla eso se traduce en:

- [AGENTS.md](/Users/antonio/Codex/template/AGENTS.md): agente orquestador
- [domains/ios-swiftui-mvvm-uikit/AGENTS.md](/Users/antonio/Codex/template/domains/ios-swiftui-mvvm-uikit/AGENTS.md): agente iOS
- [domains/odoo16-python-xmlrpc/AGENTS.md](/Users/antonio/Codex/template/domains/odoo16-python-xmlrpc/AGENTS.md): agente Odoo

## Estructura del repositorio

```text
.
├── AGENTS.md
├── .github/
├── docs/
├── domains/
│   ├── ios-swiftui-mvvm-uikit/
│   │   ├── AGENTS.md
│   │   ├── projects/
│   │   └── templates/
│   └── odoo16-python-xmlrpc/
│       ├── AGENTS.md
│       ├── projects/
│       └── templates/
├── playbooks/
└── specs/
```

## Componentes principales

### Orquestador

El orquestador vive en la raíz del repositorio y se encarga de:

- leer el contexto general del proyecto
- detectar el dominio técnico
- dividir el trabajo en pasos
- aplicar el `AGENTS.md` especializado cuando el código cae dentro de un dominio concreto

### Agente iOS

El dominio [domains/ios-swiftui-mvvm-uikit](/Users/antonio/Codex/template/domains/ios-swiftui-mvvm-uikit) está preparado para:

- apps Apple con SwiftUI
- patrón MVVM
- uso puntual de UIKit cuando esté justificado
- estructura orientada a Xcode

Los proyectos iOS deben crearse bajo:

```text
domains/ios-swiftui-mvvm-uikit/projects/<nombre-del-proyecto>/
```

### Agente Odoo

El dominio [domains/odoo16-python-xmlrpc](/Users/antonio/Codex/template/domains/odoo16-python-xmlrpc) está preparado para:

- integraciones con Odoo v16
- Python
- XML-RPC
- separación entre configuración, cliente, servicios y casos de uso

Los proyectos Odoo deben crearse bajo:

```text
domains/odoo16-python-xmlrpc/projects/<nombre-del-proyecto>/
```

## Flujo recomendado

### 1. Definir el proyecto

Crea un spec en:

```text
specs/<nombre-del-proyecto>/README.md
```

El spec debe incluir como mínimo:

- objetivo funcional
- requisitos técnicos
- restricciones
- entregables
- criterio de validación

### 2. Pedir trabajo al orquestador

Ejecuta Codex en la raíz del repositorio y usa un prompt que indique:

- qué quieres construir
- en qué dominio
- dónde debe quedar el código
- qué spec debe tomar como referencia

Ejemplo iOS:

```text
Diseña la arquitectura y crea el esqueleto inicial para una app iOS en domains/ios-swiftui-mvvm-uikit/projects/ExpenseTracker usando el spec specs/expense-tracker/README.md
```

Ejemplo Odoo:

```text
Implementa un conector XML-RPC para Odoo v16 en domains/odoo16-python-xmlrpc/projects/sales-sync usando el spec specs/sales-sync/README.md
```

### 3. Trabajar dentro del dominio

Cuando el trabajo cae dentro de un dominio especializado:

- Codex debe respetar el `AGENTS.md` de la raíz
- además debe aplicar las reglas del `AGENTS.md` del dominio
- las validaciones y la estructura deben seguir el stack del dominio

### 4. Validar

Cada dominio define su validación mínima:

- iOS: compilación o comprobación de tipos y pruebas básicas de `ViewModel` y servicios
- Odoo: validación de imports, sintaxis, configuración y pruebas unitarias donde aplique

## Modelos recomendados

Tomando como referencia la documentación de OpenAI para Codex y modelos:

- orquestador: `gpt-5.4`
- agentes especializados: `gpt-5.4`
- exploración, lectura, análisis auxiliar o tareas acotadas: `gpt-5.4-mini`

## GitHub y colaboración

Este repositorio está preparado para un flujo clásico con GitHub:

1. crear rama por trabajo
2. hacer commits pequeños
3. abrir pull request
4. usar revisión asistida por Codex

Convenciones recomendadas:

- `feat/<nombre>`
- `fix/<nombre>`
- `chore/<nombre>`

Plantillas y apoyo:

- [playbooks/github-setup.md](/Users/antonio/Codex/template/playbooks/github-setup.md)
- [.github/PULL_REQUEST_TEMPLATE.md](/Users/antonio/Codex/template/.github/PULL_REQUEST_TEMPLATE.md)

## Casos de uso incluidos

La plantilla ya incluye ejemplos de especificación en:

- [specs/example-ios-app/README.md](/Users/antonio/Codex/template/specs/example-ios-app/README.md)
- [specs/example-odoo-module/README.md](/Users/antonio/Codex/template/specs/example-odoo-module/README.md)

## Archivos importantes

- [AGENTS.md](/Users/antonio/Codex/template/AGENTS.md): reglas globales del repositorio
- [docs/openai-notes.md](/Users/antonio/Codex/template/docs/openai-notes.md): resumen de las notas aplicadas desde la documentación oficial
- [playbooks/new-project.md](/Users/antonio/Codex/template/playbooks/new-project.md): guía rápida para iniciar un proyecto nuevo

## Primeros pasos

```bash
git checkout -b feat/mi-primer-proyecto
```

```text
Crea el proyecto <nombre> dentro de domains/<dominio>/projects/<nombre> usando el spec specs/<nombre>/README.md. Respeta el AGENTS.md de la raíz y el del dominio.
```

## Referencias

- `agents.md`: https://agents.md
- guía de OpenAI sobre `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- integración de Codex con GitHub: https://developers.openai.com/codex/integrations/github

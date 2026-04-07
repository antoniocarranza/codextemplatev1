# AGENTS.md

## Rol

Eres el agente especializado en desarrollo iOS para Apple.

## Stack obligatorio

- Swift 5.9+ o compatible con la versión estable disponible
- SwiftUI como tecnología principal de UI
- MVVM como patrón de presentación
- UIKit solo cuando aporte una integración concreta necesaria
- Xcode como entorno objetivo

## Estructura esperada

- `projects/<nombre>/App/`
- `projects/<nombre>/Features/`
- `projects/<nombre>/Core/`
- `projects/<nombre>/Resources/`
- `projects/<nombre>/Tests/`

## Reglas de arquitectura

- Cada pantalla debe tener `View`, `ViewModel` y, cuando aplique, `Model`.
- La lógica de negocio no debe vivir en la `View`.
- Las dependencias compartidas deben ir en `Core/`.
- Wrappers de UIKit deben ser mínimos y estar justificados.
- Evitar acoplar vistas a servicios concretos.

## Validación mínima

- El código debe compilar con Xcode o `swiftc -typecheck` cuando proceda.
- Añadir pruebas unitarias para `ViewModel`, servicios y lógica transformadora.
- Si se añade navegación o estado complejo, documentar el flujo.

## Estilo

- Nombres claros y orientados al dominio.
- Preferir `struct` frente a `class` salvo necesidad de referencia.
- Evitar lógica de red dentro de `ViewModel`; usar servicios.

## Salida esperada

Cuando crees un nuevo proyecto, genera al menos:

- estructura de carpetas
- app entry point
- una feature inicial
- un servicio de ejemplo
- pruebas base

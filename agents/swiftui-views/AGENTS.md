# AGENTS.md

## Rol

Agente especialista en crear vistas con SwiftUI.

## Ámbito

- vistas SwiftUI
- componentes reutilizables
- composición visual
- estados de preview para Xcode

## Reglas

- Toda vista creada debe incluir `#Preview`.
- Las vistas deben ser reutilizables, pequeñas y con una sola responsabilidad visual.
- Extraer subcomponentes cuando una vista empiece a mezclar demasiadas secciones o variantes.
- Evitar lógica de negocio compleja dentro de la vista.
- Recibir dependencias y estado desde fuera siempre que sea razonable.
- Usar nombres claros para vistas, subviews y propiedades de configuración.

## Convenciones

- Si la vista necesita datos de ejemplo, crear mocks simples solo para `#Preview`.
- El `#Preview` debe mostrar una configuración representativa del componente.
- Si existen varios estados visuales relevantes, incluirlos dentro del mismo bloque de preview cuando aporte claridad.
- Mantener los modificadores y layout legibles; extraer piezas repetidas a componentes o helpers visuales.

## Validación

- La vista debe ser compilable en Xcode cuando el entorno lo permita.
- Toda vista nueva debe poder visualizarse en el IDE mediante `#Preview`.

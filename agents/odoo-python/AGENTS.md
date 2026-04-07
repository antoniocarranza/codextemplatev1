# AGENTS.md

## Rol

Agente especialista en backend Python para Odoo.

## Ámbito

- integración con Odoo v16
- XML-RPC
- servicios backend
- configuración por entorno

## Reglas

- Separar configuración, cliente, servicios y casos de uso.
- No mezclar llamadas XML-RPC crudas con lógica de negocio.
- No hardcodear credenciales ni endpoints.
- Preferir código explícito, tipado cuando ayude y funciones pequeñas.

## Validación

- Verificar imports y sintaxis.
- Añadir pruebas unitarias para piezas críticas.

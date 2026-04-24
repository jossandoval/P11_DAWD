# P11_DAWD

Este repositorio contiene la práctica de pruebas unitarias realizadas en Angular y Python.

## Contenido

- `main.tex`: Informe de la práctica con portada original.
- `angular-app/`: Proyecto Angular con prueba unitaria de conexión a un web service.
- `python-app/`: Módulo Python y prueba unitaria para la conexión a una base de datos SQLite.

## Reproducibilidad

### Requisitos

- Node.js 16+ y npm
- Python 3.7+
- Git

### Angular

1. Abre una terminal en `angular-app`:
   ```bash
   cd angular-app
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Ejecuta las pruebas unitarias:
   ```bash
   npx ng test --watch=false
   ```

### Python

1. Abre una terminal en `python-app`:
   ```bash
   cd python-app
   ```
2. Ejecuta las pruebas unitarias:
   ```bash
   python -m unittest test_database.py -v
   ```

## Descripción breve

- Angular: `src/app/web.service.ts` implementa un servicio que prueba la conexión a un web service.
- Angular: `src/app/app.spec.ts` contiene la prueba unitaria del componente que valida la conexión.
- Python: `database.py` implementa la clase de conexión a SQLite.
- Python: `test_database.py` contiene la prueba unitaria en un archivo separado.

## Notas

- El reporte original se conserva en `main.tex` y puede compilarse en Overleaf.
- Se recomienda ejecutar primero `npm install` dentro de `angular-app` antes de correr los tests de Angular.

# Laboratorio Semana 02 - Análisis de Algoritmos

## Gestión del Entorno Virtual (Windows / PowerShell)

Para aislar las dependencias de esta sesión, se creó un entorno virtual local siguiendo estos pasos:

1. **Creación:** Se generó la carpeta del entorno ejecutando `python -m venv venv` dentro del directorio `semana-02`.
2. **Activación:** Se habilitó el entorno con el comando `.\venv\Scripts\activate`. Se verificó visualmente la aparición del prefijo `(venv)` en la consola antes de proceder con las instalaciones.
3. **Reproducibilidad:** Para que otro desarrollador reconstruya este mismo entorno con las versiones exactas de las librerías (`matplotlib` y sus dependencias), debe crear y activar su propio entorno vacío y luego ejecutar:
   `pip install -r requirements.txt`
# Laboratorio 02 — Configuración del entorno de trabajo

## Propósito

Configurar un entorno virtual de Python reproducible para el desarrollo de los laboratorios del semestre.

## Configuración del entorno

El entorno virtual se creó dentro de la carpeta `ejercicios-clase/semana-02/` del repositorio del curso.

1. Crear el entorno virtual:

```bash
python -m venv venv
```

2. Activar el entorno en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Al activarlo correctamente, la terminal muestra el prefijo `(venv)`:

```text
(venv) PS ...\ejercicios-clase\semana-02>
```

3. Verificar el entorno antes de instalar dependencias:

```powershell
pip list
```

El entorno recién creado contiene únicamente las herramientas básicas, por lo que se encuentra aislado de las dependencias del sistema.

4. Instalar `matplotlib` dentro del entorno virtual:

```powershell
pip install matplotlib
```

5. Generar el archivo de dependencias:

```powershell
pip freeze > requirements.txt
```

6. Reproducir el entorno en una instalación limpia:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

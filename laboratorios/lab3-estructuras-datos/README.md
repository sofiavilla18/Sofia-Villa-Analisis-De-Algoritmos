# Curso de Análisis de Algoritmos 2026-1
## Laboratorio evaluativo 03 — Estructuras de datos
### Estudiante: Sofia Villa Muñoz


## Instrucciones para reproducir el experimento
Para reproducir correctamente el entorno del laboratorio, siga los siguientes pasos:

1. Abra una terminal dentro de la carpeta lab3-estructuras-datos y cree el entorno virtual:
### Windows
```bash
    python -m venv venv
    venv\Scripts\activate
```
### Linux / macOS
```bash
    python3 -m venv venv
    source venv/bin/activate    
```

2. Con el entorno virtual activado, instale las dependencias del proyecto mediante el archivo requirements.txt:
```bash
    pip install -r requirements.txt
```

3. Ejecute el archivo pruebas.py para validar el correcto funcionamiento de los métodos:
```bash
    python pruebas.py
```

4. Ejecute el archivo de medicion.py para las mediciones de tiempo y generación de las gráficas:
```bash
    python medicion.py
```
## Parte 1 — Descripción de validación de estructuras y casos cubiertos.

### Código de las estructuras de datos: [estructuras.py](estructuras.py)
### Pruebas: [pruebas.py](pruebas.py)

Para validar las estructuras implementadas, se realizaron diferentes pruebas mediante instrucciones assert, con el propósito de comprobar que la lista enlazada y la tabla hash devolvieran los resultados esperados al consultar las guías de envío.

En primer lugar, se verificaron búsquedas exitosas e infructuosas en ambas estructuras. Para las búsquedas exitosas, se comprobó que cada guía almacenada devolviera su estado correspondiente. Para las infructuosas, se verificó que una guía inexistente devolviera None.

También se evaluó el manejo de colisiones en la tabla hash utilizando m = 7 y las guías 10, 24 y 17. Como las tres producen el índice 3 mediante la función hash por división, se comprobó que pudieran insertarse y buscarse correctamente, que la lista enlazada de esa casilla contuviera tres nodos y que el factor de carga fuera 3 / 7.

Finalmente, se realizaron veinte colecciones aleatorias para comparar los resultados de búsqueda de ambas estructuras. Se verificó que las guías existentes devolvieran el mismo estado en la lista y en la tabla, y que las guías inexistentes no fueran encontradas. Para facilitar la reproducción de las pruebas, se utilizó una semilla fija (42) en la generación de los datos aleatorios, de modo que las colecciones pudieran generarse nuevamente siguiendo la misma secuencia.

## Parte 2 — Medir y graficar
### Código de medición: [medicion.py](medicion.py)

![Lista vs tabla parte 2](graficas/lista_vs_tabla.png)
![Tiempo vs alfa 2](graficas/tiempo_vs_alfa.png)
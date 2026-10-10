# Curso de Análisis de Algoritmos 2026-1
## Laboratorio evaluativo 02 — Dividir y vencer
### Estudiante: Sofia Villa Muñoz


## Instrucciones para reproducir el experimento
Para reproducir correctamente el entorno del laboratorio, siga los siguientes pasos:

1. Abra una terminal dentro de la carpeta lab2-divide-y-vencer y cree el entorno virtual:
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

4. Ejecute el archivo de medicion.py para las mediciones de tiempo y generación de la gráfica "Tiempo vs n":
```bash
    python medicion.py
```

## Parte 1 — Validación de soluciones y casos cubiertos.

### Algoritmo subarreglo: [subarreglo.py](subarreglo.py)
### Pruebas: [pruebas.py](pruebas.py)

Se implementaron dos soluciones para encontrar el subarreglo de mayor suma: una mediante fuerza bruta y otra mediante divide y vencerás. Ambas fueron validadas con el archivo de [pruebas.py](pruebas.py), las cuales resultaron esenciales para comprobar el comportamiento de las soluciones antes de llevar a cabo las mediciones del rendimiento. 

Para ello, se utilizaron instrucciones assert, que comprueban si la suma obtenida coincide con el resultado esperado. Se evaluaron los siguientes seis casos:

1. Serie del enunciado: se utilizó la serie [-3, 5, -2, 8, -6, 3, 9, -4] para comprobar que ambos algoritmos identifican una suma máxima de 17, correspondiente al tramo comprendido entre los días 2 y 7.

2. Serie con un solo elemento: se evaluó la lista [7] para verificar que ambos algoritmos reconocen que el único elemento constituye el mejor subarreglo y que su suma máxima es 7. Este caso comprueba el comportamiento de la condición base de la solución recursiva.

3. Serie con todos los valores negativos: se utilizó la lista [-5, -2, -8, -3] para comprobar que ambos algoritmos seleccionan el elemento menos negativo, -2, en lugar de devolver una suma incorrecta o asumir que la mejor suma es cero.

4. Serie con todos los valores positivos: se probó la lista [2, 4, 1, 3] para verificar que la suma máxima es 10, resultado de acumular todos los elementos de la serie.

5. Mejor subarreglo que cruza el punto medio: se utilizó la lista [-5, 4, -1, 3, -2] para comprobar que ambos algoritmos encuentran la suma máxima de 6, correspondiente al tramo [4, -1, 3]. Este caso permite verificar que divide y vencerás considera correctamente los subarreglos que comienzan en una mitad y terminan en la otra.

6. Listas aleatorias: se generaron 20 listas de longitudes entre 1 y 30, con valores enteros entre -100 y 100. Se fijó la semilla aleatoria en 42 para que las pruebas puedan reproducirse con los mismos datos. En cada lista se compararon las sumas máximas obtenidas por ambos algoritmos, comprobando que coincidan.




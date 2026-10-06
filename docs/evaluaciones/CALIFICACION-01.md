# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Sofia Villa Muñoz · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `801edf3`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre un algoritmo correcto y uno viable, y nombra la restricción que Tamiza incumple: la ventana de cuatro horas.
- Da un segundo ejemplo propio (los formularios de salud de su práctica) con una cantidad aproximada de datos y un límite de 2 segundos.
- Identifica dos perjuicios (el paciente y el operador del centro de contacto) y dice quién asume el costo de cada uno.
- Explica la tensión de que el orden decide a quién se llama primero.

**Lo que puede mejorar:**
- Al explicar por qué duplicar el servidor no basta, se queda en "el trabajo sigue siendo el mismo". Falta decir que al crecer los datos el tiempo crece mucho más rápido que la velocidad que se gana.
- En la parte ambiental no relaciona el tiempo de ejecución con una idea concreta de energía (por ejemplo, horas de servidor encendido por año).

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define los tres casos sobre un tamaño fijo `n`, justifica que usaría el peor caso para decidir si entra en producción y deja escrita su predicción antes de medir.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y la resuelve con el método maestro: identifica `a = 2`, `b = 2`, compara `f(n)` con `n^(log_2 2) = n`, verifica el caso 2 y concluye `Θ(n log n)`.
- Incluye la tabla de complejidades de los dos algoritmos.

**Lo que puede mejorar:**
- En el análisis línea a línea de insertion sort, para el caso promedio solo escribe "proporcional a n²". Falta sumar los costos y mostrar cómo se llega a `n(n-1)/2` y a la cota final.
- Aclare por qué el caso promedio también es cuadrático (en promedio cada elemento se desplaza la mitad del camino).

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista recibida y cuentan solo comparaciones entre elementos (en una lista ya ordenada insertion sort hace exactamente `n - 1`).
- No usa `sorted()` ni `list.sort()`, y `merge_sort` tiene su propia mezcla recursiva.
- Los generadores usan semilla, producen valores distintos y el escenario B realmente deja el 2 % desordenado al final.

**Lo que puede mejorar:**
- En `algoritmos.py` quedó la línea `from pandas import merge`. No se usa (su propia función `merge` la reemplaza) y obliga a tener instalada una librería que no hace falta. Debe borrarla.
- Las funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen *docstrings* y varias no tienen *type hints* completos.
- Hay varios avisos de estilo PEP 8, como la falta de líneas en blanco entre funciones. Quedaron además los comentarios `TODO` de la plantilla.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con cifras que C es el peor caso, B el mejor y A el intermedio, y contrasta con su predicción.
- En 4.2 describe lo que hace cada curva y lo relaciona con `Θ(n²)` y `Θ(n log n)`.
- En 4.3 recomienda merge sort, hace la extrapolación (unas 7.9 horas para insertion sort y unos 4 segundos para merge sort), la declara como estimación y menciona la memoria extra.

**Lo que puede mejorar:**
- Los tiempos que cita para n = 6400 (por ejemplo 0.806 s) no coinciden con los de la gráfica publicada (cerca de 0.94 s). Cite siempre lo que muestra la gráfica entregada.
- Diga de forma explícita si cada algoritmo cabe o no en las cuatro horas.
- Al responder sobre el servidor del doble de velocidad, use su dato: con la mitad del tiempo, insertion sort seguiría rondando las 4 horas, sin margen.
- La explicación de los tamaños pequeños es general; apóyela en sus propios números.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida y hay más de cinco commits descriptivos.
- Hay instrucciones de reproducción y enlaces a `algoritmos.py`, `datos.py` y a los archivos de cada parte.

**Lo que puede mejorar:**
- No siguió los nombres del entregable: la gráfica se llama `parte3_tiempos.png` y debía ser `parte3_tiempo.png`.
- Las imágenes del informe usan direcciones completas de GitHub y no rutas relativas a la carpeta del `README.md`, así que pueden no verse.
- Las instrucciones piden instalar un `requirements.txt` que no existe en la carpeta del laboratorio, y el comando para activar el entorno solo sirve en Windows.
- Los títulos de los enlaces de la Parte 3 y 4 no corresponden con lo que enlazan (por ejemplo, "Datos utilizados" apunta al script de la parte y "parte4_casos.py" al archivo `parte4_complejidad.py`).

## ¿El código funciona?
Sí. Los scripts corren, los algoritmos ordenan bien y generan las gráficas. Solo depende de `pandas` por la línea sobrante, que no debería necesitarse.

## Para el próximo laboratorio
- Revise los imports antes de entregar y elimine los que no use.
- Agregue *docstrings* y *type hints* a todas las funciones, también a las de apoyo, y corra una revisión de estilo PEP 8.
- Use exactamente los nombres de archivos y carpetas del entregable e incluya su `requirements.txt` en la carpeta del laboratorio.
- Incruste las imágenes con rutas relativas y compruebe en GitHub que se ven.
- Desarrolle los cálculos completos (sumas de costos línea a línea) y cite en el informe las mismas cifras que muestran sus gráficas.

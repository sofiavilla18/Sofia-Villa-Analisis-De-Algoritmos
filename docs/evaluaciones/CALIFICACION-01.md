# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Sofia Villa Muñoz · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `7cdee42`

Muy buen trabajo: su informe está completo, sus cálculos son correctos y sus conclusiones se apoyan en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 16 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **87 / 100** |
| **Nota (0–5)** | **4.35** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica que un servidor el doble de rápido no cambia el crecimiento del trabajo de insertion sort.
- Su ejemplo propio (formularios de salud, unos 5.000 al día, respuesta en menos de 2 segundos) tiene datos y una restricción clara.
- Señala dos perjuicios concretos (paciente que se llama tarde y operador con lista incompleta) e indica quién asume el costo de cada uno. También explica la obligación extra que impone que el orden decida a quién se llama primero.

**Lo que puede mejorar:**
- La parte ambiental queda corta: calcula las 1.460 horas de servidor al año, pero no explica con más detalle cómo ese tiempo se vuelve energía gastada y cómo se acumula durante varios años.
- El ejemplo propio podría decir cuántos pasos o validaciones hace cada formulario para justificar mejor por qué tarda más de lo permitido.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define los tres casos con un tamaño fijo n, escribe su predicción antes del experimento y justifica que usaría el peor caso para decidir si el algoritmo entra en producción.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro: identifica a, b y f(n), compara con n^(log_b a) y concluye Θ(n log n) por el caso 2.
- Hace el análisis de insertion sort línea por línea, con sumas para el peor caso y el caso promedio, y deja la tabla de complejidades.

**Lo que puede mejorar:**
- En la tabla línea por línea falta la línea del `while`, y no se suman los costos de todas las líneas para llegar al total final.
- Al definir el caso promedio, diga sobre qué conjunto de entradas se promedia y qué supone (por ejemplo, que todos los órdenes posibles son igual de probables).

## 3. Corrección de la implementación (16 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor, de forma consistente), no cambian la lista recibida y cuentan solo comparaciones entre elementos. `merge_sort` tiene su propia mezcla recursiva y no usa funciones de ordenamiento de Python.
- Los tres generadores producen listas de n valores distintos, con semilla reproducible. El escenario B deja el 98 % ordenado y el 2 % desordenado al final.

**Lo que puede mejorar:**
- Hay faltantes de estilo: líneas en blanco de más en `algoritmos.py` y `datos.py`, y falta una línea en blanco antes de una función en `datos.py`.
- En `merge_sort` el resumen del docstring queda pegado al siguiente párrafo, sin línea en blanco.
- `parte3_casos.py` y `parte4_complejidad.py` no tienen docstring de módulo. Algunos parámetros (`generador`, `algoritmo`, `resultados`) no tienen *type hints*, y las funciones de graficar de la Parte 3 no indican el tipo de retorno.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes con unidades y leyenda. Las dos de la Parte 3 muestran los tres escenarios en los mismos ejes, y la de la Parte 4 muestra una curva por algoritmo.
- Identifica con datos que C es el peor caso, B el mejor y A el intermedio, y lo contrasta con su predicción. Las comparaciones del informe coinciden con la gráfica `parte3_comparaciones.png` (el escenario C llega a unos 20 millones en n = 6400).
- En 4.2 describe lo que hace cada curva y lo relaciona con Θ(n²) y Θ(n log n). También nota que con tamaños pequeños ambas curvas son casi iguales y que la diferencia aparece al crecer n.
- El concepto técnico recomienda merge sort, estima el tiempo para 1.200.000 registros (unas 7,87 horas contra unos 3,66 segundos) y lo declara como estimación. Responde a la propuesta del servidor con un dato medido y menciona la memoria extra de merge sort.

**Lo que puede mejorar:**
- Algunos tiempos de la Parte 3.2 no coinciden del todo con lo que muestra `parte3_tiempo.png` en n = 6400. Por ejemplo, el escenario B se cita con 0,077 s y en la gráfica está cerca de 0,06 s; el escenario A se cita con 0,827 s y en la gráfica está cerca de 0,79 s.
- No explica cómo midió: cada tiempo viene de una sola corrida y no lo dice. Repetir cada medición y usar el promedio reduce el ruido.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab1-fundamentos-complejidad-recurrencias/` es una ubicación válida y tiene todos los archivos del entregable.
- El informe está en el orden pedido, con las gráficas incrustadas (las rutas funcionan), enlaces al código en las Partes 3 y 4 y un historial de más de cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- En las instrucciones de reproducción, los comandos aparecen con un guion al inicio dentro de los bloques de código, así que no se pueden copiar y pegar tal cual.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan bien en mis pruebas, y los dos scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Repita cada medición varias veces, use el promedio y diga en el informe cómo midió.
- Revise que las cifras que cita coincidan con lo que se ve en sus gráficas.
- Pase una revisión de estilo (PEP 8) y complete los *type hints* y *docstrings* en todas las funciones y archivos.
- En las explicaciones teóricas, escriba todos los pasos (por ejemplo, sumar los costos de todas las líneas) y los supuestos del caso promedio.
- Explique con más detalle la relación entre tiempo de ejecución y consumo de energía.

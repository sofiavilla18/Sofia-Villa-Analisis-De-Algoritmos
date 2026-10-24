# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Sofia Villa Muñoz · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `ba70bd2`

Excelente trabajo: el código es correcto y el informe responde las cinco preguntas con sus propios datos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Comparó con el problema del máximo de un arreglo y justificó con el costo de combinar `Θ(1)` y la recurrencia `T(n) = 2T(n/2) + Θ(1)`.
- Recomendó divide y vencerás y estimó el tiempo para 1.000.000 de registros usando `n²` y `n log n`, declarando que es una estimación.

**Lo que puede mejorar:**
- Dice que divide y vencerás empieza a ganar desde n = 50, pero lo sustenta con una sola medición muy pequeña. Con tiempos tan cortos el ruido es grande; conviene repetir la medición antes de afirmar un punto de cruce.
- La explicación de por qué pierde con n pequeño es correcta pero breve; podría apoyarla con más tamaños pequeños.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Planteó la recurrencia `T(n) = 2T(n/2) + Θ(n)` explicando los dos subproblemas y el costo lineal del caso cruzado.
- Aplicó el método maestro (a = 2, b = 2, `n^(log₂2) = n`) y justificó `Θ(n²)` en la fuerza bruta con `n(n+1)/2` subarreglos.

**Lo que puede mejorar:**
- Al decir que se cumple el caso 2, indique de forma explícita la condición que se verifica (`f(n) = Θ(n^(log_b a))`) y concluya con ella paso a paso.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no modifican la lista recibida.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- Código ordenado, con *type hints* y *docstrings* en cada función.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- Gráfica con título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calculó el factor al duplicar n (4000 a 8000): 3,84 para fuerza bruta y 1,60 para divide y vencerás, y lo comparó con lo esperado.

**Lo que puede mejorar:**
- El factor 1,60 queda por debajo de lo esperado (cerca de 2) y lo explicó solo con "condiciones de ejecución". Repetir las mediciones y usar la mediana ayudaría a darle una explicación más sólida.
- Cada medición se hizo una sola vez; lo declaró, pero con esto los tiempos son poco confiables.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura correcta (`laboratorios/lab2-divide-y-vencer/`), informe en el orden pedido, gráfica visible, enlaces al código en cada parte, instrucciones de reproducción y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores, el experimento corre completo, verifica que ambos algoritmos den la misma suma y genera la gráfica.

## Para el próximo laboratorio
- Repita cada medición varias veces y use el promedio o la mediana.
- Agregue una tabla con los valores medidos para poder leer los tamaños pequeños.
- Sustente los puntos de cruce con varios tamaños pequeños, no con una sola medición.
- Al aplicar el método maestro, escriba explícitamente la condición del caso que se cumple.

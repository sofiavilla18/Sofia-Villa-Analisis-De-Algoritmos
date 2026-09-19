# Curso de Análisis de Algoritmos 2026-1
## Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
### Estudiante: Sofia Villa Muñoz


## Intrucciones para reproducir el experimento

## Parte 1 — Respuesta argumentativa.
Antes de realizar este proceso la secretaria de salud departamental debe priorizar el análisis del algoritmo a profundidad, debido a una pequeña distinción, que un algoritmo sea correcto y cumpla con su labor esperada no significa que sea viable para las condiciones actuales que presenta el sistema. La plataforma Tamiza es un ejemplo de esto, donde insertion sort es correcto por que lleva a cabo su función, la cual es ordenar los 1.200.000 registros correspondientes por índice de riesgo para generar la lista de llamadas, teniendo en cuenta la prioridad a pacientes con mayor riesgo. No obstante, el problema que se ha generando en la ultimas semanas con la aplicación a todo el departamento es que el proceso ya no alcanza a terminar en el tiempo establecido entre las 2:00 am y 6:00 am ocasionando hasta el uso de una lista parcial, no ordenada por riesgo. Por lo tanto, aunque el resultado sea el correcto cuando finaliza la ejecución, está incumpliendo la ventana máxima de cuatro horas establecida para completar el proceso.

Luego de considerar esta situación, se considera la decisión de comprar un servidor con doble de velocidad para que cumpla con los tiempos necesarios algo cuestionable, debido a que es cierto que la velocidad del servidor podría reducir sus tiempos de ejecución, pero no solucionaría el problema de fondo. La plataforma Tamiza continuara realizando la misma cantidad de trabajo sobre los 1.200.000 registros, algo fundamental de entender, ya que, al aumentar el tamaño de los datos, puede incluso incrementar significativamente el trabajo que debe realizar el algoritmo. Por esto, antes de invertir en Hardware, es fundamental el análisis del algoritmo frente al tamaño de entrada. O como los llama Cormen, los algoritmos como una tecnología, debido a que la elección de este puede generar repercusiones medibles en tiempo, dinero y capacidad.

Un ejemplo particular desde la experiencia es la empresa Cielum en la que realice mis prácticas, esta manejaba un sistema de formularios de salud con muchas reglas de flujo y de diseño. Para plantear una situación concreta, supongamos que el aplicativo debía procesar aproximadamente un alrededor de 5.000 formularios al día. Lo que ocasionaba que un mismo formulario podría tener numerosos condicionales que determinaban que preguntas mostrar u ocultar, y dependiendo de estas, que acciones realizar, como lo es él envió de una alerta o de correos electrónicos. Aunque el sistema aplicara correctamente cada una de las reglas, si una interacción tardara mas de 2 segundos por la cantidad de validaciones y acciones que debe ejecutar, podría incumplir con la latencia esperada por el usuario. Para este caso, el algoritmo sería correcto puesto que produce las acciones esperadas, pero algo inviables frente a la restricción de tiempo de respuesta por parte del usuario. 

## Parte 2 — Respuesta argumentativa.
La plataforma Tamiza, aparte de algoritmos y datos, maneja una gran responsabilidad ética y ambiental, la cual se ve reflejada en el tiempo que tarda el algoritmo en ejecutarse, relacionándose directamente con el uso de recursos computacionales para realizar sus operaciones diarias. Para el aplicativo, el ordenamiento de los 1.200.000 registros se ejecuta todas las madrugadas y actualmente supera la ventana establecida entre las 2:00 a. m. y las 6:00 a. m. Por lo tanto, entre más tiempo permanezca ejecutándose este proceso, durante más tiempo se estarán utilizando estos recursos. A pesar de que no se cuenta con datos específicos sobre el consumo energético del servidor de Tamiza, sí se puede entender que este se acumula con la repetición constante del algoritmo todas las madrugadas durante varios años, convirtiendo una diferencia en el tiempo de ejecución diario en un impacto ambiental acumulado a largo plazo.

En cuanto al apartado ético y moral, el problema tiene una importancia mayor porque los registros representan personas y el índice de riesgo determina el orden en el que estas serán contactadas. La primera consecuencia se presenta cuando la lista queda desordenada, ocasionando que un paciente con un índice de riesgo mayor pueda ser contactado después de otro con un riesgo menor. Para este caso, el costo del error lo asume principalmente el paciente, ya que su prioridad de contacto puede verse afectada.

Una segunda consecuencia se genera cuando a las 6:00 a. m. la lista se encuentra aún incompleta. El operador del centro de contacto recibe una lista que no contiene todos los registros que deberían estar disponibles para el inicio de las llamadas durante la jornada de trabajo y, además, no cuenta con el orden de prioridad esperado. En este caso, el costo operativo recae sobre el operador, ya que debe trabajar con un resultado que no cumple con las condiciones establecidas para el proceso.

Lo anterior plantea una tensión fundamental en la plataforma Tamiza, ya que el orden no representa únicamente una tarea técnica, porque el resultado define a quién se llama primero. Por esta razón, el planteamiento de un nuevo algoritmo tiene una responsabilidad adicional. No es suficiente con que los registros queden ordenados; la lista debe quedar correctamente ordenada y disponible dentro de la ventana establecida de tiempo para que esta prioridad pueda cumplirse adecuadamente.

## Parte 3

### Algoritmo insertion sort: [algoritmos.py](https://github.com/sofiavilla18/Sofia-Villa-Analisis-De-Algoritmos/blob/main/laboratorios/lab1-fundamentos-complejidad-recurrencias/algoritmos.py)
### Logíca implementada: [datos.py](https://github.com/sofiavilla18/Sofia-Villa-Analisis-De-Algoritmos/blob/main/laboratorios/lab1-fundamentos-complejidad-recurrencias/datos.py)
### Datos utilizados: [parte3_casos.py](https://github.com/sofiavilla18/Sofia-Villa-Analisis-De-Algoritmos/blob/main/laboratorios/lab1-fundamentos-complejidad-recurrencias/parte3_casos.py)

## Parte 3.1 Explicación 
Para esta sección, se dará una breve explicación de los casos posibles, además de la elección de uno de estos para el caso en el que el algoritmo de Tamiza entra en producción. 

- Mejor caso:  Este ocurre cuando, para un tamaño fijo n, el arreglo se encuentra ordenado según el orden que necesita producir insertion sort. Para este caso, la condición del ciclo while resulta falsa desde la primera comparación entre elementos, por lo que no necesita realizar desplazamientos.

- Peor caso: En este caso, el arreglo está ordenado exactamente al contrario del orden requerido, para un tamaño fijo de n. Además, cada uno de sus elementos debe desplazarse a través de todos los elementos que ya están ordenados a su izquierda, lo que requiere una mayor cantidad de comparaciones y desplazamientos.

- Caso promedio: Corresponde al comportamiento promedio de insertion sort sobre un conjunto de entradas de tamaño fijo n. Para este tipo de entradas, se espera que cada elemento deba desplazarse aproximadamente hasta la mitad de la parte que ya está ordenada.

- Caso para producción: Teniendo en cuenta que el aplicativo de Tamiza tiene una ventana estricta de cuatro horas, es fundamental prestar atención al peor caso, ya que permite comprobar el comportamiento del algoritmo ante una entrada válida que exija la mayor cantidad de trabajo. Si en ese escenario el algoritmo tarda más de cuatro horas y supera la ventana de 2:00 a. m. a 6:00 a. m., existe el riesgo de que el proceso no esté disponible en el tiempo acordado.

El caso de análisis que representa cada escenario de Tamiza para insertion sort es:

- Escenario A: Representa los registros que llegan mediante las cargas de la plataforma web sin un orden específico. Al no existir un orden previo entre los índices de riesgo, se espera que el algoritmo realice una cantidad intermedia de comparaciones y desplazamientos. Por esta razón, se considera que este escenario se aproxima al caso promedio.

- Escenario B: Representa la situación en la que la mayor parte de los registros conserva el orden de la lista del día anterior y solamente se agregan nuevos registros al final. Debido a que insertion sort funciona de manera favorable cuando los datos se encuentran ordenados o casi ordenados, se espera que este sea el escenario mas favorable de los tres y que requiera menos comparaciones y desplazamientos.

- Escenario C: Representa el caso en que los registros están ordenados exactamente al contrario del orden que Tamiza necesita para generar la lista de llamadas. En esta situación, los elementos deben desplazarse a través de gran parte de los elementos que ya se encuentran ordenados, por lo que se espera la mayor cantidad de comparaciones y desplazamientos. Por esta razón, se predice que este escenario corresponde al peor caso.

## Parte 3.2  Demostración experimental

Luego de realizar la demostración experimental, los resultados obtenidos fueron los siguientes: el escenario C fue el peor caso, ya que presentó el mayor número de comparaciones, con 20.476.800, y el mayor tiempo de ejecución, con 1.559084 s, para un n = 6400. Además, se observó que tanto el número de comparaciones como el tiempo de ejecución aumentaron a medida que crecía el tamaño de la entrada. Para el escenario B, este fue el mejor de los tres, puesto que obtuvo considerablemente menos comparaciones, con 813.455, y un menor tiempo de ejecución de 0.076926 s para n = 6400. Finalmente, el escenario A presentó un comportamiento intermedio, aproximándose al caso promedio, con 10.276.753 comparaciones y un tiempo de ejecución de 0.827344 s.

Estos resultados experimentales coinciden con las predicciones realizadas, donde se esperaba que el escenario B fuera el más favorable, el escenario A representara un comportamiento promedio y el escenario C correspondiera al peor caso.

### Gráfica: Comparaciones vs Tamaño de Entrada
![image alt](https://github.com/sofiavilla18/Sofia-Villa-Analisis-De-Algoritmos/blob/main/laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte3_comparaciones.png)

### Gráfica: Tiempo vs Tamaño de Entrada
![image alt](https://github.com/sofiavilla18/Sofia-Villa-Analisis-De-Algoritmos/blob/main/laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte3_tiempos.png)

## Parte 4

## Parte 4.1 Cálculo teórico

Para el análisis de merge sort, se parte de la siguiente recurrencia: 

T(n) = 2T(n/2) + Θ(n)

La cual representa el trabajo realizado por el algoritmo sobre una entrada de tamaño (n).En primer lugar, merge sort divide el problema original en dos subproblemas (2T(n/2)). Cada uno de estos tiene aproximadamente la mitad del tamaño de la entrada original (n/2).

Luego de ordenar las dos mitades de forma recursiva, el algoritmo debe combinarlas mediante la operación merge. Esta recorre los elementos de ambas partes para constituir una única lista ordenada. Teniendo en cuenta que como conjunto se deben procesar aproximadamente los (n) elementos, el costo de esta combinación es lineal, representado por Θ(n).

Para resolverla se hace la elección del método maestro, ya que la recurrencia tiene directamente la forma general:

T(n)=aT(n/b)+f(n)

Para nuestro caso:
- a= 2 
- b=2

Además, el costo de combinar las dos mitades corresponde a f(n)=Θ(n).

Se compara el costo de dividir recursivamente el problema con el costo de combinar los resultados, por lo tanto, se realiza la sustitución de los valores obtenidos.

n^(log_b(a)) = n^(log_2(2)) = n^1=n

Por lo cual, la función que se debe comparar es:
f(n)=Θ(n) con n^(log_b(a)) = n

Ambas tienen el mismo orden de crecimiento ya que f(n)=Θ(n) = Θ(n^(log_b(a))), por esta razón, la recurrencia corresponde al caso dos del método maestro, este establece que cuando f(n) tiene el mismo orden que n^(log_b(a)), la solución a la recurrencia es:

 T(n) = Θ(n log n)

Esto significa que el costo de dividir el problema y combinas las soluciones a lo largo de los niveles de la recursión produce un crecimiento de (n log n).

### Cálculo de cota de Insertion Sort
Para realizar el calculo de la cota de insertion sort, se debe analizar cuantas veces puede ejecutarse cada línea de la implementación.

    arreglo = datos.copy()
    comparaciones = 0

    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if arreglo[j] >= clave:
                break

            arreglo[j + 1] = arreglo[j]
            j -= 1

        arreglo[j + 1] = clave

    return arreglo, comparaciones 

Para una entrada de tamaño (n), las instrucciones que están fuera del ciclo while se ejecutan una cantidad lineal de veces. La diferencia entre los casos aparece principalmente en el comportamiento del ciclo interno.

| Instrucción | Mejor caso | Caso promedio | Peor caso |
|---|---:|---:|---:|
| `arreglo = datos.copy()` | 1 | 1 | 1 |
| `comparaciones = 0` | 1 | 1 | 1 |
| `for i in range(1, len(arreglo))` | `n-1` | `n-1` | `n-1` |
| `clave = arreglo[i]` | `n-1` | `n-1` | `n-1` |
| `j = i - 1` | `n-1` | `n-1` | `n-1` |
| `comparaciones += 1` | `n-1` | proporcional a `n²` | proporcional a `n²` |
| `if arreglo[j] >= clave` | `n-1` | proporcional a `n²` | proporcional a `n²` |
| `arreglo[j + 1] = arreglo[j]` | 0 | proporcional a `n²` | `n(n-1)/2` |
| `j -= 1` | 0 | proporcional a `n²` | `n(n-1)/2` |
| `arreglo[j + 1] = clave` | `n-1` | `n-1` | `n-1` |
| `return arreglo, comparaciones` | 1 | 1 | 1 |

En el mejor caso, los elementos ya están ordenados de mayor a menor. Por ello, en cada iteración del for la primera comparación permite salir del while mediante el break. Se realizan aproximadamente (n-1) comparaciones y no hay desplazamientos, por lo que el crecimiento es de Θ(n).

En el peor caso, los elementos están ordenados de menor a mayor, que es el orden contrario al que necesita producir el algoritmo. Cada nuevo elemento debe desplazarse a través de todos los elementos que ya están ordenados a su izquierda. La cantidad de desplazamientos es de Θ(n^2).

El caso promedio se encuentra entre ambos comportamientos. Los elementos no necesitan desplazarse siempre por toda la parte ordenada, pero sí realizan una cantidad de comparaciones y desplazamientos que crece cuadráticamente con (n). Por esta razón, su complejidad esperada también es de Θ(n^2).

Finalmente la complejidad esperada de cada algoritmo en el mejor, el peor y el caso promedio es de:

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
|---|---:|---:|---:|
| Insertion sort | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ |
| Merge sort | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n\log n)$ |





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





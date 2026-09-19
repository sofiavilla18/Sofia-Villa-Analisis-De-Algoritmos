"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
from pandas import merge


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    # TODO: implemente el algoritmo contando cada comparacion
    # entre dos elementos de la lista.
    
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

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = datos.copy()

    if len(arreglo) <= 1:
        return arreglo, 0

    mitad = len(arreglo) // 2

    izquierda, comparaciones_izquierda = merge_sort(arreglo[:mitad])
    derecha, comparaciones_derecha = merge_sort(arreglo[mitad:])

    resultado, comparaciones_merge = merge(izquierda, derecha)

    comparaciones_totales = (comparaciones_izquierda + comparaciones_derecha + comparaciones_merge)

    return resultado, comparaciones_totales

def merge(izquierda: list[int],derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ordenadas de mayor a menor.

    Compara los elementos al frente de ambas listas y agrega
    primero el de mayor valor.

    Args:
        izquierda: lista ordenada de mayor a menor.
        derecha: lista ordenada de mayor a menor.

    Returns:
        Una tupla con la lista combinada y el numero de
        comparaciones entre elementos realizadas.
    """
    resultado: list[int] = []
    i = 0
    j = 0
    comparaciones = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones
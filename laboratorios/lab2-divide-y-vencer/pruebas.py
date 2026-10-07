"""Pruebas de los algoritmos de subarreglo."""


import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


# Caso 1: serie de ocho dias del enunciado
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17


# Caso 2: un solo elemento
serie = [7]
assert subarreglo_fuerza_bruta(serie)[2] == 7
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 7


# Caso 3: todos los valores negativos
serie = [-5, -2, -8, -3]
assert subarreglo_fuerza_bruta(serie)[2] == -2
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -2


# Caso 4: todos los valores positivos
serie = [2, 4, 1, 3]
assert subarreglo_fuerza_bruta(serie)[2] == 10
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 10


# Caso 5: el mejor subarreglo cruza el punto medio
serie = [-5, 4, -1, 3, -2]
assert subarreglo_fuerza_bruta(serie)[2] == 6
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 6


# Caso 6: listas aleatorias
random.seed(42)

for _ in range(20):
    serie = [
        random.randint(-100, 100)
        for _ in range(random.randint(1, 30))
    ]

    suma_fuerza_bruta = subarreglo_fuerza_bruta(serie)[2]
    suma_divide_y_venceras = subarreglo_maximo(
        serie, 0, len(serie) - 1
    )[2]

    assert suma_fuerza_bruta == suma_divide_y_venceras
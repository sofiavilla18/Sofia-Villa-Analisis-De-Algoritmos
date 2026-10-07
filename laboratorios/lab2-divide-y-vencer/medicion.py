"""Mide y grafica el tiempo de ejecucion de los algoritmos de subarreglo."""

import random
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 500, 1000, 4000, 8000]
SEMILLA = 42


def medir_fuerza_bruta(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de fuerza bruta.

    Args:
        valores: lista de valores sobre la que se ejecuta el algoritmo.

    Returns:
        Tiempo de ejecucion en segundos.
    """
    inicio = time.perf_counter()
    subarreglo_fuerza_bruta(valores)
    fin = time.perf_counter()

    return fin - inicio


def medir_divide_y_venceras(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de divide y venceras.

    Args:
        valores: lista de valores sobre la que se ejecuta el algoritmo.

    Returns:
        Tiempo de ejecucion en segundos.
    """
    inicio = time.perf_counter()
    subarreglo_maximo(valores, 0, len(valores) - 1)
    fin = time.perf_counter()

    return fin - inicio


def generar_datos(tamanos: list[int]) -> list[list[int]]:
    """Genera listas aleatorias reproducibles para las mediciones.

    Args:
        tamanos: tamaños de las listas que se deben generar.

    Returns:
        Lista de listas con valores enteros entre -100 y 100.
    """
    random.seed(SEMILLA)

    return [
        [random.randint(-100, 100) for _ in range(tamano)]
        for tamano in tamanos
    ]


def main() -> None:
    """Ejecuta el experimento y genera la grafica."""
    datos = generar_datos(TAMANOS)

    tiempos_fuerza_bruta = []
    tiempos_divide_y_venceras = []

    print("Resultados de las mediciones:")
    print(
        f"{'n':>6} {'Fuerza bruta (s)':>20} "
        f"{'Divide y venceras (s)':>25}"
    )

    for valores in datos:
        resultado_fuerza_bruta = subarreglo_fuerza_bruta(valores)
        resultado_divide_y_venceras = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )

        assert resultado_fuerza_bruta[2] == resultado_divide_y_venceras[2]

        tiempo_fuerza_bruta = medir_fuerza_bruta(valores)
        tiempo_divide_y_venceras = medir_divide_y_venceras(valores)

        tiempos_fuerza_bruta.append(tiempo_fuerza_bruta)
        tiempos_divide_y_venceras.append(tiempo_divide_y_venceras)

        print(
            f"{len(valores):>6} "
            f"{tiempo_fuerza_bruta:>20.8f} "
            f"{tiempo_divide_y_venceras:>25.8f}"
        )

    plt.figure()
    plt.plot(
        TAMANOS,
        tiempos_fuerza_bruta,
        marker="o",
        label="Fuerza bruta",
    )
    plt.plot(
        TAMANOS,
        tiempos_divide_y_venceras,
        marker="o",
        label="Divide y venceras",
    )

    plt.title("Tiempo de ejecucion vs el tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/tiempo_vs_n.png",
        dpi=300,
        bbox_inches="tight",
    )


if __name__ == "__main__":
    main()
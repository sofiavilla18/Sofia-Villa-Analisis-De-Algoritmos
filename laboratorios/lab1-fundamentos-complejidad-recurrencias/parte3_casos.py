import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_escenario(generador, n: int) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de insertion sort.

    Args:
        generador: función que genera los datos del escenario.
        n: tamaño de la entrada.

    Returns:
        Una tupla con el tiempo de ejecución en segundos y el número
        de comparaciones realizadas.
    """
    datos = generador(n)

    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    tiempo = fin - inicio
    return tiempo, comparaciones


def graficar_comparaciones(resultados):
    """Genera la gráfica del número de comparaciones por escenario.

    Args:
        resultados: resultados del experimento organizados por escenario.
    """
    plt.figure()

    for escenario, datos in resultados.items():
        n = [fila[0] for fila in datos]
        comparaciones = [fila[2] for fila in datos]

        plt.plot(
            n,
            comparaciones,
            marker="o",
            label=f"Escenario {escenario}"
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.title("Comparaciones de insertion sort")
    plt.legend()
    plt.grid(True)

    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()


def graficar_tiempos(resultados):
    """Genera la gráfica del tiempo de ejecución por escenario.

    Args:
        resultados: resultados del experimento organizados por escenario.
    """
    plt.figure()

    for escenario, datos in resultados.items():
        n = [fila[0] for fila in datos]
        tiempos = [fila[1] for fila in datos]

        plt.plot(
            n,
            tiempos,
            marker="o",
            label=f"Escenario {escenario}"
        )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución de insertion sort")
    plt.legend()
    plt.grid(True)

    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()


def main() -> None:
    """Ejecuta el experimento para los tres escenarios."""
    resultados = {"A": [], "B": [], "C": []}

    for n in TAMANOS:
        tiempo_a, comparaciones_a = medir_escenario(generar_aleatorio, n)
        tiempo_b, comparaciones_b = medir_escenario(generar_casi_ordenado, n)
        tiempo_c, comparaciones_c = medir_escenario(generar_inverso, n)

        resultados["A"].append((n, tiempo_a, comparaciones_a))
        resultados["B"].append((n, tiempo_b, comparaciones_b))
        resultados["C"].append((n, tiempo_c, comparaciones_c))

    print("Resultados del experimento:")
    print()

    for escenario, datos in resultados.items():
        print(f"Escenario {escenario}")

        for n, tiempo, comparaciones in datos:
            print(
                f"n={n:4d} | "
                f"tiempo={tiempo:.6f} s | "
                f"comparaciones={comparaciones}"
            )

        print()

    graficar_comparaciones(resultados)
    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()
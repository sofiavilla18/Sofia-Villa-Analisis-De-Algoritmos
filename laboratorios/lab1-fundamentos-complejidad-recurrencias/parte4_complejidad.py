import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_algoritmo(algoritmo, datos: list[int]) -> tuple[float, int]:
    """Mide el tiempo y las comparaciones de un algoritmo de ordenamiento.

    Args:
        algoritmo: función de ordenamiento que se desea medir.
        datos: lista de datos que se utilizará como entrada.

    Returns:
        Una tupla con el tiempo de ejecución en segundos y el número
        de comparaciones realizadas.
    """
    inicio = time.perf_counter()
    _, comparaciones = algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio, comparaciones


def graficar_tiempos(resultados) -> None:
    """Genera una gráfica con los tiempos de ambos algoritmos.

    Args:
        resultados: resultados del experimento para cada tamaño de entrada.
    """
    n = [fila[0] for fila in resultados]
    tiempos_insertion = [fila[1] for fila in resultados]
    tiempos_merge = [fila[3] for fila in resultados]

    plt.figure()

    plt.plot(
        n,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort"
    )

    plt.plot(
        n,
        tiempos_merge,
        marker="o",
        label="Merge Sort"
    )

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución: Insertion Sort vs. Merge Sort")
    plt.legend()
    plt.grid(True)

    plt.savefig("graficas/parte4_tiempo.png")
    plt.close()


def main() -> None:
    """Ejecuta el experimento y genera la gráfica de tiempos."""
    resultados = []

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion, comparaciones_insertion = medir_algoritmo(
            insertion_sort, datos
        )

        tiempo_merge, comparaciones_merge = medir_algoritmo(
            merge_sort, datos
        )

        resultados.append(
            (
                n,
                tiempo_insertion,
                comparaciones_insertion,
                tiempo_merge,
                comparaciones_merge,
            )
        )

    print("Resultados del experimento:")
    print()

    for (
        n,
        tiempo_insertion,
        comparaciones_insertion,
        tiempo_merge,
        comparaciones_merge,
    ) in resultados:
        print(
            f"n={n:4d} | "
            f"Insertion Sort: "
            f"tiempo={tiempo_insertion:.6f} s | "
            f"comparaciones={comparaciones_insertion} | "
            f"Merge Sort: "
            f"tiempo={tiempo_merge:.6f} s | "
            f"comparaciones={comparaciones_merge}"
        )

    graficar_tiempos(resultados)


if __name__ == "__main__":
    main()
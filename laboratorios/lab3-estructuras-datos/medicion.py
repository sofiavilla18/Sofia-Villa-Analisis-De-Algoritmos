"""Experimentos de tiempo de busqueda para lista enlazada y tabla hash."""

import random
import time
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


CANTIDAD_BUSQUEDAS = 200
REPETICIONES = 5
TAMANO_FIJO = 20_000
TAMANOS = [100, 500, 1_000, 5_000, 20_000, 50_000]
FACTORES_CARGA = [0.5, 1, 4, 10]

CARPETA_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int],
    cantidad: int,
    semilla: int = 7,
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cantidad de guias inexistentes que se generaran.
        semilla: Semilla para reproducir la medicion.

    Returns:
        Lista de guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un numero entero es primo.

    Args:
        numero: Entero que se desea comprobar.

    Returns:
        True si el numero es primo; False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 1

    return True


def siguiente_primo(numero: int) -> int:
    """Encuentra el primer numero primo mayor o igual al recibido.

    Args:
        numero: Limite inferior de busqueda.

    Returns:
        El primer numero primo mayor o igual a numero.
    """
    candidato = max(2, numero)

    while not es_primo(candidato):
        candidato += 1

    return candidato


def generar_datos(
    cantidad: int,
    semilla: int = 2026,
) -> list[tuple[int, str]]:
    """Genera guias unicas y sus estados de envio.

    Args:
        cantidad: Numero de guias que se generaran.
        semilla: Semilla para reproducir los datos.

    Returns:
        Lista de pares formados por guia y estado.
    """
    azar = random.Random(semilla)

    guias = azar.sample(
        range(10**9, 10**10),
        cantidad,
    )

    estados = ["En bodega", "En reparto", "Entregado"]

    return [
        (guia, azar.choice(estados))
        for guia in guias
    ]


def construir_estructuras(
    datos: list[tuple[int, str]],
    m: int,
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye la lista y la tabla hash con los mismos datos.

    Args:
        datos: Pares de guia y estado que se almacenaran.
        m: Numero de casillas de la tabla hash.

    Returns:
        Una tupla con la lista enlazada y la tabla hash.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia, estado in datos:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def verificar_busquedas(
    lista: ListaEnlazada,
    tabla: TablaHash,
    datos: list[tuple[int, str]],
) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados.

    Args:
        lista: Lista enlazada construida.
        tabla: Tabla hash construida.
        datos: Pares de guia y estado almacenados.
    """
    muestra = datos[:min(100, len(datos))]

    for guia, estado in muestra:
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado
        assert lista.buscar(guia) == tabla.buscar(guia)


def medir_busquedas(
    buscar: Callable[[int], str | None],
    guias: list[int],
) -> float:
    """Calcula el tiempo medio por busqueda en segundos.

    Args:
        buscar: Metodo de busqueda de una estructura.
        guias: Guias que se consultaran en cada repeticion.

    Returns:
        Tiempo medio por busqueda, expresado en segundos.
    """
    tiempos: list[float] = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        for guia in guias:
            buscar(guia)

        fin = time.perf_counter()
        tiempos.append((fin - inicio) / len(guias))

    return sum(tiempos) / len(tiempos)


def experimento_a() -> None:
    """Compara los tiempos de busqueda de ambas estructuras."""
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    for n in TAMANOS:
        print(f"Experimento A: n = {n:,}")

        datos = generar_datos(n)
        guias_existentes = {guia for guia, _ in datos}

        # La tabla usa un primo cercano a n / 2.
        m = siguiente_primo(n // 2)

        lista, tabla = construir_estructuras(datos, m)
        verificar_busquedas(lista, tabla, datos)

        # Ambas estructuras reciben exactamente las mismas consultas.
        guias_inexistentes = generar_guias_inexistentes(
            guias_existentes,
            CANTIDAD_BUSQUEDAS,
            semilla=7,
        )

        tiempo_lista = medir_busquedas(
            lista.buscar,
            guias_inexistentes,
        )
        tiempo_tabla = medir_busquedas(
            tabla.buscar,
            guias_inexistentes,
        )

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"  m = {m}, alfa = {tabla.factor_carga():.3f}, "
            f"lista = {tiempo_lista:.8f} s/busqueda, "
            f"tabla = {tiempo_tabla:.8f} s/busqueda"
        )

    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    plt.plot(
        TAMANOS,
        tiempos_lista,
        marker="o",
        label="Lista enlazada",
    )
    plt.plot(
        TAMANOS,
        tiempos_tabla,
        marker="s",
        label="Tabla hash",
    )
    plt.title("Experimento A: lista enlazada frente a tabla hash")
    plt.xlabel("Numero de guias almacenadas (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga en la tabla hash."""
    print(f"\nExperimento B: n = {TAMANO_FIJO:,}")

    datos = generar_datos(TAMANO_FIJO)
    guias_existentes = {guia for guia, _ in datos}

    guias_inexistentes = generar_guias_inexistentes(
        guias_existentes,
        CANTIDAD_BUSQUEDAS,
        semilla=7,
    )

    alfas_medidos: list[float] = []
    tiempos: list[float] = []

    for alfa_objetivo in FACTORES_CARGA:
        m = siguiente_primo(
            int(TAMANO_FIJO / alfa_objetivo)
        )

        lista, tabla = construir_estructuras(datos, m)
        verificar_busquedas(lista, tabla, datos)

        tiempo = medir_busquedas(
            tabla.buscar,
            guias_inexistentes,
        )

        alfa_real = tabla.factor_carga()
        alfas_medidos.append(alfa_real)
        tiempos.append(tiempo)

        print(
            f"  alfa objetivo = {alfa_objetivo:g}, "
            f"m = {m}, alfa real = {alfa_real:.4f}, "
            f"tiempo = {tiempo:.8f} s/busqueda"
        )

    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    plt.plot(
        alfas_medidos,
        tiempos,
        marker="o",
        label="Tabla hash",
    )
    plt.title("Experimento B: efecto del factor de carga")
    plt.xlabel("Factor de carga (α = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta los dos experimentos y genera sus graficas."""
    experimento_a()
    experimento_b()


if __name__ == "__main__":
    main()

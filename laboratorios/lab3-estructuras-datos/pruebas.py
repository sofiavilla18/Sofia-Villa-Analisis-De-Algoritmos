"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_busquedas_basicas() -> None:
    """Verifica busquedas exitosas e infructuosas en ambas estructuras."""
    lista = ListaEnlazada()
    tabla = TablaHash(7)

    datos = [
        (1234567890, "En bodega"),
        (2345678901, "En reparto"),
        (3456789012, "Entregado"),
    ]

    for guia, estado in datos:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia, estado in datos:
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado

    guia_inexistente = 9999999999
    assert lista.buscar(guia_inexistente) is None
    assert tabla.buscar(guia_inexistente) is None


def probar_colisiones() -> None:
    """Verifica la insercion y busqueda de guias que colisionan."""
    tabla = TablaHash(7)
    guias = (10, 24, 17)

    for guia in guias:
        tabla.insertar(guia, "En bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    for guia in guias:
        assert tabla.buscar(guia) == "En bodega"

    assert tabla.casillas[3].tamano == 3

    # El factor de carga debe ser n / m = 3 / 7.
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara las busquedas de ambas estructuras en 20 colecciones aleatorias."""
    generador = random.Random(42)

    for _ in range(20):
        lista = ListaEnlazada()
        tabla = TablaHash(101)

        cantidad_guias = generador.randint(1, 50)
        guias = generador.sample(
            range(1_000_000_000, 10_000_000_000),
            cantidad_guias,
        )

        datos = [
            (guia, generador.choice(
                ["En bodega", "En reparto", "Entregado"]
            ))
            for guia in guias
        ]

        for guia, estado in datos:
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia, _ in datos:
            assert lista.buscar(guia) == tabla.buscar(guia)

        guias_inexistentes = generador.sample(
            range(10_000_000_000, 20_000_000_000),
            10,
        )

        for guia in guias_inexistentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None


def ejecutar_pruebas() -> None:
    """Ejecuta todas las pruebas definidas para las estructuras."""
    probar_busquedas_basicas()
    probar_colisiones()
    probar_colecciones_aleatorias()

    print("Todas las pruebas se ejecutaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
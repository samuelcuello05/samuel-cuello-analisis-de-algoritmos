"""Experimento de peor, mejor y caso promedio para insertion sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

CARPETA_GRAFICAS = Path("graficas")


def medir_escenario(generador, n: int):
    """Genera datos y mide únicamente la ejecución del algoritmo."""
    datos = generador(n)

    inicio = time.perf_counter()
    _, comparaciones = insertion_sort(datos)
    fin = time.perf_counter()

    tiempo = fin - inicio

    return tiempo, comparaciones


def ejecutar_experimento():
    """Ejecuta las mediciones de los tres escenarios."""
    resultados = {
        "Aleatorio": {"tiempo": [], "comparaciones": []},
        "Casi ordenado": {"tiempo": [], "comparaciones": []},
        "Inverso": {"tiempo": [], "comparaciones": []},
    }

    generadores = {
        "Aleatorio": generar_aleatorio,
        "Casi ordenado": generar_casi_ordenado,
        "Inverso": generar_inverso,
    }

    for nombre, generador in generadores.items():
        for n in TAMANOS:
            tiempo, comparaciones = medir_escenario(generador, n)

            resultados[nombre]["tiempo"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)

            print(
                f"{nombre:16} n={n:5} "
                f"tiempo={tiempo:.6f}s "
                f"comparaciones={comparaciones}"
            )

    return resultados


def graficar_comparaciones(resultados):
    """Genera la gráfica de comparaciones."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion Sort: comparaciones vs. tamaño")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        CARPETA_GRAFICAS / "parte3_comparaciones.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


def graficar_tiempo(resultados):
    """Genera la gráfica de tiempo."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempo"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion Sort: tiempo vs. tamaño")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        CARPETA_GRAFICAS / "parte3_tiempo.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    resultados = ejecutar_experimento()

    graficar_comparaciones(resultados)
    graficar_tiempo(resultados)

    print("\nGráficas generadas correctamente.")
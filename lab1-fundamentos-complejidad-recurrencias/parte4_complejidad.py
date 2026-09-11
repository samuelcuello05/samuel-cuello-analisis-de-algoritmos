"""Medición comparativa de insertion sort y merge sort."""

import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

CARPETA_GRAFICAS = Path("graficas")


def medir_algoritmo(algoritmo, datos):
    """Mide únicamente el tiempo de ejecución del algoritmo."""
    inicio = time.perf_counter()
    algoritmo(datos)
    fin = time.perf_counter()

    return fin - inicio


def ejecutar_experimento():
    """Mide ambos algoritmos sobre el escenario A."""
    tiempos_insertion = []
    tiempos_merge = []

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        tiempo_insertion = medir_algoritmo(
            insertion_sort,
            datos,
        )

        tiempo_merge = medir_algoritmo(
            merge_sort,
            datos,
        )

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        print(
            f"n={n:5} | "
            f"insertion={tiempo_insertion:.6f}s | "
            f"merge={tiempo_merge:.6f}s"
        )

    return tiempos_insertion, tiempos_merge


def generar_grafica(tiempos_insertion, tiempos_merge):
    """Genera la gráfica comparativa."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    plt.figure()

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title("Insertion Sort vs. Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        CARPETA_GRAFICAS / "parte4_tiempo.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    tiempos_insertion, tiempos_merge = ejecutar_experimento()

    generar_grafica(
        tiempos_insertion,
        tiempos_merge,
    )

    print("\nGráfica de Parte 4 generada correctamente.")
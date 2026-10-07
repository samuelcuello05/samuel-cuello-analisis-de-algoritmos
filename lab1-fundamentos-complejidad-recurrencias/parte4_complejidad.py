"""Medición comparativa de insertion sort y merge sort."""

import statistics
import time
from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

REPETICIONES = 3

CARPETA_GRAFICAS = Path("graficas")

Algoritmo = Callable[[list[int]], tuple[list[int], int]]

ALGORITMOS: dict[str, Algoritmo] = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}


def medir_algoritmo(
    algoritmo: Algoritmo,
    datos: list[int],
) -> tuple[float, int]:
    """Mide unicamente la ejecucion del algoritmo sobre un lote.

    El algoritmo se ejecuta REPETICIONES veces sobre el mismo lote y se
    toma la mediana del tiempo para reducir el ruido del sistema
    operativo. Como el algoritmo no modifica la lista recibida, todas las
    repeticiones ordenan exactamente la misma entrada.

    Args:
        algoritmo: funcion de ordenamiento de algoritmos.py.
        datos: lote de indices de riesgo a ordenar.

    Returns:
        Una tupla con la mediana del tiempo de ejecucion en segundos y
        el numero de comparaciones entre elementos.
    """
    tiempos = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = algoritmo(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return statistics.median(tiempos), comparaciones


def ejecutar_experimento() -> dict[str, dict[str, list[float]]]:
    """Mide ambos algoritmos sobre el escenario A para cada tamano.

    Returns:
        Diccionario indexado por nombre de algoritmo. Cada valor tiene
        las listas "tiempo" (segundos) y "comparaciones", en el mismo
        orden de TAMANOS.
    """
    resultados = {
        nombre: {"tiempo": [], "comparaciones": []}
        for nombre in ALGORITMOS
    }

    for n in TAMANOS:
        datos = generar_aleatorio(n)
        linea = f"n={n:5}"

        for nombre, algoritmo in ALGORITMOS.items():
            tiempo, comparaciones = medir_algoritmo(algoritmo, datos)

            resultados[nombre]["tiempo"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)

            linea += (
                f" | {nombre}: {tiempo:.6f}s, "
                f"{comparaciones} comparaciones"
            )

        print(linea)

    return resultados


def comparar_por_escenario(
    n: int = 6400,
) -> dict[str, dict[str, tuple[float, int]]]:
    """Mide ambos algoritmos sobre los tres escenarios de Tamiza.

    Sirve para comprobar con datos si el tiempo de cada algoritmo
    depende del canal por el que llega el lote.

    Args:
        n: cantidad de registros de cada lote.

    Returns:
        Diccionario indexado por nombre de algoritmo y luego por
        escenario, con la tupla (tiempo en segundos, comparaciones).
    """
    escenarios = {
        "A - Aleatorio": generar_aleatorio(n),
        "B - Casi ordenado": generar_casi_ordenado(n),
        "C - Inverso": generar_inverso(n),
    }

    resultados = {nombre: {} for nombre in ALGORITMOS}

    print(f"\nComparacion por escenario (n={n}):")

    for escenario, datos in escenarios.items():
        for nombre, algoritmo in ALGORITMOS.items():
            tiempo, comparaciones = medir_algoritmo(algoritmo, datos)
            resultados[nombre][escenario] = (tiempo, comparaciones)

            print(
                f"{escenario:18} | {nombre:14} | "
                f"tiempo={tiempo:.6f}s | "
                f"comparaciones={comparaciones}"
            )

    return resultados


def generar_grafica(resultados: dict[str, dict[str, list[float]]]) -> None:
    """Genera la grafica comparativa de tiempo vs. tamano de entrada.

    Args:
        resultados: diccionario devuelto por ejecutar_experimento.
    """
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempo"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion Sort vs. Merge Sort (escenario A)")
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
    resultados = ejecutar_experimento()

    generar_grafica(resultados)

    comparar_por_escenario()

    print("\nGráfica de Parte 4 generada correctamente.")

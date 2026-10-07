"""Medicion del subarreglo maximo: fuerza bruta vs. divide y venceras."""

import random
import statistics
import time
from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


SEMILLA = 2026

TAMANOS = [10, 25, 50, 100, 250, 500, 1000, 2000, 4000, 8000]

REPETICIONES = 3

CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

Algoritmo = Callable[[list[float]], tuple[int, int, float]]


def divide_y_venceras(valores: list[float]) -> tuple[int, int, float]:
    """Llama a subarreglo_maximo sobre la serie completa.

    Permite medir ambos algoritmos con la misma firma de un argumento.

    Args:
        valores: variacion diaria de caja, con al menos un elemento.

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo de toda la serie.
    """
    return subarreglo_maximo(valores, 0, len(valores) - 1)


ALGORITMOS: dict[str, Algoritmo] = {
    "Fuerza bruta": subarreglo_fuerza_bruta,
    "Divide y vencerás": divide_y_venceras,
}


def generar_datos(n: int, generador: random.Random) -> list[int]:
    """Genera una serie de variaciones diarias de caja.

    Args:
        n: cantidad de dias de la serie.
        generador: generador pseudoaleatorio inicializado con SEMILLA,
            para que las mediciones sean reproducibles.

    Returns:
        Una lista de n enteros entre -100 y 100 (miles de pesos).
    """
    return [generador.randint(-100, 100) for _ in range(n)]


def medir(algoritmo: Algoritmo, datos: list[int]) -> tuple[float, float]:
    """Mide unicamente la ejecucion del algoritmo sobre una serie.

    El algoritmo se ejecuta REPETICIONES veces sobre la misma serie y se
    toma la mediana del tiempo para reducir el ruido del sistema
    operativo. Ningun algoritmo modifica la lista, asi que todas las
    repeticiones resuelven exactamente la misma entrada.

    Args:
        algoritmo: funcion que recibe la serie y devuelve
            (inicio, fin, suma).
        datos: serie de variaciones diarias de caja.

    Returns:
        Una tupla con la mediana del tiempo de ejecucion en segundos y la
        suma maxima encontrada.
    """
    tiempos = []
    suma = 0.0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, _, suma = algoritmo(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return statistics.median(tiempos), suma


def ejecutar_experimento() -> dict[str, list[float]]:
    """Mide ambos algoritmos para cada tamano de TAMANOS.

    En cada tamano ambos algoritmos reciben la misma serie y se verifica
    que encuentren la misma suma maxima.

    Returns:
        Diccionario indexado por nombre de algoritmo con la lista de
        tiempos en segundos, en el mismo orden de TAMANOS.

    Raises:
        ValueError: si en algun tamano los algoritmos no coinciden en la
            suma maxima.
    """
    generador = random.Random(SEMILLA)
    resultados: dict[str, list[float]] = {nombre: [] for nombre in ALGORITMOS}

    print(
        f"{'n':>6} | {'Fuerza bruta (s)':>16} | "
        f"{'Divide y venceras (s)':>21} | {'Suma maxima':>11}"
    )

    for n in TAMANOS:
        datos = generar_datos(n, generador)
        sumas = []

        for nombre, algoritmo in ALGORITMOS.items():
            tiempo, suma = medir(algoritmo, datos)
            resultados[nombre].append(tiempo)
            sumas.append(suma)

        if sumas[0] != sumas[1]:
            raise ValueError(
                f"Las sumas no coinciden para n={n}: {sumas[0]} != {sumas[1]}"
            )

        print(
            f"{n:>6} | {resultados['Fuerza bruta'][-1]:>16.6f} | "
            f"{resultados['Divide y vencerás'][-1]:>21.6f} | "
            f"{sumas[0]:>11}"
        )

    return resultados


def graficar(
    resultados: dict[str, list[float]],
    archivo: str,
    titulo: str,
    escala_log: bool,
) -> None:
    """Grafica el tiempo de ambos algoritmos contra el tamano de entrada.

    Args:
        resultados: diccionario devuelto por ejecutar_experimento.
        archivo: nombre del archivo PNG dentro de CARPETA_GRAFICAS.
        titulo: titulo de la grafica.
        escala_log: si es True, usa escala logaritmica en ambos ejes.
    """
    plt.figure()

    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)

    if escala_log:
        plt.xscale("log")
        plt.yscale("log")

    plt.title(titulo)
    plt.xlabel("Tamaño de entrada n (días)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True, which="both" if escala_log else "major", alpha=0.4)

    plt.savefig(CARPETA_GRAFICAS / archivo, dpi=150, bbox_inches="tight")
    plt.close()


def generar_graficas(resultados: dict[str, list[float]]) -> None:
    """Genera la grafica en escala lineal y la grafica log-log.

    Args:
        resultados: diccionario devuelto por ejecutar_experimento.
    """
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    graficar(
        resultados,
        "tiempo_vs_n.png",
        "Subarreglo máximo: fuerza bruta vs. divide y vencerás",
        escala_log=False,
    )
    graficar(
        resultados,
        "tiempo_vs_n_log.png",
        "Subarreglo máximo (escala log-log)",
        escala_log=True,
    )


if __name__ == "__main__":
    resultados = ejecutar_experimento()

    generar_graficas(resultados)

    print(f"\nGráficas guardadas en {CARPETA_GRAFICAS}")

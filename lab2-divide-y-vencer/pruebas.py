"""Pruebas con assert para las soluciones del subarreglo maximo."""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


SEMILLA = 2026

CANTIDAD_ALEATORIAS = 30

Resultado = tuple[int, int, float]


def resolver_ambas(valores: list[float]) -> tuple[Resultado, Resultado]:
    """Resuelve la misma serie con fuerza bruta y con divide y venceras.

    Args:
        valores: variacion diaria de caja, con al menos un elemento.

    Returns:
        Una tupla con el resultado (inicio, fin, suma) de la fuerza
        bruta y el de divide y venceras, en ese orden.
    """
    fuerza_bruta = subarreglo_fuerza_bruta(valores)
    divide_y_venceras = subarreglo_maximo(valores, 0, len(valores) - 1)
    return fuerza_bruta, divide_y_venceras


serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert sum(serie) == 10
assert subarreglo_fuerza_bruta(serie) == (1, 6, 17)
assert subarreglo_maximo(serie, 0, len(serie) - 1) == (1, 6, 17)

for valores in ([7], [-7], [0]):
    fuerza_bruta, divide_y_venceras = resolver_ambas(valores)
    assert fuerza_bruta[2] == valores[0]
    assert divide_y_venceras[2] == valores[0]

negativos = [-8, -3, -6, -2, -5, -9]
fuerza_bruta, divide_y_venceras = resolver_ambas(negativos)
assert fuerza_bruta[2] == -2
assert divide_y_venceras[2] == -2

positivos = [4, 1, 7, 3, 2, 6]
fuerza_bruta, divide_y_venceras = resolver_ambas(positivos)
assert fuerza_bruta[2] == 23
assert divide_y_venceras[2] == 23

cruzado = [-10, -10, 5, 6, 7, 8, -10, -10]
medio = (len(cruzado) - 1) // 2
assert suma_cruzada(cruzado, 0, medio, len(cruzado) - 1) == (2, 5, 26)
assert subarreglo_maximo(cruzado, 0, medio)[2] == 11
assert subarreglo_maximo(cruzado, medio + 1, len(cruzado) - 1)[2] == 15
fuerza_bruta, divide_y_venceras = resolver_ambas(cruzado)
assert fuerza_bruta[2] == 26
assert divide_y_venceras[2] == 26

assert suma_cruzada([-1, -4, -3, -2], 0, 1, 3) == (1, 2, -7)

generador = random.Random(SEMILLA)

for _ in range(CANTIDAD_ALEATORIAS):
    n = generador.randint(1, 60)
    valores = [generador.randint(-100, 100) for _ in range(n)]
    original = valores.copy()

    fuerza_bruta, divide_y_venceras = resolver_ambas(valores)

    assert fuerza_bruta[2] == divide_y_venceras[2], valores
    assert valores == original

    inicio, fin, suma = divide_y_venceras
    assert sum(valores[inicio:fin + 1]) == suma

print(
    "Todas las pruebas pasaron "
    f"({CANTIDAD_ALEATORIAS} listas aleatorias con semilla {SEMILLA})."
)

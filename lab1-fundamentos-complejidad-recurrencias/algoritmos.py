"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = datos.copy()
    comparaciones = 0

    for i in range(1, len(copia)):
        clave = copia[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if copia[j] < clave:
                copia[j + 1] = copia[j]
                j -= 1
            else:
                break

        copia[j + 1] = clave

    return copia, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    copia = datos.copy()

    def merge_sort_recursivo(lista):
        if len(lista) <= 1:
            return lista, 0

        mitad = len(lista) // 2

        izquierda, comparaciones_izq = merge_sort_recursivo(
            lista[:mitad]
        )
        derecha, comparaciones_der = merge_sort_recursivo(
            lista[mitad:]
        )

        combinada = []
        i = 0
        j = 0
        comparaciones_merge = 0

        while i < len(izquierda) and j < len(derecha):
            comparaciones_merge += 1

            if izquierda[i] >= derecha[j]:
                combinada.append(izquierda[i])
                i += 1
            else:
                combinada.append(derecha[j])
                j += 1

        combinada.extend(izquierda[i:])
        combinada.extend(derecha[j:])

        total = (
            comparaciones_izq
            + comparaciones_der
            + comparaciones_merge
        )

        return combinada, total

    return merge_sort_recursivo(copia)
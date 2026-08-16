def calcular_promedio(numeros: list[int]) -> float:
    """
    Calcula el promedio matemático de los elementos en una lista.

    Args:
        numeros (list[int]): Una lista que contiene números enteros.

    Returns:
        float: El valor promedio de los números ingresados.
    """
    suma = 0
    for numero in numeros:
        suma += numero
        
    return suma / len(numeros)

def main() -> None:
    lista_numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista_numeros))

if __name__ == "__main__":
    main()
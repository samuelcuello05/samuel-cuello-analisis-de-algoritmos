"""Clasificador de años bisiestos.

Complete las funciones siguiendo la especificación de cada docstring.
"""


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.

    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.

    Args:
        anio: año a evaluar (número entero).

    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.

    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).

    Returns:
        Lista de años como enteros.
    """
    while True:
        entrada = input("Ingrese una lista de años separados por comas (ej. 2024, 1900, 2000): ")
        try:
            # Separamos el texto por comas, quitamos espacios y convertimos a entero
            lista_anios = [int(x.strip()) for x in entrada.split(",")]
            return lista_anios
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar solo números enteros separados por comas. Intente de nuevo.\n")


def main() -> None:
    """Punto de entrada del script."""
    anios_ingresados = leer_anios()
    
    # Filtramos usando comprensión de listas
    bisiestos = [anio for anio in anios_ingresados if es_bisiesto(anio)]
    
    # Imprimimos el resumen
    print("\n--- Resumen ---")
    print(f"Total de años evaluados: {len(anios_ingresados)}")
    print(f"Cantidad de años bisiestos encontrados: {len(bisiestos)}")
    print(f"Lista de años bisiestos: {bisiestos}")


if __name__ == "__main__":
    main()
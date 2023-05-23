from re import sub


REGEX_DE_NUMERO_FLOTANTE: str = '[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)'


def es_numero_flotante_valido(entrada: str) -> bool:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Evalua si la 'entrada' dada, tiene el formato de un número flotante
          y si el mismo, es mayor a 0
    """

    numero: int = int()
    numero_formateado: str = sub(REGEX_DE_NUMERO_FLOTANTE, '', entrada)
    flag_numero_flotante_valido: False

    if numero_formateado:
        numero = int(numero_formateado)

        if numero > 0:
            flag_numero_flotante_valido = True

        else:
            print('\n¡Sólo se pueden ingresar numeros positivos!')
    else:
        print('\n¡Sólo se pueden ingresar numeros enteros o flotantes!')
    
    return flag_numero_flotante_valido


def main() -> None:
    pass


main()
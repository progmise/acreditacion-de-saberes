from re import findall


REGEX_DE_NUMERO_FLOTANTE: str = r'[-+]?(?:\d+\.?\d*|\.\d+)'
SUELDO_BASE: float = 100000.00


def es_numero_flotante_valido(entrada: str) -> bool:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un boolean, que es resultado de evaluar si la 
          'entrada' dada, tiene el formato de un número flotante
    """

    numeros_encontrados: list = findall(REGEX_DE_NUMERO_FLOTANTE, entrada)
    es_numero_valido: bool = False

    if numeros_encontrados:
        es_numero_valido = True
    else:
        print('\n¡Sólo se pueden ingresar numeros enteros o con decimales!')
    
    return es_numero_valido


def validar_numero_flotante(entrada: str) -> float:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un float a partir de 'entrada', el cual ha sido
          validado
    """

    numero: float = float()
    numberos_encontrados: list = list()
    es_numero_valido: bool = False

    while not es_numero_valido:

        if es_numero_flotante_valido(entrada):
            numberos_encontrados = findall(REGEX_DE_NUMERO_FLOTANTE, entrada)
            numero = float(numberos_encontrados[0])
            es_numero_valido = True

        else:
            entrada = solicitar_sueldo()

    return numero


def solicitar_sueldo() -> str:
    """
    PRE:  No tiene
    POST: Solicita y devuelve un string que representa el 
          sueldo de un trabajador
    """

    entrada: str = input('\nIngrese el sueldo del trabajador: ')

    return entrada


def ingresar_sueldo() -> float:
    """
    PRE:  No tiene
    POST: Devuelve un float que representa el sueldo de un trabajador,
          el cual se solicita por consola y se valida
    """

    entrada: str = solicitar_sueldo()
    sueldo: float = validar_numero_flotante(entrada)

    return sueldo


def dar_de_alta_sueldo_de_trabajador(id_trabajador: int, sueldos_de_trabajadores: dict) -> float:
    """
    PRE:  'id_trabajador' debe ser una variable de tipo int
          'sueldos_de_trabajadores' debe ser una variable de tipo dict
    POST: Da de alta un sueldo, si cumple las condiciones, y devuelve el mismo
          como un float
    """

    print(f'\n######## {id_trabajador}° TRABAJADOR ########')

    sueldo: float = ingresar_sueldo()  

    if sueldo > 0:
        sueldos_de_trabajadores[id_trabajador] = {
            'sueldo_anterior': sueldo,
            'sueldo_actualizado': round(sueldo * 1.15, 2) if sueldo < SUELDO_BASE else sueldo
        }

    return sueldo


def mostrar_comparativa_de_sueldos(sueldos_de_trabajadores: dict) -> None:
    """
    PRE:  'sueldos_de_trabajadores' debe ser una variable de tipo dict
    POST: Muestra por pantalla, una comparativa del sueldo de cada
          trabajador, es decir, su sueldo anterior y actualizado
    """

    print('\n######## SUELDOS DE TRABAJADORES ########')

    for id_trabajador, sueldo in sueldos_de_trabajadores.items():
        print(f'\n|| {id_trabajador}° trabajador ||')

        for llave, valor in sueldo.items():
            print(
                '    {0}: {1}'.format(
                    llave.capitalize().replace('_', ' '),
                    valor
                )
            )


def main() -> None:
    """
    PRE:  No tiene
    POST: Inicializa el programa de la empresa
    """

    contador: int = 1
    sueldos_de_trabajadores: dict = dict()

    sueldo: float = dar_de_alta_sueldo_de_trabajador(contador, sueldos_de_trabajadores)

    while sueldo > 0:

        contador += 1

        sueldo = dar_de_alta_sueldo_de_trabajador(contador, sueldos_de_trabajadores)

    if not sueldos_de_trabajadores:
        print('¡No se ingresó ningún sueldo válido de algún trabajador!')

    else:
        mostrar_comparativa_de_sueldos(sueldos_de_trabajadores)

    print('\n¡Hasta luego!')


main()
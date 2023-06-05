from random import randint

VALOR_MINIMO: int = 0
VALOR_MAXIMO: int = 999
CANTIDAD_MAXIMA_DE_INTENTOS: int = 10


def se_encuentra_entre_valores(numero: int, numero_minimo: int, numero_maximo: str) -> bool:
    """
    PRE: 'numero', debe ser una variable de tipo int
         'numero_minimo', debe ser una variable de tipo int
         'numero_maximo', debe ser una variable de tipo int
    POST: Devuelve un boolean, que es resultado de evaluar si el 
          'numero' dado, se encuentra entre los valores de 'numero_minimo'
          y 'numero_maximo'
    """

    esta_dentro_del_rango: bool = False

    if numero >= numero_minimo and numero <= numero_maximo:
        esta_dentro_del_rango = True

    else:
        print(f'\n¡El número entero ingresado debe estar entre {numero_minimo} y {numero_maximo}!')

    return esta_dentro_del_rango


def es_numero_entero(entrada: str) -> bool:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un boolean, que es resultado de evaluar si la 
          'entrada' dada, tiene el formato de un número entero
          mayor a 0
    """

    es_numero_valido: bool = False

    if entrada.isnumeric():
        es_numero_valido: bool = True
    else:
        print('\n¡Sólo se pueden ingresar numeros enteros!')

    return es_numero_valido


def es_numero_entero_valido(entrada: str) -> bool:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un boolean, que es resultado de evaluar si la 
          'entrada' dada, tiene el formato de un número entero, ya 
          sea positivo o negativo
    """

    es_numero_valido: bool = False

    if entrada[0] == '-':
        es_numero_valido = es_numero_entero(entrada[1::])

    else:
        es_numero_valido = es_numero_entero(entrada)      

    return es_numero_valido


def son_solo_espacios(entrada: str) -> bool:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un boolean, que es resultado de evaluar si la 
          'entrada' dada, sólo representa a espacios
    """

    son_espacios: bool = True

    if entrada.isspace():
        print('\n¡No se pueden ingresar solamente espacios!')
    else:
        son_espacios = False

    return son_espacios


def validar_numero_entero(entrada: str, numero_minimo: int, numero_maximo: int) -> int:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un entero a partir de 'entrada', el cual ha sido
          validado
    """

    numero: int = int()
    es_numero_valido: bool = False

    while not es_numero_valido:

        if (not son_solo_espacios(entrada) and es_numero_entero_valido(entrada) and 
                se_encuentra_entre_valores(int(entrada), numero_minimo, numero_maximo)):
            numero = int(entrada)
            es_numero_valido: bool = True

        else:
            entrada = solicitar_numero()

    return numero


def solicitar_numero() -> str:
    """
    PRE:  No tiene
    POST: Solicita y devuelve un string que representa el 
          número que está oculto
    """

    entrada: str = input('\nIngrese el número que cree que está oculto: ')

    return entrada


def mostrar_digitos_correctos(numero_ingresado: str, numero_a_adivinar: str) -> None:
    """
    PRE: 'numero_ingresado', debe ser una variable de tipo string
         'numero_a_adivinar', debe ser una variable de tipo string
    POST: Muestra por pantalla, los dígitos que coinciden entre 'numero_ingresado'
          y 'numero_a_adivinar' y su posición
    """

    cantidad_de_digitos_correctos: int = 0

    for i in range(len(numero_ingresado)):
        for j in range(len(numero_a_adivinar)):
            if i == j:
                if numero_ingresado[i] == numero_a_adivinar[j]:
                    cantidad_de_digitos_correctos += 1

                    print(f'\nEl dígito {numero_ingresado[i]}, en la posición {i + 1}, es correcto')

    print(f'\nLa cantidad de dígitos correctos es: {cantidad_de_digitos_correctos}')
    

def se_adivino_numero(numero_ingresado: str, numero_a_adivinar: str) -> bool:
    """
    PRE: 'numero_ingresado', debe ser una variable de tipo string
         'numero_a_adivinar', debe ser una variable de tipo string
    POST: Devuelve un boolean, resultado de evaluar si el 'numero_ingresado'
          es el mismo que 'numero_a_adivinar'
    """

    son_numeros_coincidentes: bool = True

    if len(numero_ingresado) == len(numero_a_adivinar):

        if numero_ingresado != numero_a_adivinar:
            son_numeros_coincidentes = False

    else:
        son_numeros_coincidentes = False

    return son_numeros_coincidentes


def ingresar_numero() -> int:
    """
    PRE:  No tiene
    POST: Devuelve un int que representa el número que está oculto,
          el cual se solicita por consola y se valida
    """

    entrada: str = solicitar_numero()
    numero: int = validar_numero_entero(entrada, VALOR_MINIMO, VALOR_MAXIMO)

    return numero


def adivinar_numero(numero_a_adivinar: int) -> bool:
    """
    PRE: 'numero_a_adivinar', debe ser una variable de tipo int
    POST: Devuelve un boolean, resultado de evaluar si el usuario
          descubrió el 'numero_a_adivinar'. También se le muestra al
          usuario las cifras que acertó
    """

    numero_ingresado: int = ingresar_numero()
    son_numeros_coincidentes: bool = se_adivino_numero(str(numero_ingresado), str(numero_a_adivinar)) 

    mostrar_digitos_correctos(str(numero_ingresado), str(numero_a_adivinar))

    return son_numeros_coincidentes


def main() -> None:
    """
    PRE:  No tiene
    POST: Inicializa el programa para adivinar el número
    """

    numero_a_adivinar: int = randint(VALOR_MINIMO, VALOR_MAXIMO)
    cantidad_de_intentos: int = 1

    son_numeros_coincidentes: bool = adivinar_numero(numero_a_adivinar)

    while not son_numeros_coincidentes and cantidad_de_intentos < CANTIDAD_MAXIMA_DE_INTENTOS:
        print('\nNo hubo suerte, ¡Vamos de nuevo!')

        son_numeros_coincidentes: bool = adivinar_numero(numero_a_adivinar)

        cantidad_de_intentos += 1

    if son_numeros_coincidentes:
        print(f'\n¡Se adivino el número {numero_a_adivinar}, con una cantidad de intentos de {cantidad_de_intentos}!')
    else:
        print(f'\n¡No se llegó a adivinar el número {numero_a_adivinar}, en los {CANTIDAD_MAXIMA_DE_INTENTOS} intentos que se tenía!')

    print('\n¡Hasta luego!')


main()
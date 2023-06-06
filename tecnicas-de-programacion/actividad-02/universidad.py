EDAD_MINIMA: int = 18
EDAD_MAXIMA: int = 99
NUMERO_DE_MATRICULA_MINIMO: int = 1
NUMERO_DE_MATRICULA_MAXIMO: int = 999999
GENEROS: tuple = (('M', 'Masculino') ,('F', 'Femenino'), ('X', 'No binario'))
VALOR_DE_CUOTA_MENSUAL: float = 32000.00
CANTIDAD_DE_ANIOS_APROBADOS_MINIMO: int = 0
CANTIDAD_DE_ANIOS_APROBADOS_MAXIMO: int = 6
DURACION_DE_CARRERAS_EN_ANIOS: int = 6


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


def es_alfabetico(entrada: str) -> bool:
    """
    PRE: 'entrada', debe ser una variable de tipo string
    POST: Devuelve un boolean, que es resultado de evaluar si la 
          'entrada' dada, sólo contiene caracteres del alfabeto
    """

    son_solo_caracteres_alfabeticos: bool = False

    if entrada.isalpha():
        son_solo_caracteres_alfabeticos = True
    else:
        print('\n¡Sólo se pueden ingresar caracteres del alfabeto!')

    return son_solo_caracteres_alfabeticos


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


def validar_numero_entero(entrada: str, numero_minimo: int, numero_maximo: int, mensaje: str) -> int:
    """
    PRE: 'entrada', debe ser una variable de tipo string
         'numero_minimo', debe ser una variable de tipo int
         'numero_maximo', debe ser una variable de tipo int
         'mensaje', debe ser una variable de tipo string
    POST: Devuelve un entero a partir de 'entrada', el cual ha sido
          validado
    """

    numero: int = int()
    es_numero_valido: bool = False

    while not es_numero_valido:

        if (not son_solo_espacios(entrada) and es_numero_entero_valido(entrada) and 
                se_encuentra_entre_valores(int(entrada), numero_minimo, numero_maximo)):
            numero = int(entrada)
            es_numero_valido = True

        else:
            entrada = solicitar_ingreso(mensaje)

    return numero


def validar_matricula(estudiantes: list, numero_de_matricula: int, mensaje: str, se_debe_validar_duplicado: bool) -> int:
    """
    PRE: 'estudiantes', debe ser una variable de tipo list
         'numero_de_matricula', debe ser una variable de tipo int
         'mensaje', debe ser una variable de tipo string
         'se_debe_validar_duplicado', debe ser una variable de tipo bool
    POST: Devuelve un entero a partir de 'numero_de_matricula', el cual se valida
          de que no exista previamente en 'estudiantes'. Se puede indicar sumar
          una estrategia de validación, a partir de 'se_debe_validar_duplicado'
    """

    entrada: str = str()
    es_matricula_valida: bool = False
    numeros_de_matriculas: list = [estudiante['numero_de_matricula'] for estudiante in estudiantes]

    while not es_matricula_valida:

        if se_debe_validar_duplicado:

            if numero_de_matricula not in numeros_de_matriculas:
                es_matricula_valida = True

            else:
                print(f'\n¡El número de matrícula {numero_de_matricula}, ya fue ingresado anteriormente! Debe ingresar otro')

                entrada = solicitar_ingreso(mensaje)
                numero_de_matricula = validar_numero_entero(entrada, NUMERO_DE_MATRICULA_MINIMO, NUMERO_DE_MATRICULA_MAXIMO, mensaje)

        else:
            if numero_de_matricula in numeros_de_matriculas:
                es_matricula_valida = True

            else:
                print(f'\n¡El número de matrícula {numero_de_matricula}, no existe en la base de estudiante! Debe ingresar otro')

                entrada = solicitar_ingreso(mensaje)
                numero_de_matricula = validar_numero_entero(entrada, NUMERO_DE_MATRICULA_MINIMO, NUMERO_DE_MATRICULA_MAXIMO, mensaje)

    return numero_de_matricula


def validar_entrada(entrada: str, mensaje: str) -> str:
    """
    PRE: 'entrada', debe ser una variable de tipo string
         'mensaje', debe ser una variable de tipo string
    POST: Devuelve un string a partir de 'entrada', el cual ha sido
          validado
    """

    es_entrada_valida: bool = False

    while not es_entrada_valida:

        if not son_solo_espacios(entrada) and es_alfabetico(entrada):
            es_entrada_valida = True

        else:
            entrada = solicitar_ingreso(mensaje)

    return entrada


def solicitar_ingreso(mensaje: str) -> str:
    """
    PRE:  'mensaje' debe ser una variable de tipo string
    POST: Solicita y devuelve un string. Se le muestra un 'mensaje' al usuario
          con el fin de clarificar que es lo que tiene que ingresar
    """

    entrada: str = input(f'\n{mensaje}: ')

    return entrada


def obtener_descripcion_de_genero(genero: str) -> str:
    """
    PRE:  'genero' debe ser una variable de tipo string
    POST: Devuelve un string, que representa la descripción del género,
          a partir del 'genero' dado
    """

    descripcion_de_genero: str = str()

    for tupla_de_genero in GENEROS:
        if genero in tupla_de_genero:
            descripcion_de_genero = tupla_de_genero[1]

    return descripcion_de_genero


def ingresar_opcion_de_usuario(opciones: list) -> int:
    """
    PRE:  'opciones', debe ser una variable de tipo list
    POST: Devuelve un int, que representa a la entrada hecha por el  
          usuario, de una opcion, a la cual se la valida
    """

    print('\nOpciones válidas: \n')

    for x in range(len(opciones)):
        print(x + 1, '-', opciones[x])

    mensaje: str = 'Ingrese una opción'
    entrada: str = solicitar_ingreso(mensaje)
    opcion: int = validar_numero_entero(entrada, 1, len(opciones), mensaje)

    return opcion


def ingresar_anios_aprobados() -> int:
    """
    PRE:  No tiene
    POST: Devuelve un int que representa la cantidad de años aprobados 
          del estudiante, el cual se solicita por consola y se valida
    """

    mensaje: str = 'Ingrese la cantidad de años aprobados, de la carrera, del estudiante'
    entrada: str = solicitar_ingreso(mensaje)
    cantidad_de_anios_aprobados: int = validar_numero_entero(entrada, CANTIDAD_DE_ANIOS_APROBADOS_MINIMO, CANTIDAD_DE_ANIOS_APROBADOS_MAXIMO, mensaje)

    return cantidad_de_anios_aprobados


def ingresar_matricula(estudiantes: list, se_debe_validar_duplicado: bool) -> int:
    """
    PRE:  'estudiantes', debe ser una variable de tipo list
          'se_debe_validar_duplicado', debe ser un boolean
    POST: Devuelve un int que representa el número de matrícula del estudiante,
          el cual se solicita por consola y se valida
    """

    mensaje: str = 'Ingrese el número de matrícula del estudiante'
    entrada: str = solicitar_ingreso(mensaje)
    numero_de_matricula: int = validar_numero_entero(entrada, NUMERO_DE_MATRICULA_MINIMO, NUMERO_DE_MATRICULA_MAXIMO, mensaje)
    numero_de_matricula: int = validar_matricula(estudiantes, numero_de_matricula, mensaje, se_debe_validar_duplicado)

    return numero_de_matricula


def ingresar_edad() -> int:
    """
    PRE:  No tiene
    POST: Devuelve un int que representa la edad del estudiante,
          el cual se solicita por consola y se valida
    """

    mensaje: str = 'Ingrese la edad del estudiante'
    entrada: str = solicitar_ingreso(mensaje)
    edad: int = validar_numero_entero(entrada, EDAD_MINIMA, EDAD_MAXIMA, mensaje)

    return edad


def ingresar_genero() -> str:
    """
    PRE:  No tiene
    POST: Devuelve un string que representa el género del estudiante,
          el cual se solicita por consola y se valida
    """

    print('\nA continuación, se deberá ingresar el género del estudiante')

    generos_formateados: list = [f'{tupla_de_genero[1]} ({tupla_de_genero[0]})' for tupla_de_genero in GENEROS]
    opcion: int = ingresar_opcion_de_usuario(generos_formateados)
    genero: str = GENEROS[opcion - 1][0]

    return genero


def ingresar_apellido() -> str:
    """
    PRE:  No tiene
    POST: Devuelve un string que representa el apellido del estudiante,
          el cual se solicita por consola y se valida
    """

    mensaje: str = 'Ingrese el apellido del estudiante'
    entrada: str = solicitar_ingreso(mensaje)
    apellido: str = validar_entrada(entrada, mensaje)

    return apellido


def ingresar_nombre() -> str:
    """
    PRE:  No tiene
    POST: Devuelve un string que representa el nombre del estudiante,
          el cual se solicita por consola y se valida
    """

    mensaje: str = 'Ingrese el nombre del estudiante'
    entrada: str = solicitar_ingreso(mensaje)
    nombre: str = validar_entrada(entrada, mensaje)

    return nombre


def mostrar_datos_de_estudiante_por_matricula(estudiantes: list):
    """
    PRE:  'estudiantes', debe ser una variable de tipo list
    POST: Muestra por consola, los datos de un estudiante, a partir
          de un número de matrícula solicitado al usuario. También
          se informa costo de la carrera y años restantes para finalizar
          la misma
    """

    numero_de_matricula: int = ingresar_matricula(estudiantes, False)
    estudiante: dict = dict()

    for datos_de_estudiante in estudiantes:
        if datos_de_estudiante['numero_de_matricula'] == numero_de_matricula:
            estudiante = datos_de_estudiante

    print('\nDatos del estudiante')

    for llave, valor in estudiante.items():
        if llave == 'genero':
            valor = obtener_descripcion_de_genero(valor)

        print('    {0}: {1}'
            .format(
                llave.capitalize().replace('_', ' '),
                valor
            )
        )

    print('\nAl estudiante le faltan {0} años para terminar con la carrera'
        .format(DURACION_DE_CARRERAS_EN_ANIOS - estudiante['cantidad_de_anios_aprobados'])
    )

    print('\nEl costo que tuvo la carrera hasta la fecha es de ${0}'
        .format(
            round(estudiante['cantidad_de_anios_aprobados'] * 12 * VALOR_DE_CUOTA_MENSUAL, 2)
        )
    )


def mostrar_porcentaje_de_estudiantes_por_genero(estudiantes: list) -> None:
    """
    PRE:  'estudiantes', debe ser una variable de tipo list
    POST: Muestra por consola, el porcentaje de estudiantes por
          género
    """

    total_de_estudiantes: int = len(estudiantes)
    estudiantes_por_genero: dict = dict()

    for tupla_de_genero in GENEROS:
        genero: str = tupla_de_genero[0]

        estudiantes_por_genero[genero] = 0

        for estudiante in estudiantes:
            if estudiante['genero'] == genero:
                estudiantes_por_genero[genero] += 1

    for llave, valor in estudiantes_por_genero.items():
        descripcion_de_genero: str = obtener_descripcion_de_genero(llave)

        print('\nDe un total de {0} estudiantes, un {1}% se corresponden al género "{2}"'
            .format(
                total_de_estudiantes,
                round(valor * 100 / total_de_estudiantes, 2),
                descripcion_de_genero
            )
        )


def mostrar_cantidad_de_estudiantes(estudiantes: list) -> None:
    """
    PRE:  'estudiantes', debe ser una variable de tipo list
    POST: Muestra por consola, la cantidad de estudiantes que
          se han ingresado hasta el momento
    """

    print(f'\nHay un total de {len(estudiantes)} estudiantes, en la univerdad')


def registrar_estudiante(estudiantes: list) -> None:
    """
    PRE:  'estudiantes', debe ser una variable de tipo list
    POST: Solicita los datos de un estudiante, y los carga a
          la lista de estudiantes
    """
    print('\nA continuación, se deberán ingresar los datos del estudiante')

    nombre: str = ingresar_nombre()
    apellido: str = ingresar_apellido()
    genero: str = ingresar_genero()
    edad: int = ingresar_edad()
    numero_de_matricula: int = ingresar_matricula(estudiantes, True)
    cantidad_de_anios_aprobados: int = ingresar_anios_aprobados()

    estudiantes.append({
        'nombre': nombre,
        'apellido': apellido,
        'genero': genero,
        'edad': edad,
        'numero_de_matricula': numero_de_matricula,
        'cantidad_de_anios_aprobados': cantidad_de_anios_aprobados
    })


def main() -> None:
    """
    PRE:  No tiene
    POST: Inicializa el programa de la universidad
    """

    opciones: list = [
        'Dar de alta un estudiante',
        'Mostrar cantidad de estudiantes',
        'Mostrar porcentaje de alumnos por género',
        'Consulta datos de estudiante, por número de matrícula',
        'Salir'
    ]
    estudiantes: list = list()
    opcion: str = ingresar_opcion_de_usuario(opciones)

    while opcion != len(opciones):    
        if opcion == 1:
            registrar_estudiante(estudiantes)

        elif opcion == 2:
            mostrar_cantidad_de_estudiantes(estudiantes)

        elif opcion == 3:
            mostrar_porcentaje_de_estudiantes_por_genero(estudiantes)

        elif opcion == 4:
            mostrar_datos_de_estudiante_por_matricula(estudiantes)

        opcion = ingresar_opcion_de_usuario(opciones)


main()
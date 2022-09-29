""" Funciones
Es una forma de escribir código reutilizable, o
reducir la complejidad de mi código.

Una función debe y solo debe realizar una función en concreto.

Las funciones reciben un nombre, y deben recibir un nombre acorde 
a su tarea.

Las funciones deben ser cargadas por el intérprete antes de ser
invocadas o llamadas.

Las funciones permiten hacer branching, lo que quiere decir que el puntero
de la ejecución, una vez invocada la función, salta al pedazo de código
que se encuentra dentro de la función.

"""


def mifuncion():
    print('Nombre')
    print('Mas lineas')

    for i in range(1, 6):
        print(i)


print('Antes')

mifuncion()

print('Después')

"""
Las funciones tienen parámetros.
Son valores o objetos que se le dan a la función, a la hora de escribirla
y serán las variables sue le darán al comienzo de ejecución de la 
función. Dentro de los paréntesis de la declaración.
"""


def saludo(nombre):
    print('Hola', nombre)


saludo('Agustin')


def suma(a, b):
    print(a + b)


suma(5, 4)

"""
Las funciones pueden tener funciones dentro del bloque de código.
Para esto no hay limites, pero no es algo muy visto hacer mas de una 
indentación dentro de la primer función
"""


def matematicas(a, b):
    def suma(a, b):
        print(a + b)

    def resta(a, b):
        print(a - b)

    def masoperaciones(a, b):
        def multiplicacion(a, b):
            print(a * b)
    
        multiplicacion(a, b)

    suma(a, b)
    resta(a, b)
    masoperaciones(a, b)


matematicas(5, 4)

"""
Las funciones tiene variables, que a la hora de escribir se llaman parametros,
a la hora de invocar las funciones se llaman argumentos.

"""

hoyHace = 12.0 # Variable global
temperatura = 13.0  # variable global


def mifuncion2(nombre):
    hoyHace = 6.0  # variable local (vairable shadowing)
    print('Temperatura', temperatura)
    print(f'Hola {nombre} la temperatura es de {hoyHace}')


mifuncion2('Agustin')
print('hoyHace', hoyHace)

"""
Las variables de funcions solo existen dentro de la función, en cambio las variables
de afuera de una función si las puedo usar dentro de una función,
pero estas si le doy un valor dentro de la función enmascaran a las variables 
globales. Hay que tener esto en cuenta, ya que puede ser algo util en ciertos
casos, pero puede traer errores. Una vez finalizada la ejecución de la función, las 
variables locales son destruidas, y en el caso de estar enmascarando una 
función global esta vuelve al esta original antes de la ejecución de la función.

Esto se le llama variable shadowing
-------

se pueden volver globales las variables locales, utilizando la palabra
reservada 'global'
"""

hoyHace = 12.0 # Variable global


def mifuncion2(nombre):
    global hoyHace  # De esta manera, las modificaciones que hagamos en la var serán globales
    hoyHace = 6.0  
    print('Temperatura', temperatura)
    print(f'Hola {nombre} la temperatura es de {hoyHace}')


mifuncion2('Agustin')


"""
Parametros opcionales al invocar a la función, a estos se le da un valor 
por default a la hora de declarar la variable. Esto debe hacerse cumpliendo una regla
los parametros opcionales siempre deben estar al final de la lista de parametros,
ya que teniendo en cuenta que al asignar los valores de los parametros no opcionales,
el compilador no podra entender a cual se le esta asignando valor

"""


def mifuncion3(nombre='Juan'):  # Asignación de valor pór default
    print("Hola ", nombre)


mifuncion3()  # Como se puede ver, a esta función si la puedo llamar si dale un valor del parametro


def suma2(a=1, b=5, c=1):
    print(a + b + c)


suma2(c=9, b=3)


def suma3(*args):  # Parámetros variables
    resultado1 = 0
    for arg in args:
        resultado1 += arg
    return resultado1


suma3(1, 2, 3, 4, 5, 6)

""" Named parameters
kwargs son opcionales


"""


def suma4(**kwargs):  # Cuando utilizamos **kwargs tenemos un diccionario
    for key, value in kwargs.items():
        print(key, '=', value)
    if 'coche' in kwargs and kwargs['coche'] == 'bonito':
        print('Tu coche es bonito')


suma4(a='piso', b='rojo', coche='bonito')


def suma5(**kwargs):
    if 'coche' not in kwargs:
        return  # El return funciona terminando la ejecución de la función
    if kwargs['coche'] == 'bonito':
        print('Tu coche es bonito')


suma5(coche='bonito')  # en este caso si imprime
suma5()  # En este caso la función no realiza ninguna acción

"""
Las funciones rara vez van a usar prints, la buena practica 
sería que estas devuelvan valores.
return es lo tipico en las funciones.
Las funciones devuelven con return 0 o mas valores.
"""


def suma6(a, b):
    return a + b


resultado = suma6(2, 4)


def operaciones(a, b):
    return a + b, a - b, a * b, a / b


print(operaciones(2, 4))  # nos devuelve una tupla con todos los valores
suma, resta, multi, divi = operaciones(2, 4)  # de esta manera almacenamos los valores en variables individuales
print('suma =', suma)
print('resta =', resta)
print('multi =', multi)
print('divi =', divi)
print(operaciones(2, 4)[0])  # Indice de la tupla
"""
Si llegase a poner menos nombres de variables que valores que devuelve la 
función, esto generaría un error.

Para guardar los valores de una función que devuelve muchos valores, hay
dos opciones, lo guardamos en una variable en forma de tupla, o en 
tantas variables como devuelva la función.
"""


# operador ternario en if
def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inicial  # operador ternario

    resultado1 = 0
    for x in range(inicial, final + 1):
        resultado1 += x

    return resultado1


print(sumador(inicial=15))
print(sumador())
print(sumador(final=5))


# Función anónima "lambda"
anonima = lambda: print('Hola')
anonima()

# Función anónima con parámetros
anonima2 = lambda nombre, apellido: print('Hola', nombre, apellido)
anonima2('Agustin', 'Rodriguez')

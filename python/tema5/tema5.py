""" Funciones
Es un forma de escribir código re utilizable, o 
reducir la complejidad de mi código.

Una función debe y solo debe realizar un función en concreto.

Las funciones reciben un nombre, y deben recibir un nombre acorde 
a su tarea.

Las funciones deben ser cargadas por el interprete antes de ser 
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
print('hoyHace',hoyHace)

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

mifuncion3() # Como se puede ver, a esta función si la puedo llamar si dale un valor del parametro




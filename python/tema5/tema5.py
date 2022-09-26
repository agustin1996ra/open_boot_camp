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


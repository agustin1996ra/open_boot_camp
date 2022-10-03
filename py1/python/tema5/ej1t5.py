""" Ejercicio 1:
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
"""


def bisiesto(anio):
    es_bisiesto = False
    if anio % 4 == 0 and not anio % 400 == 0:
        es_bisiesto = True
    return es_bisiesto


anio_ingresado = int(input('Ingrese un año: '))
resultado = bisiesto(anio_ingresado)
if resultado:
    print(f'El año {anio_ingresado} es bisiesto')
else:
    print(f'El año {anio_ingresado} no es bisiesto.')

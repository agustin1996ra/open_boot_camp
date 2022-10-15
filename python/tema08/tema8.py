numero = 511
texto = 'quijote'
otromas = 1.2

# print("El número es %d y el texto es %s y tiene %f" % (numero, texto, otromas))
# print("El número es {} y el texto es {} y tiene {}".format(numero, texto, otromas))
# print("Valor flotante: %.1f" % otromas)

print(f'El número es {numero} y el texto es {texto} y tiene {otromas}')


#

num = 511
print(type(num))

numtxt = str(num)
print(type(numtxt))

print(repr(num))
print(type(repr(num)))


class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # sobre carga de métodos
    # Implemento mi solución a un método existente
    def __str__(self):  # salidas informales
        return f'Mi nombre es {self.nombre} y valgo {self.precio}'

    def __repr__(self):  # Salidas Técnicas
        return f'Juguete({self.nombre}, {self.precio})'


j1 = Juguete('Potato', 10.5)
print(j1)
print(str(j1))
print(repr(j1))

cadena = 'en un lugar de la manchA'
print(cadena.capitalize())
print(cadena.title())
print(cadena.count('a'))
print(cadena.lower().count('a'))
numero = '5'
print(numero.isdigit())
print(numero.isalnum())
print(numero.isalpha())
cadena2 = '          en un lugar de la manchA     '
print(cadena2)
print(cadena2.strip())
print(cadena2.lstrip())
print(cadena2.rstrip())

print(cadena2.split())
print(cadena2.split('n'))
print(cadena2.endswith('manchA'))
print(cadena2.endswith('mancha'))

# Manipulación de ficheros

f = open('./wiki_hola.txt', 'r')

""" modos:
r : Lectura
a : append
w : escritura
x : create

t : texto
b : binary
+ : plus
"""
linea1 = f.readline()
linea2 = f.readline()
linea3 = f.readline()
datos = f.read()
datos2 = f.read(18)  # leer solo 18 bits

f.close()

print(datos)
print(datos2)
print(linea1)
print(linea2)
print(linea3)






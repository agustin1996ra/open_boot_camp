f = open('mifichero.txt', 'w')
lista = [
    'una linea\n',
    'dos lineas\n',
    'tres lineas\n'
]
f.write('datos\n')
f.write('datos2\n')
f.writelines(lista)
f.close()


# Hacemos una función
def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n'
        f.write(linea)

    f.close()


lista = [
    'una linea',
    'dos lineas',
    'tres lineas'
]
escribe('./fichero.txt', lista)

# Serializar datos
import pickle


class Juguete:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre


j1 = Juguete('Potato', 10.5)
print(j1.get_nombre())
f = open('datos.bin', 'wb')
pickle.dump(j1, f)
f.close()



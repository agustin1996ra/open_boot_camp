"""
En este ejercicio, deberás crear un archivo py donde crees un archivo
.txt, abras y escribas dentro del archivo. Para ello, tendrás que acceder
dos veces al archivo creado.
"""


def main():
    f = open('archivo.txt', 'w')
    f.write('Creamos el archivo\n')
    f.close()

    f = open('archivo.txt', 'a')
    f.write('Añadimos una segunda linea\n')
    f.write('Añadimos también una tercera\n')
    f.close()

    # leemos e imprimimos por consola el contenido del archivo
    f = open('archivo.txt', 'r')
    lineas = f.readlines()
    for linea in lineas:
        print(linea)

        
if __name__ == '__main__':
    main()

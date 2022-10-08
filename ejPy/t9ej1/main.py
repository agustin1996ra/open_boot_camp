"""
Crea un script que le pida al usuario una lista de países (separados por comas). Estos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados
alfabéticamente y separados por comas.
"""
import pprint


def main():

    paises = []

    while True:

        pais = input('Introduzca el nombre de un pais: ').title()
        paises.append(pais)
        bandera = input('Si desea continuar agregando países oprima enter,\nsi no introduzca cualquier caractér: ')
        if bandera == '':
            continue
        else:
            break

    paises = list(set(paises))
    paises.sort()
    print('La lista de países ordenada es:')
    print(paises)


if __name__ == '__main__':
    main()

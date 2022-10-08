"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
import functools


def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    impares = filter(lambda x: x % 2 != 0, numeros)
    sumatoria = functools.reduce(lambda x, y: x+y, impares)
    print(f'La suma de los números impares de la lista {numeros}\nes {sumatoria}')


if __name__ == '__main__':
    main()




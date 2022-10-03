
a = 5
b = 6

resultado = a < b
print(f'a= {a} es menor que b={b} {resultado}')
print(a > b)

print('tabla de verdad de and')
print(f'T and T = {True and True}')
print(f'T and F = {True and False}')
print(f'F and T = {False and True}')
print(f'F and F = {False and False}')

print('tabla de verdad de or')
print(f'T or T = {True or True}')
print(f'T or F = {True or False}')
print(f'F or T = {False or True}')
print(f'F or F = {False or False}')

print('tabla de verdad de and')
print(f'T xor T = {True ^ True}')
print(f'T xor F = {True ^ False}')
print(f'F xor T = {False ^ True}')
print(f'F xor F = {False ^ False}')


lista = [1, 2, 3, 4, 5]

for valorActual in lista:
    print(valorActual)


lista = ['hola', 'mensaje', 'adios']

for palabra in lista:
    print('Palabra actual:', palabra)

    if palabra == 'mensaje':
        print('He encontrado la palabra mensaje')
        break

if 'mensaje' in lista:
    print('He encontrado la palabra mensaje')

lista = [3, 4, 1, 2, 5]
print(lista)

listaOrdenada = sorted(lista)
print(listaOrdenada)
listaOrdenada = sorted(lista, reverse=True)
print(listaOrdenada)

valor = 5

if valor == 1:
    print('Valor es 1')
elif valor == 2:
    print('Valor es 2')
elif valor == 3:
    print('Valor es 3')
elif valor == 4:
    print('Valor es 4')
elif valor == 5:
    print('Valor es 5')

match valor:
    case 1:
        print('Valor es 1')
    case 2:
        print('Valor es 2')
    case 3:
        print('Valor es 3')
    case 4:
        print('Valor es 4')
    case 5:
        print('Valor es 5')


# Else del for

lista = ['hola', 'mensaje', 'adios']
for palabra in lista:
    if palabra == 'mensaje':

        print('Encuentro la palabra mensaje')
        break
else:
    print('No encuentro nada')


# -

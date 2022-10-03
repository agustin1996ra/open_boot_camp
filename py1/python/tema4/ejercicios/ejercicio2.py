"""
Escribe un programa capaz de mostrar todos los números
impares desde un numero de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8,
el programa debe imprimir por consola: [3, 5, 7] 
"""

n_i = 2  # Numero inicial
n_f = 8  # Numero final
numeros_impares = []
for numero in range(n_i, n_f + 1):
    
    if numero % 2 != 0:
        numeros_impares.append(numero)

print(numeros_impares)

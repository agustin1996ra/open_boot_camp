# Estructuras de control

- control de flujo
- setencias de operaciones
- Switch

## Control de flujo

El control de flujo sirve para guiar la ejecucion de nuestro programa.

Operaciones condicionales y test de veracidad.

### Operadores condicionales
- `>` Mayor
- `>=` Mayor o igual
- `==` Exactamente igual
- `<=` Menor o igual
- `<` Menor

Combinacion de operaciones booleanas
- Y : `and` o `&&`
- O : `or ` o `||`

## Sentecias condicionales
En Python solo tenemos dos sentecias condicionales las cuales son `if` y `while`.

### `if`
El `if` tiene como parametro una condicion.(o varias condiciones)
El `elif` me permite anadir una condicione a un `if` existente
Tambien podemos usar `else` para cuando ninguan de la condiciones de la estructura `if` se cumple.


 

### `while`
Mientra la condicion sea verdadera, se van ejecutar las acciones dentro del la estructura `while`.

Palabras para control de bucles
- `continue`:
	esta palabra nos permite pasar al proximo ciclo de ejecucion
- `break`
	Esta palabra rompe la ejecuciopn del bucle


## Bucle `for`

```python
lista = [1, 2, 3, 4, 5]

for valorActual in lista:
	print(valorActual)

```

`range(x,y)` es un conjunto de rango que incluye `x` y excluye `y`
en caso de tener un solo valor de parametro, es el valor final y comenzara desde 0.

```python
lista = ['hola', 'mensaje', 'adios']

for palabra in lista:
    print('Palabra actual:', palabra)

    if palabra == 'mensaje':
        print('He encontrado la palabra mensaje')
        break
```

```python
if 'mensaje' in lista:
    print('He encontrado la palabra mensaje')
```



### Else del for

En caso de que un for no se rompa con un `break` entre en la estructura `else`.

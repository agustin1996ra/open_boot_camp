
# Tipos de objetos de Python

- numeros enteros
- cadenas de texto
- booleanos
- numeros flotantes
- listas
- tuplas
- diccionarios 
- conjuntos

## Numeros enteros y flotantes

### Operadores


## Cadenas de texto

Las cadenas de texto funcionan como arrays donde estas tienen un indice donde se aloja cada caracter que la compone.


Los metodos para las cadenas son:

### `cadena.capitalize()`
Este metodo tranforma la primera letra de la cadena en mayuscula.

### `cadena.title()`
Este metodo transforma a su version mayuscula cada una de las primaras letras de las palabras.

### `cadena.lower()`
Este metodo tranforma a todas las letras de la cadena en su version minuscula.

### `cadena.upper()`
Este metodo vuelve a todas las letras de la cadena a su version mayuscula.

### `cadena.replace('a', 'o')`
Este metodo remplaza cada una de las letras ingresadas como primer parametro y las remplaza por la letra ingresada 
como segundo parametro. En este caso remplaza todas las 'a' por 'o'.

### `cadena.find('hola')`
Este comando dara como resultado un numero entero, que será la posicion en la que empieza la subcadena
dentro de la cadena.

### `cadena.split()`
Este metodo por defecto, separa a la cadena por los espacios, pero si yo le entrego un caracter como parametro,
me va a separar la cadena teniendo como separador el caracter le dei.
La cadena se separara en pequeñas cadenas que se guardaran en una lista.

### `cadena.join(lista_depalabras)`
Este metodo me juntara todas las palabras dadas en una lista, usando como caracter de union la  `cadena`.
ej: `' '.join(['Hola', 'esto', 'es', 'una', 'cadena'])`
esto tendria como resultado la siquiente cadena:
`'Hola esto es una cadena'`
> Tener en cuenta que puedo usar como caracter o cadena de coneccion, lo que se me ocurra.

### `cadena.isnumeric()`
Este medoto es una comprobacion booleana, si el o los caracteres de la cadena son numeros, devuelve `True`, en
caso de contener una caracter letra devuelve `False`.




Todos los metodos anteriores son combinables.

## Booleanos



## Listas

## Tuplas

## Diccionarios

## Conjuntos

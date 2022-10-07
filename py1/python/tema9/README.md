# Introducción a la biblioteca estándar de Python y funciones Built-in

Son funciones que trae el propio lenguaje a nivel del intérprete.

Donde se encuentra la documentación: [La biblioteca estándar de Python](https://docs.python.org/es/3/library/index.html)
Funciones Built-in: [Documentación de las funciones Built-in](https://docs.python.org/es/3/library/functions.html)

## Paradigma de la programación multi-hilo

Para que esto funcione debemos bloquear nuestro programa ejecutándose. Esto se logra con `while True: pass` o con un `time.sleep()`. Es necesario que sea así para que le dé tiempo a mi proceso a ejecutarse.
```python
import _thread
import time

def hora_actual(nombre_thread, tiempo_de_espera):
    count = 0
    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(hora_actual, ('thread_uno', 1))
_thread.start_new_thread(hora_actual, ('thread_dos', 2))

print('He disparado ya los hilos')
while True:
    pass

```

## Funciones logging
Estos son mensajes que tienen varios niveles de jerarquía, hay algunos que se imprimirán por pantalla y otros no.
Se utiliza para ir trazando lo que realiza el programa. Para usar un logger y que no usemos los `print()`
```python
import logging


logging.info('Arrancando programa') # por default este no se imprimirá
logging.warning("Hace calor")
logging.basicConfig(level=logging.INFO)  # Cambio la jerarquía desde la que se imprimirá
# Todos los niveles desde info en adelante se imprimirán desde ahora
logging.info('Arrancando programa')
logging.error('test')
logging.debug('prueba de debug')
logging.critical('adios')
```
Las jerarquías de logging ban desde debug hasta critical:
- .debug  # menor jerarquía
- .info
- .warning
- .error
- .critical

## Funciones `map`, `filter` y `reduce`
### Función `map(función, iterable, iterable(opcional), ...)`:
Retorna un iterador al que le aplica una función a cada elemento del iterable, devolviendo el resultado.
Si se le pasan argumentos adicionales de tipo iterable, la función debe tomar la misma cantidad 
de argumentos y es aplicado a los elementos de todos los iterables en paralelo. Con iterables múltiples,
el iterador se detiene cuando el iterable más corto se agota.

### Función `filter(función, iterable)`:
Construye un iterador a partir de aquellos elementos del `iterable`, para los cuales `función` retorna 
`True`. `iterable` puede ser una secuencia, un contenedor que soporta iteración, o un iterador. 
Si `función` es **None**, se asume la función identidad, es decir, todos los elementos del `iterable`
que son False son eliminados.

Ten en cuenta que `filter(función, iterable)` es equivalente a la expresión de un generador `item for
item in iterable if función(item)` si la función no es **None** y a `item for item in iterable if item`
si la función es **None**.

### Función `reduce(función, iterable[, initializer])`
Aplicar una función de dos argumentos acumulativos a los elementos del `iterable`, de izquierda a 
derecha, para reducir los iterables a un solo valor. Por ejemplo, `reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])`
calcula `((((1+2)+3)+4)+5)`. El argumento de la izquierda, `x`, es el valor acumulado y el de la derecha,
`y`, es el valor de actualización del iterable. Si el `initializer` opcional está presente, se coloca
antes de los ítems del `iterable` en el cálculo, y sirve como predeterminado cuando el `iterable` está 
vacío. Si no se da el `initializer` y el `iterable` contiene sólo un elemento, se retorna el primer elemento.

Aproximadamente equivalente a:
```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```
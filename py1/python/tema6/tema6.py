""" Tema 6: programación orientada a objetos
Clases y objetos
Con la metodología de la programación orientada a objetos, podemos agrupar una
serie de funciones en torno a un objeto.

Un objeto es una representación del mundo real, en un lenguaje de programación.

Los objetos tienen métodos, estos son acciones que realizamos.
Los objetos también tienen propiedades, una propiedad es una variable que le
pertenece al objeto y esta puede mutar.
"""


# Para definir una clase
class Juguete:
    _encendido = False  # Propiedad (estas no necesitan declararse antes de ser utilizadas)
    color = 'verde'  # no se puede modificar desde afuera
    # Definicion de metodos

    def cambia_color(self):
        self.color = 'azul'

    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


# Crear una instancia, es iniciar un objeto
d1 = Juguete()  # Objeto
print(d1.color)
d1.cambia_color()  # Accedo a el método
d1.color = "amarillo"  # Puedo sobrescribir una propiedad en cualquier momento
print(d1.color)


""" 
Por defecto en python todo es publico, ya que no existen los conceptos de 
publico, privado y protegido

Hay una convención en python a la hora de nombrar las propiedades y métodos, 
que nos dice, que si una propiedad empieza con un guion bajo, no lo deberíamos 
poder modificar desde afuera.
Por ejemplo:
"""

d1._encendido = True  # Esto no se debe hacer porque va en contra de la convención

"""
A la hora de definir un método dentro de la clase, que modifica el valor de una 
propiedad debo dentro de la funcion, llamar con la palabra resevada self, a la 
variable o propiedad que deseo modificar. Por que si no el compilador entedera
que solo al escribir la variable, tiene que crear una variable local a la 
función / método
"""

d1.apaga()
print(d1.isEncendido())

d2 = Juguete()
d2.enciende()
print(d2.isEncendido())

"""
Cada vez que yo llame a una instancia de una clase, esta tendra un pedazo de
memoria para almacenar sus propiedades, y cada instancia nueva, ocupara otra parte 
de memoria, separada de las otras. No habrá inter dependencia entre instancias.
"""


#  Clases estaticas

"""
"""

class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1


# Herencia
"""

"""


class Potato(Juguete):
    def __init__(self):
        print("Estoy en el constructor de Potato")

    def poneroreja(self):
        pass

    def sacaroreja(self):
        pass


p = Potato()
p.enciende()
print(p.isEncendido())  # Utilizo los métodos heredados


"""
Herencia multiple
"""

class Dino(Potato, Juguete):

    def verEscamas(self):
        pass


d = Dino()
print(dir(d))  # Con este método podemos ver los todos los métodos, los heredados también


"""
En python los constructores de las clases, se llaman con la palabra
reservada def __init__(self):

Los constructores sirven para setear las propiedades iniciales de la 
nueva instancia generada.
"""


class SenioraPotato(Potato):
    nombre = None

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        print('Estoy en el constructor', nombre)
        self.color = 'verde'

    def ponercartera(self):
        pass

    def __del__(self):
        print("Estoy en el destructor de la clase", self.__class__)


sp = SenioraPotato('Agustin')
print(sp.color)

print(sp.nombre)
print("a")
del sp  # Invoco el destructor cuando lo deseo
print("b")

"""
Los destructores se programas para eliminar la instancia, ósea elimina el objeto,
y esto lo hace cuando no encuentra mas llamadas a la instancia.

Esto por defecto python lo hace con su recolector de basura.
Este hace esta función de eliminar todo lo que el compilador ya sabe no va a
volver a utilizar. 
"""

"""
Las clase en python realmente no existen, son diccionarios
"""


def saluda(nombre):
    print("Hola que tal", nombre)


diccionario = {
    'saluda': saluda
}

diccionario['saluda']("Agustin")


# Clases Abstractas
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def dihola(self):
        print("Hola")


# a = Animal() Esto rompe la ejecución, por una clase abstracta no se puede instanciar
"""
Esto se debe a que es una clase que tiene métodos que se deben implementar, una 
vez se herede de esta clase.

Esto se utiliza para demarcar una implementación parcial de ciertos métodos 
que pertenecen a la clase. Estos métodos no implementados, en la clase abstracta
serán concebidos conceptualmente por el programador de clase abstracta,
y tendrán que ser implementados, por aquel programador, que desee
heredar los métodos y propiedades de esa clase abstracta
"""


class Perro(Animal):
    def sonido(self):
        print('Guau')


pe = Perro()
pe.sonido()
pe.dihola()


class Gato(Animal):
    def sonido(self):
        print("Miau")


ga = Gato()
ga.sonido()
ga.dihola()


"""
Esto es una composición de varias clases, para llegar a la clase coche
"""

class Motor:
    tipo = 'eléctrico'


class Ventanas:
    cantventanas = 5

    def cambiarcantidad(self, valor):
        self.cantventanas = valor


class Ruedas:
    cantruedas = 4


class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()


class Coche:
    motor = Motor()
    carroceria = Carroceria()


c = Coche()
print("Motor es", c.motor.tipo)
print("Ventanas:", c.carroceria.ventanas.cantventanas)
c.carroceria.ventanas.cambiarcantidad(3)
print("Ventanas:", c.carroceria.ventanas.cantventanas)


class Categorias:
    idcategorias = 0
    nombre = "lapiz"


class Proveedores:
    idproveedor = 0
    nombre = "fabercastel"


class Productos:
    idproducto = 0
    categoriaProducto = Categorias()
    precio = 0
    tamano = 0
    tipoDeProducto = 0
    cifProveedor = Proveedores()


lapiz = Productos()
print(lapiz.cifProveedor.nombre)
print(lapiz.categoriaProducto.idcategorias)
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
class Dino:
    encendido = False  # Propiedad (estas no necesitan declararse antes de ser utilizadas)
    # Definicion de metodos

    def enciende(self):
        pass


# Crear una instancia, es iniciar un objeto
d1 = Dino()  # Objeto
d1.enciende()  # Accedo a el método
print(d1.encendido)
d1.encendido = True  # Puedo sobrescribir una propiedad en cualquier momento
print(d1.encendido)


""" 
Por defecto en python todo es publico, ya que no existen los conceptos de 
publico, privado y protegido

Hay una conveción en python a la hora de nombrar las propiedades y métodos, 
que nos dice, que si una propiedad empieza con un guion bajo, no lo deberíamos 
poder modificar desde afuera.
"""



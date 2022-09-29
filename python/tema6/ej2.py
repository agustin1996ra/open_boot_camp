""" Ejercicio 2
En este segundo ejercicio tenés que crear un programa que tenga una
clase llamada Alumno que tenga como atributos su nombre y su nota. Debés
definir los métodos para inicializar sus atributos, imprimirlos y
mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""


class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f'El alumno {self.nombre} tiene una nota de {self.nota}')

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_nota(self, nota):
        self.nota = nota

    def get_nombre(self):
        return self.nombre

    def get_nota(self):
        return self.nota


# Utilizando la función __init__, dando sus argumentos y el print inicial
a1 = Alumno('Agustin', 8)

# Cambio las propiedades con los sets
a1.set_nombre('Agustin Rodriguez')
a1.set_nota(9)
# Obtengo los valores con los gets
print(f'El alumno {a1.get_nombre()} tiene la nota {a1.get_nota()}')

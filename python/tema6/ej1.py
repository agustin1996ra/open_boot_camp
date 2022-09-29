""" Ejercicio 1
En este ejercicio tenés que crear la clase Vehículo la cual
tendrá los siguientes atributos:
- Color
- Ruedas
- Puertas

Por otro lado crearás la clase Coche la cual heredará de Vehículo
y tendrá los siguientes atributos:
- Velocidad
- Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo
por consola.
"""


class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def pintar(self, pintura):
        self.color = pintura

    def set_ruedas(self, valor):
        self.ruedas = valor

    def set_puertas(self, valor):
        self.puertas = valor


class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def set_velocidad(self, vel):
        self.velocidad = vel

    def set_cilindrada(self, cil):
        self.cilindrada = cil


auto = Coche()
auto.pintar('rojo')
auto.set_cilindrada(1.6)
auto.set_puertas(4)
auto.set_ruedas(4)
auto.set_velocidad(80)

print('Color de auto:', auto.color)
print('N° de ruedas:', auto.ruedas)
print('N° de puertas:', auto.puertas)
print('Velocidad:', auto.velocidad)
print('Cilindrada:', auto.cilindrada)


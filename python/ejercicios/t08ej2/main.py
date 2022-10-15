"""
En este segundo ejercicio, tendrás que crear un archivo py y
dentro crearas una clase Vehículo, harás un objeto de ella,
lo guardarás en una archivo y luego lo cargarás
"""
import pickle


class Vehiculo:
    modelo = ''
    color = ''
    tipo_motor = ''

    def __init__(self, modelo, color, tipo_motor):
        self.modelo = modelo
        self.color = color
        self.tipo_motor = tipo_motor

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_tipo(self):
        return self.tipo_motor


def main():
    auto = Vehiculo('Fiat 128', 'rojo', 'nafta')
    f = open('objeto.bin', 'wb')
    pickle.dump(auto, f)
    f.close()

    f = open('objeto.bin', 'rb')
    autito = pickle.load(f)
    f.close()

    print(autito.get_modelo())
    print(autito.get_color())
    print(autito.get_tipo())


if __name__ == '__main__':
    main()

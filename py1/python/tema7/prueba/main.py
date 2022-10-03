import operaciones as op  # Cuando se carga un modulo se ejecuta su código
import paquetes.suma
import pprint as p


def main():
    res = op.suma(2, 2)
    res_resta = op.resta(5, 3)
    print("Hola en main()", res, res_resta)
    print(op.como_me_llamo())
    print(paquetes.suma.suma(2, 2))

    mp = paquetes.suma.Multiplicador()  # Instancio la clase dentro del paquete y dentro del modulo suma
    print(mp.multiplica(5, 2))  # Uso el método de mi instancia

    p.pprint(locals())



print('Soy el modulo:', __name__)
if __name__ == '__main__':
    main()

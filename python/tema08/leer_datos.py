import pickle
import escribir

f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()
print(type(potato))
print(potato.get_nombre(), 'Precio:', potato.precio)

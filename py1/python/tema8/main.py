def main():
    usuarios = listar_usuarios()
    print(usuarios)


def listar_usuarios():
    f = open('/etc/passwd', 'r')
    datos = f.readline()
    f.close()
    for linea in datos:
        if linea[0] == '#':
            continue
        if linea[0] == '_':
            continue

        partes = linea.split()
        print(linea)
        print(partes)


if __name__ == '__main__':
    main()
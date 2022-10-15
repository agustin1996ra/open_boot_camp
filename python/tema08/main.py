def main():
    usuarios = listar_usuarios()
    for usuario in usuarios:
        print(f'Usuario: {usuario}')


def listar_usuarios():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()
    resultado = []
    for linea in datos:
        if linea[0] == '#':
            continue
        if linea[0] == '_':
            continue

        partes = linea.split(':')
        resultado.append(partes[0])
    return resultado


if __name__ == '__main__':
    main()
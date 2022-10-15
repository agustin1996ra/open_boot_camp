import sqlite3
import getpass


def main():
    crear_usuario(3, 'pepe', 'pep123')


def main2():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('Login incorrecto')


def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'
    print(f'Query a ejecutar: {query}')
    row = cursor.execute(query)
    data = row.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return False

    return True


def crear_usuario(indentificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f'INSERT INTO users(id, username, password) VALUES({indentificador}, "{usuario}", "{clave}")'

    row = cursor.execute(query)
    print(type(row))
    conn.commit()  # es necesario confirmar, a la hora de escribir o eliminar
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

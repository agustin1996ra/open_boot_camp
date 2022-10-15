# Definición y gestión de bases de datos en Python

Una base de datos es una almacén.

Las bases de datos relacionales son como hojas de calculo.

En python se pueden usar las bases de datos relacionales como no relacionales.

Las bases de datos relacionan una tabla con otras.

Mirar bases de datos no relacionales: Casandra, prometeus, influx, mongodb.

Relacionales: MariaDB, MySQL, PostgreSQL, SQLite

Tanto MariaDB, como MySQL o PostgreSQL son programas para construir bases de datos grandes y conectadas a internet, son complejas y tienen muchisimas funciones.

SQLite es un programa que no conecta las bases de datos a internet, ósea, solo se pueden usar para bases de datos locales. Es muy utilizada para proyectos chicos, por que es muy liviana en cuanto a los recursos que necesita para operarse.

## SQLite
### Para instalarlo:
```bash
$ sudo apt install sqlite3
```
### Crear una base de datos con SQLite
Desde la terminal:
```bash
agus@agus-escritorio ~/rep/open_boot_camp/py1/python/tema11 (main) $ sqlite3 mifichero.db
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> CREATE TABLE demo(
   ...> id INT
   ...> nombre TEXT
   ...> );
```
> Para salir `.quit`

Debemos crear almenos una tabla para que al momento de usar el comando `.quit` se cree la base de datos, si salimos sin modificar nada, nuestra base de datos no se creara.

Pra consultar las tablas que tengo creadas uso el comando `.tables`.

Para ver los datos que tengo dentro de una tabla:
```
SELECT * FROM demo;
```
> Siendo en este caso demo en nombre de mi tabla, y * la forma de indicar que deseo todos los datos de la tabla.


Para insertar un registro en una tabla:
```
sqlite> INSERT INTO users(id, username, password) VALUES(1, 'Agus', '1234');
```
> Siendo: users el nombre de mi tabla, los campos y sus valores.


# Requisitos para usar SQLite con python
```
pip install pysqlite3
```

## Conectar mi base de datos 

```python
import sqlite3

conn = sqlite3.connect('miaplicacion.db')

# Aca debe estar mi trabajo con la base de datos

conn.close()  # Este es el método para cerrar el archivo
```

## Cursores
Las bases de datos funcionan trabajando con el concepto de *cursor*.
Un cursor es una variable que va a contener unos datos en un momento determinado.

Si tengo varios datos, mi cursor irá iterando en los datos, y dependiendo del momento del bucle en el que se encuentre, tendrá diferentes datos.

```python
import sqlite3

conn = sqlite3.connect('miaplicacion.db')

cursor = conn.cursor()

cursor.close()  # esto no es necesario, pero es una buena práctica.

conn.close()  
```

## Para ejecutar consultas:
```python
import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users')

for row in rows:
    print(row)

cursor.close()  # esto no es necesario, pero es una buena práctica.
conn.close()  
```

### Para filtrar por el valor de uno de los campos
```python
import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users WHERE username="Agus"')

for row in rows:
    print(row)

cursor.close()  # esto no es necesario, pero es una buena práctica.
conn.close()  
```

## Ejemplo de inicio de sesión
```python
import sqlite3
import getpass

def main():
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
    

if __name__ == '__main__':
    main()
```

## Otro ejemplo
```python
import sqlite3


def main():
    crear_usuario(3, 'pepe', 'pep123')


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

```

## Para no usar `conn.commit()`
```python
import sqlite3


def main():
    crear_usuario(3, 'pepe', 'pep123')


def crear_usuario(indentificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db', isolation_level=None)
    cursor = conn.cursor()

    query = f'INSERT INTO users(id, username, password) VALUES({indentificador}, "{usuario}", "{clave}")'

    row = cursor.execute(query)
    print(type(row))
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

```
> Debemos usar el atributo `isolation_level=None`, para indicar que no se necesita confirmación para los `INSERT`, `DELETE` o `UPDATE`
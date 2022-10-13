"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de
tres columnas: la columna id de tipo entero, la columna nombre que será de tipo
texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que
insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar
los datos por consola.
"""
import sqlite3


def main():
    crear_tabla()
    alumnos = [['agustin', 'rodriguez'],
               ['renzo', 'romani'],
               ['lautaro', 'urquiza'],
               ['federico', 'pfund'],
               ['gabriel', 'romero'],
               ['matias', 'redondo'],
               ['facundo', 'blanco'],
               ['frank', 'biorkman']]
    i = 0
    for alumno in alumnos:
        i += 1
        agregar_alumno(i, alumno[0], alumno[1])

    mostrar_tabla()


def crear_tabla():
    conn = sqlite3.connect('mibasededatos.db')
    cursor = conn.cursor()
    cursor.execute(f'CREATE TABLE alumnos(id INT, nombre TEXT, apellido TEXT);')
    conn.commit()
    cursor.close()
    conn.close()


def agregar_alumno(id, nombre, apellido):
    conn = sqlite3.connect('mibasededatos.db')
    cursor = conn.cursor()
    ex = f'INSERT INTO alumnos VALUES ({id}, "{nombre}", "{apellido}");'
    cursor.execute(ex)
    conn.commit()
    cursor.close()
    conn.close()


def mostrar_tabla():
    conn = sqlite3.connect('mibasededatos.db')
    cursor = conn.cursor()
    rows = cursor.execute(f'SELECT * FROM alumnos;')
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

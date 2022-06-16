import sqlite3
from sqlite3 import Error

# Función para conectar la base de datos, en caso de no existir, las crea
def conectar():
    try:
        conexion = sqlite3.connect('contactos.db')
        return conexion
    except Error as err:
        print('Ha ocurrido un error en la conexión' + str(err))


# Creación de las tablas a la base de datos
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    # Creamos las tablas
    sentencia_sql = '''CREATE TABLE IF NOT EXISTS contactos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellio TEXT NOT NULL,
        empresa TEXT,
        telefono TEXT NOT NULL,
        email TEXT,
        direccion TEXT
    ) '''

    # Ejecutamos la sentencia SQL
    cursor.execute(sentencia_sql)
    # Guardamos los cambios
    conexion.commit()
    # Cerramos la conexion
    conexion.close()


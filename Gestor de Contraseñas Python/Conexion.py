import sqlite3
from sqlite3 import Error

# Función para conectar a la base de datos
def conectar():
    try:
        conexion = sqlite3.connect('database.db')
        return conexion
    except Error:
        print('Ha ocurrido un error en la conexión')


# Función para crear las tablas
def crear_tablas(conexion):
    cursor = conexion.cursor()
    # Creamos las tablas
    sentencia_sql1 = '''CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellio TEXT NOT NULL,
        contrasena_maestra TEXT NOT NULL
    ) '''

    sentencia_sql2 = '''CREATE TABLE IF NOT EXISTS contrasena(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        url TEXT NOT NULL,
        nombre_user TEXT NOT NULL,
        contrasena TEXT NOT NULL,
        descripcion TEXT,
        CONSTRAINT fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id)
    ) '''

    # Ejecutamos
    cursor.execute(sentencia_sql1)
    cursor.execute(sentencia_sql2)

    # Comiteamos y cerramos la conexion
    conexion.commit()
    conexion.close()

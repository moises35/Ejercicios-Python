import hashlib
from Conexion import *


def registrar_usuario(nombre, apellio, contrasena_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO usuario(
                nombre, apellio, contrasena_maestra) 
                VALUES(?, ?, ?)'''
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest()
        datos = (nombre, apellio, cm_cifrada)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return True
    except Error as err:
        return False


def comprobar_password(id, contra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM usuario WHERE id = ? AND contrasena_maestra = ?'
        cm_cifrada = hashlib.sha256(contra.encode('utf-8')).hexdigest()
        cursor.execute(sentencia_sql, (id, cm_cifrada))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        return('Ha ocurrido un error' + str(err))

    


# print(comprobar_usuario())
# print(registrar('Moises', 'Alvarenga', 'moises'))
# print(comprobar_password(2, '123'))
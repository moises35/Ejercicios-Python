import hashlib
from Conexion import *

# Se encarga de registrar una contraseña en la base de datos
def add_password(id_usuario, nombre, url, nombre_user, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO contrasena(
                id_usuario, nombre, url, nombre_user, contrasena, descripcion) 
                VALUES(?, ?, ?, ?, ?, ?)'''
        datos = (id_usuario, nombre, url, nombre_user, contrasena, descripcion)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Registro exitoso'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)


# Función para mostrar todas las contraseñas de un usuario
def mostrar(id_usuario):
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM contrasena WHERE id_usuario = ?'
        cursor.execute(sentencia_sql, (id_usuario,))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        print('Ha ocurrido un error' + str(err))
        return datos


# Función para mostrar una única contraseña
def mostrar_unico(id_usuario, id_contrasena):
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM contrasena WHERE id_usuario = ? AND id = ?'
        cursor.execute(sentencia_sql, (id_usuario, id_contrasena))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print('Ha ocurrido un error' + str(err))
    return datos


# Función para actualizar una contraseña
def modificar_password(id_usuario, id_contrasena, nombre, url, nombre_user, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE contrasena SET 
            nombre = ?, url = ?, nombre_user = ?, contrasena = ?, descripcion = ? 
            WHERE id_usuario = ? AND id = ?'''
        datos = (nombre, url, nombre_user, contrasena, descripcion, id_usuario, id_contrasena)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Modificación exitosa'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)


# Función para eliminar una contraseña
def eliminar_password(id_usuario, id_contrasena):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'DELETE FROM contrasena WHERE id_usuario = ? AND id = ?'
        datos = (id_usuario, id_contrasena)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Eliminación exitosa'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)
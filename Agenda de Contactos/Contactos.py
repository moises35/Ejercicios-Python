from Conexion import *

# Para insertar en la tabla de la base de datos
def insertar(nombre, apellido, empresa, telefono, email, direccion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO contactos(nombre, apellio, empresa, telefono, email, direccion)
        VALUES(?, ?, ?, ?, ?, ?)'''
        cursor.execute(sentencia_sql, (nombre, apellido, empresa, telefono, email, direccion))
        conexion.commit()
        conexion.close()
        return 'Registro exitoso'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)


# Para consultar todos los registros de la tabla
def consultar():
    registros = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM contactos'''
        cursor.execute(sentencia_sql)
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Error as err:
        print( 'Ha ocurrido un error' + str(err))
        return registros


# Para consultar un registro de la tabla por medio de su ID
def consultar_id(id):
    registros = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''SELECT * FROM contactos WHERE id = ?'''
        cursor.execute(sentencia_sql, (id,))
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Error as err:
        print( 'Ha ocurrido un error' + str(err))
        return registros


# Para modificar un registro de la tabla por medio de su ID
def modificar(id, nombre, apellido, empresa, telefono, email, direccion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''UPDATE contactos SET nombre = ?, apellio = ?, empresa = ?, telefono = ?, email = ?, direccion = ? WHERE id = ?'''
        cursor.execute(sentencia_sql, (nombre, apellido, empresa, telefono, email, direccion, id))
        conexion.commit()
        conexion.close()
        return 'Operación exitosa'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)


# Para eliminar un registro de la tabla por medio de su ID
def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''DELETE FROM contactos WHERE id = ?'''
        cursor.execute(sentencia_sql, (id,))
        conexion.commit()
        conexion.close()
        return 'Operación exitosa'
    except Error as err:
        return 'Ha ocurrido un error' + str(err)
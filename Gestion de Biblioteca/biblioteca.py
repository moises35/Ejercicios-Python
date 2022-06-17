from conexion import *

# Función para insertar un libro en la base de datos
def insertar(titulo, autor, estado):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'INSERT INTO libros (titulo, autor, estado) VALUES (%s, %s, %s)'
        datos = (titulo, autor, estado)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        return 'Libro agregado!'
    except mysql.Error as error:
        return "Ha ocurrido un error: {}".format(error)


# Función que devuelve los registros de la BD
def seleccionar_libros():
    resultado = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM libros'
        cursor.execute(sentencia_sql)
        resultado = cursor.fetchall()
        return resultado
    except mysql.Error as error:
        print("Ha ocurrido un error: {}".format(error))
        return resultado


#  Función que devuelve un registro de la BD
def seleccionar_libro_id(id):
    resultado = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'SELECT * FROM libros WHERE id = %s'
        datos = (id,)
        cursor.execute(sentencia_sql, datos)
        resultado = cursor.fetchall()
        return resultado
    except mysql.Error as error:
        print("Ha ocurrido un error: {}".format(error))
        return resultado


# Para modificar un campo de un libro
def modificar(id, opcion, valor):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'UPDATE libros SET '
        if opcion == 1:
            sentencia_sql += 'titulo = %s '
        elif opcion == 2:
            sentencia_sql += 'autor = %s '
        elif opcion == 3:
            sentencia_sql += 'estado = %s '
        sentencia_sql += 'WHERE id = %s'
        datos = (valor, id)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        return 'Libro modificado!'
    except mysql.Error as error:
        return "Ha ocurrido un error: {}".format(error)



# Función para eliminar un libro mediante su ID
def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = 'DELETE FROM libros WHERE id = %s'
        datos = (id,)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        return 'Libro eliminado!'
    except mysql.Error as error:
        return "Ha ocurrido un error: {}".format(error)
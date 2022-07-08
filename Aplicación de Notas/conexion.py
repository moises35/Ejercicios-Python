import mysql.connector as mysql

def conectar():
    try:
        conexion = mysql.connect(
            host='localhost',
            user='root',
            password='',
            database='datos'
        )
        print('Conexión exitosa!')
        return conexion
    except mysql.Error as error:
        print("Ha ocurrido un error: {}".format(error))
        return None
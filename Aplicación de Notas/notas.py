from conexion import *
from datetime import date
import os

class Nota:
    def __init__(self, id = '', nombre = '', contenido = ''):
        self.id = id
        self.nombre = f'{nombre}.txt'
        self.contenido = contenido
        self.fecha_creacion = date.today()

    # Método para registrar
    def registrar(self):
        try:
            con = conectar()
            cursor = con.cursor()
            sentencia_sql = 'INSERT INTO notas(nombre, fecha) VALUES(%s, %s)'
            datos = (self.nombre, self.fecha_creacion)
            cursor.execute(sentencia_sql, datos)
            self.crear_archivo()
            con.commit()
            con.close()
            print('Nota registrada!') 
        except mysql.Error as error:
            print("Ha ocurrido un error: {}".format(error)) 


    # Método para crear archivo
    def crear_archivo(self):
        try:
            archivo = open(f'./notas/{self.nombre}', 'w')
            archivo.write(self.contenido)
            archivo.close()
        except FileNotFoundError as err:
            print('Ha ocurrido un error ' + err)

    # Método para ver notas
    def ver_notas(self):
        resultado = []
        try:
            con = conectar()
            cursor = con.cursor()
            sentencia_sql = 'SELECT * FROM notas'
            cursor.execute(sentencia_sql)
            resultado = cursor.fetchall()
            con.close()
            return resultado
        except mysql.Error as error:
            print("Ha ocurrido un error: {}".format(error))
            return resultado


    def buscar(self):
        resultado = []
        try:
            con = conectar()
            cursor = con.cursor()
            sentencia_sql = f'SELECT * FROM notas where id = {self.id}'
            cursor.execute(sentencia_sql)
            resultado = cursor.fetchall()
            con.close()
            return resultado
        except mysql.Error as error:
            print("Ha ocurrido un error: {}".format(error))
            return resultado

    def eliminar(self):
        try:
            con = conectar()
            cursor = con.cursor()
            sentencia_sql = f'DELETE FROM notas WHERE id = {self.id}'
            cursor.execute(sentencia_sql)
            con.commit()
            con.close()
            print('Nota eliminada!')
        except mysql.Error as error:
            print("Ha ocurrido un error: {}".format(error))
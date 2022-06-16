from Contactos import *
from tabulate import tabulate

# Función para pedir los datos e insertarlos
def agregar_contacto():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    empresa = input('Empresa: ')
    telefono = input('Teléfono: ')
    email = input('Email: ')
    direccion = input('Dirección: ')
    print(insertar(nombre, apellido, empresa, telefono, email, direccion))


# Función para mostrar los contactos
def mostrar_contactos():
    registros = consultar()
    if(len(registros) > 0):
        print(tabulate(registros, headers=['ID', 'NOMBRE', 'APELLIDO', 'EMPRESA', 'TELEFONO', 'EMAIL', 'DIRECCION'], tablefmt='fancy_grid'))
    else:
        print('No hay contactos')


# Función para mostrar un contacto por medio de su ID
def mostrar_contacto_id(): 
    id = input('ID: ')
    registros = consultar_id(id)
    if(len(registros) > 0):
        print(tabulate(registros, headers=['ID', 'NOMBRE', 'APELLIDO', 'EMPRESA', 'TELEFONO', 'EMAIL', 'DIRECCION'], tablefmt='fancy_grid'))
    else:
        print('No hay contactos con ese ID')


# Función para modificar un contacto por medio de su ID
def modificar_contacto():
    id = (input('ID del contacto a modificar: '))
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    empresa = input('Empresa: ')
    telefono = input('Teléfono: ')
    email = input('Email: ')
    direccion = input('Dirección: ')
    print(modificar(id, nombre, apellido, empresa, telefono, email, direccion))


# Función para eliminar un contacto por medio de su ID
def eliminar_contacto():
    id = int(input('ID del contacto a eliminar: '))
    print(eliminar(id))
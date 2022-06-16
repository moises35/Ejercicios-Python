# Importar módulo del SO
import os 

# Para que las contraseñas se muestren cifradas
from getpass import getpass

# Para que se muestre en forma de tablas (hay que descargar)
# pip install tabulate
from tabulate import tabulate

# importar módulos creados
from Conexion import *
from Usuario import *
from Contrasenia import *

def inicio():
    # Creamos la conexión y las tablas
    conexion = conectar()
    crear_tablas(conexion)
    ejecucion = True
    while(ejecucion):
        os.system('cls')
        print('Bienvenido al gestor de contraseñas')
        print('Para continuar, ingrese una opción:')
        print('\t1. Iniciar sesión')
        print('\t2. Crear una cuenta')
        print('\t3. Salir')
        try:
            opcion = int(input('--> Opción: '))
            if opcion == 1:
                id = input('Ingrese su id: ')
                contrasenia = getpass('Ingrese su contraseña: ')
                datos = comprobar_password(id, contrasenia)
                if len(datos) > 0:
                    print('\nBienvenido ' + datos[0][1] + ' ' + datos[0][2] + '!!!\n')
                    os.system('pause')
                    menu(datos)
                else:
                    print('Error. Verifique su contraseña y su usuario')
                os.system('pause')
            elif opcion == 2:
                nombre = input('Ingrese su nombre: ')
                apellido = input('Ingrese su apellido: ')
                contrasenia_maestra = getpass('Ingrese su contraseña maestra: ')
                if registrar_usuario(nombre, apellido, contrasenia_maestra):
                    print('Usuario creado correctamente')
                else:
                    print('Ha ocurrido un error')
                os.system('pause')
            elif opcion == 3:
                ejecucion = False
            else:
                print('No ingresó una opción valida!!!')
        except Error as err:
            print('Ocurrió un error: ', err)
        


# Función para mostrar el menú
def menu(datos):
    while True:
        os.system('cls')
        print('Selecione una de las siguientes opciones: ')
        print('\t1. Añadir contraseña')
        print('\t2. Ver todas las contraseñas')
        print('\t3. Visualizar una contraseña')
        print('\t4. Modificar contraseña')
        print('\t5. Eliminar contraseña')
        print('\t6. Salir')
        try:
            opcion = int(input('--> Opción: '))
            if opcion == 1:
                agregar(datos)
            elif opcion == 2:
                ver_todo(datos)
            elif opcion == 3:
                ver_unico(datos)
            elif opcion == 4:
                modificar(datos)
            elif opcion == 5:
                eliminar(datos)
            elif opcion == 6:
                break
            else:
                print('No ingresó una opción valida!!!')
            os.system('pause')
        except:
            print('Ha ocurrido un error')


def agregar(datos):
    print('Ingrese los datos de la contraseña: ')
    nombre = input('\t-->Nombre: ')
    url = input('\t-->URL: ')
    nombre_user = input('\t-->Nombre de usuario: ')
    contrasena = getpass('\t-->Contraseña: ')
    descripcion = input('\t-->Descripción: ')
    exito = add_password(datos[0][0], nombre, url, nombre_user, contrasena, descripcion)
    if exito == 'Registro exitoso':
        print(exito)
    else:
        print(exito)



def ver_todo(datos):
    lista = mostrar(datos[0][0])
    if len(lista) > 0:
        nuevaLista = []
        for lis in lista:
            convertido = list(lis)
            convertido.pop(1)
            convertido[4] = '**********'
            nuevaLista.append(convertido)
        print(tabulate(nuevaLista, headers=['ID', 'Nombre', 'URL', 'Nombre de usuario', 'Contraseña', 'Descripción'], tablefmt='fancy_grid'))
    else:
        print('No hay contraseñas registradas')


def ver_unico(datos):
    masterPass = getpass('Ingrese la contraseña maestra: ')
    masterPass = hashlib.sha256(masterPass.encode('utf-8')).hexdigest()
    if masterPass == datos[0][3]:
        id = input('Ingrese el ID de la contraseña: ')
        password = mostrar_unico(datos[0][0], id)
        if len(password) > 0:
            nuevaLista = []
            for lis in password:
                convertido = list(lis)
                convertido.pop(1)
                nuevaLista.append(convertido)
            print(tabulate(nuevaLista, headers=['ID', 'Nombre', 'URL', 'Nombre de usuario', 'Contraseña', 'Descripción'], tablefmt='fancy_grid'))
        else:
            print('No hay contraseñas registradas con ese ID')
    else:
        print('Contraseña maestra incorrecta')



def modificar(datos):
    masterPass = getpass('Ingrese la contraseña maestra: ')
    masterPass = hashlib.sha256(masterPass.encode('utf-8')).hexdigest()
    if masterPass == datos[0][3]:
        id = input('Ingrese el ID de la contraseña: ')
        nombre = input('Ingrese el nuevo nombre: ')
        url = input('Ingrese la nueva URL: ')
        nombre_user = input('Ingrese el nuevo nombre de usuario: ')
        contrasena = getpass('Ingrese la nueva contraseña: ')
        descripcion = input('Ingrese la nueva descripción: ')
        exito = modificar_password(datos[0][0], id, nombre, url, nombre_user, contrasena, descripcion)
        if exito == 'Actualización exitosa':
            print(exito)
        else:
            print(exito)
    else:
        print('Contraseña maestra incorrecta')



def eliminar(datos):
    masterPass = getpass('Ingrese la contraseña maestra: ')
    masterPass = hashlib.sha256(masterPass.encode('utf-8')).hexdigest()
    if masterPass == datos[0][3]:
        id = input('Ingrese el ID de la contraseña: ')
        exito = eliminar_password(datos[0][0], id)
        if exito == 'Eliminación exitosa':
            print(exito)
        else:
            print(exito)
    else:
        print('Contraseña maestra incorrecta')



inicio()
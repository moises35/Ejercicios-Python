from msilib.schema import Error
import os
import Conexion
from Funcionalidades import *

def opciones():
    print('Seleccione una opción:')
    print('\t1. Agregar contacto')
    print('\t2. Mostrar contactos')
    print('\t3. Buscar contacto')
    print('\t4. Modificar contacto')
    print('\t5. Eliminar contacto')
    print('\t6. Salir')

def main():
    Conexion.crear_tabla()
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = input('Opción: ')
            if opcion == '1':
                agregar_contacto()
            elif opcion == '2':
                mostrar_contactos()
            elif opcion == '3':
                mostrar_contacto_id()
            elif opcion == '4':
                modificar_contacto()
            elif opcion == '5':
                eliminar_contacto()
            elif opcion == '6':
                print('Muchas Gracias!!! Vuelva pronto😄')
                break
            else:
                print('Opción inválida')
            os.system('pause')
    except Error as err:
        print('Ha ocurrido un error: ' + str(err))

main()
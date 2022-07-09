from msilib.schema import Error
import funcionalidades
import os

# Función para obtener las opciones del programa
def opciones():
    print('Seleccione una opción:')
    print('\t1. Registrar una cita medica')
    print('\t2. Ver todas las citas medicas')
    print('\t3. Ver citas medicas de hoy')
    print('\t4. Modificar estado de una cita médica')
    print('\t5. Eliminar cita medica')
    print('\t6. Salir')

# Ejecución principal del programa
def main():
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = input('Opción: ')
            if opcion == '1':
                funcionalidades.registrar()
            elif opcion == '2':
                funcionalidades.mostrarTodo()
            elif opcion == '3':
                funcionalidades.mostrarHoy()
            elif opcion == '4':
                funcionalidades.modificar()
            elif opcion == '5':
                funcionalidades.eliminar()
            elif opcion == '6':
                print('Muchas Gracias!!! Vuelva pronto😄')
                break
            else:
                print('Opción inválida')
            os.system('pause')
    except Error as e:
        print('Ha ocurrido un error: ' + e)
    

main()
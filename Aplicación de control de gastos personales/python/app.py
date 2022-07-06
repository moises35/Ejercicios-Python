from msilib.schema import Error
import funcionalidades
import os

# Función para obtener las opciones del programa
def opciones():
    print('Seleccione una opción:')
    print('\t1. Registrar un nuevo movimiento')
    print('\t2. Ver todos los movimientos')
    print('\t3. Buscar un movimiento')
    print('\t4. Modificar un movimiento')
    print('\t5. Eliminar un movimiento')
    print('\t6. Salir')

# Ejecución principal del programa
def main():
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = input('Opción: ')
            if opcion == '1':
                funcionalidades.registrarMovimiento()
            elif opcion == '2':
                funcionalidades.mostrarTodo()
            elif opcion == '3':
                funcionalidades.buscar_movimiento()
            elif opcion == '4':
                funcionalidades.modificarMovimiento()
            elif opcion == '5':
                funcionalidades.eliminarMovimiento()
            elif opcion == '6':
                print('Muchas Gracias!!! Vuelva pronto😄')
                break
            else:
                print('Opción inválida')
            os.system('pause')
    except Error as e:
        print('Ha ocurrido un error: ' + e)
    

main()
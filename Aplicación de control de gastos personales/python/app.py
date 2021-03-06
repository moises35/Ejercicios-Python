from msilib.schema import Error
import funcionalidades
import os

# Funci贸n para obtener las opciones del programa
def opciones():
    print('Seleccione una opci贸n:')
    print('\t1. Registrar un nuevo movimiento')
    print('\t2. Ver todos los movimientos')
    print('\t3. Buscar un movimiento')
    print('\t4. Modificar un movimiento')
    print('\t5. Eliminar un movimiento')
    print('\t6. Salir')

# Ejecuci贸n principal del programa
def main():
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = input('Opci贸n: ')
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
                print('Muchas Gracias!!! Vuelva pronto馃槃')
                break
            else:
                print('Opci贸n inv谩lida')
            os.system('pause')
    except Error as e:
        print('Ha ocurrido un error: ' + e)
    

main()
from msilib.schema import Error
import funcionalidades
import os

# Funci贸n para obtener las opciones del programa
def opciones():
    print('Seleccione una opci贸n:')
    print('\t1. Registrar producto')
    print('\t2. Consultar todos los productos')
    print('\t3. Buscar un producto')
    print('\t4. Modificar un producto')
    print('\t5. Eliminar un producto')
    print('\t6. Nueva venta')
    print('\t7. Salir')

# Ejecuci贸n principal del programa
def main():
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = input('Opci贸n: ')
            if opcion == '1':
                funcionalidades.registrar()
            elif opcion == '2':
                funcionalidades.mostrarTodo()
            elif opcion == '3':
                funcionalidades.buscar()
            elif opcion == '4':
                funcionalidades.modificar()
            elif opcion == '5':
                funcionalidades.eliminar()
            elif opcion == '6':
                funcionalidades.vender()
            elif opcion == '7':
                print('Muchas Gracias!!! Vuelva pronto馃槃')
                break
            else:
                print('Opci贸n inv谩lida')
            os.system('pause')
    except Error as e:
        print('Ha ocurrido un error: ' + e)
    

main()
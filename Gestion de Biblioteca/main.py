import os
from funcionalidades import *

def opciones():
    print('Seleccione una opción:')
    print('\t1. Agregar libro')
    print('\t2. Ver todos los libros')
    print('\t3. Buscar un libro')
    print('\t4. Modificar un libro')
    print('\t5. Eliminar un libro')
    print('\t6. Salir')


# id, titulo, autor, estado
def main():
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                agregar_libro()
            elif opcion == 2:
                mostrar_libros()
            elif opcion == 3:
                mostrar_libro_id()
            elif opcion == 4:
                modificar_libro()
            elif opcion == 5:
                eliminar_libro()
            elif opcion == 6: 
                break
            else:
                print('Opción inválida')
            os.system('pause')
    except ValueError:
        print('Opción inválida')

main()
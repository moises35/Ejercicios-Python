import os
from funcionalidades import *

def opciones():
    print('Seleccione una opción:')
    print('\t1. Nueva nota')
    print('\t2. Ver notas')
    print('\t3. Ver contenido')
    print('\t4. Modificar una nota')
    print('\t5. Eliminar una nota')
    print('\t6. Salir')


# id, titulo, autor, estado
def main():
    try:
        while(True):
            os.system('cls')
            opciones()
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                registrar()
            elif opcion == 2:
                verNotas()
            elif opcion == 3:
                verContenido()
            elif opcion == 4:
                modificar()
            elif opcion == 5:
                eliminar()
            elif opcion == 6: 
                break
            else:
                print('Opción inválida')
            os.system('pause')
    except ValueError:
        print('Opción inválida')

main()
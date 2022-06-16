from msilib.schema import Error
import os
from Tareas import *

def opciones():
    print('***********************')
    print('*        ToDo         *')
    print('***********************')
    print('--> 1. Agregar tarea')
    print('--> 2. Editar tarea')
    print('--> 3. Marcar tarea como completada')
    print('--> 4. Borrar tarea')
    print('--> 5. Ver todas las tareas')
    print('--> 6. Salir')


def menu():
    tareas = []
    id = 1
    while(True):
        try:
            os.system('cls')
            opciones()
            opcion = int(input('--> Opción: '))
            if opcion == 1:
                id = agregar_tarea(tareas, id)
                print('Agregar tarea')
            elif opcion == 2:
                editar_tarea(tareas)
                print('Editar tarea')
            elif opcion == 3:
                tarea_completada(tareas)
                print('Marcar tarea como completada')
            elif opcion == 4:
                borrar_tarea(tareas)
                print('Borrar tarea')
            elif opcion == 5:
                mostrar_tareas(tareas)
                print('Ver todas las tareas')
            elif opcion == 6:
                break
            else:
                print('Opción inválida!!!')
            os.system('pause')
        except Error as err:
            print('Ha ocurrido un error: ', err)

menu()
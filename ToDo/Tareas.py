class Tarea:
    def __init__(self, nombre, fecha, id):
        self.nombre = nombre
        self.fecha = fecha
        self.estado = False
        self.id = id

    def __str__(self):
        return f"ID: {self.id}; Tarea: {self.nombre}; Fecha: {self.fecha}; Estado:{self.estado}"

def agregar_tarea(tareas, id):
    nombre = input('Ingrese el nombre de la tarea: ')
    fecha = input('Ingrese la fecha de la tarea: ')
    tareas.append(Tarea(nombre, fecha, id))
    id += 1
    return id


def editar_tarea(tareas):
    id = int(input('Ingrese el id de la tarea: '))
    for tarea in tareas:
        if tarea.id == id:
            tarea.nombre = input('Ingrese el nombre de la tarea: ')
            tarea.fecha = input('Ingrese la fecha de la tarea: ')
            break


def tarea_completada(tareas):
    id = int(input('Ingrese el id de la tarea: '))
    for tarea in tareas:
        if tarea.id == id:
            tarea.estado = True
            break


def borrar_tarea(tareas):
    id = int(input('Ingrese el id de la tarea: '))
    for tarea in tareas:
        if tarea.id == id:
            tareas.remove(tarea)
            break


def mostrar_tareas(tareas):
    for tarea in tareas:
        print(tarea)
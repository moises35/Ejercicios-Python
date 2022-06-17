from biblioteca import *
from tabulate import tabulate

# Pide los datos y llama a la función de insertar
def agregar_libro():
    titulo = input('Ingrese el título del libro: ')
    autor = input('Ingrese el autor del libro: ')
    estado = 'Disponible'
    print(insertar(titulo, autor, estado))


# Muestra todos los libros en la base de datos
def mostrar_libros():
    resultado = seleccionar_libros()
    if len(resultado) > 0:
        print(tabulate(resultado, headers=['ID', 'TITULO', 'AUTOR', 'ESTADO'], tablefmt='fancy_grid'))
    else:
        print('No hay libros registrados')


# Realiza la busqueda de un libro en especifico mediante el ID
def mostrar_libro_id():
    id = int(input('Ingrese el ID del libro: '))
    resultado = seleccionar_libro_id(id)
    if len(resultado) > 0:
        print(tabulate(resultado, headers=['ID', 'TITULO', 'AUTOR', 'ESTADO'], tablefmt='fancy_grid'))
    else:
        print('No hay libros registrados con ese ID')


# Modificar algun dato del libro
def modificar_libro():
    id = int(input('Ingrese el ID del libro: '))
    print('Que desea modificar?:')
    print('1. Titulo')
    print('2. Autor')
    print('3. Estado')
    opcion = int(input('Ingrese el número de la opción: '))
    while(opcion < 1 or opcion > 3):
        opcion = int(input('Ingrese una opcion valida: '))
    valor = input('Ingrese el nuevo valor: ')
    modificar(id, opcion, valor)



# Elimina un libro mediante el ID
def eliminar_libro():
    id = int(input('Ingrese el ID del libro: '))
    print(eliminar(id))
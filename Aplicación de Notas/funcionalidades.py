from notas import Nota
from tabulate import tabulate
import os 

def registrar():
    nombre = input('Ingrese el nombre de la nota: ')
    contenido = input('Ingrese el contenido de la nota: ')
    nota = Nota(nombre = nombre, contenido = contenido)
    nota.registrar()


def verNotas():
    nota = Nota()
    resultado = nota.ver_notas()
    if len(resultado) > 0:
        print(tabulate(resultado, headers=['ID', 'NOMBRE DEL ARCHIVO', 'FECHA DE CREACIÓN'], tablefmt='fancy_grid'))
    else:
        print('No hay notas registradas')



def verContenido():
    id = input('Ingrese el ID de la nota: ')
    nota = Nota(id = id)
    resultado = nota.buscar()
    if len(resultado) > 0:
        archivo = open(f'./notas/{resultado[0][1]}', 'r')
        print('\n' + archivo.read() + '\n')
        archivo.close()
    else:
        print('No se encontró la nota')


def modificar():
    archivos = os.listdir('./notas')
    print('Seleccione una nota:')
    for i, archivo in enumerate(archivos):
        print(f'\t{i+1}. {archivo}')
    opcion = int(input('Ingrese una opción: '))
    new_contenido = input('Ingrese el nuevo contenido: ')
    archivo = open(f'./notas/{archivos[opcion-1]}', 'w')
    archivo.write(new_contenido)
    archivo.close()

def eliminar():
    id = input('Ingrese el ID de la nota: ')
    nota = Nota(id = id)
    nota.eliminar()
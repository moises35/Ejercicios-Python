import requests
# Para imprimir en tablas
from tabulate import tabulate
# Importar constantes
from constantes import *
from datetime import date

def registrar():
    # Obtener datos del producto
    name = input('Ingrese el nombre del paciente: ')
    detalle = input('Ingrese el detalle de su cita: ')
    fecha = input('Ingrese la fecha de su cita: ')
    hora = input('Ingrese la hora: ')
    data = {'name': name, 'detalle': detalle, 'fecha': fecha, 'hora': hora, 'estado': 'Agendada'}
    # Enviar petición POST al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'citas/create'
    r = requests.post(url=url, data=data)
    # Imprimir el resultado
    print(r.text)


def mostrarTodo():
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'citas/all'
    respuesta = requests.get(url=url)
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    print(tabulate(datos, HEADER_CITA, tablefmt='fancy_grid'))


def mostrarHoy():
    fecha = date.today().strftime("%d-%m-%Y")
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'citas/viewToday'
    respuesta = requests.get(url=url, data={'fecha': fecha})
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    print(tabulate(datos, HEADER_CITA, tablefmt='fancy_grid'))


def modificar():
    id = input('Ingrese el ID del paciente: ')
    estado = 'Atendido'
    data = {'estado': estado}
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'citas/update/' + id
    r = requests.post(url=url, data=data)
    # Imprimir el resultado
    print(r.text)


def eliminar():
    id = input('Ingrese el ID del paciente: ')
    # Enviar petición DELETE al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'citas/delete/' + id
    r = requests.post(url=url)
    # Imprimir el resultado
    print(r.text)    
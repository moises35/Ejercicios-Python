# Para realizar peticiones (pip install requests)
import requests
# Para imprimir en tablas
from tabulate import tabulate
# Importar constantes
from constantes import *

# Función para registrar un movimiento
def registrarMovimiento():
    # Pedimos los datos
    tipo = input('Ingrese el tipo de movimiento: \n - Ingreso \n - Egreso \n')
    cantidad = input("Ingrese la cantidad: ")
    fecha = input("Ingrese la fecha: ")
    data = {'tipo': tipo, 'cantidad': cantidad, 'fecha': fecha}
    # Establecemos la url
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'movimientos/create'
    respuesta = requests.post(url = url, data=data)
    print(respuesta.text)


# Función para ver todos los movimientos
def mostrarTodo():
    # Establecemos la url
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'movimientos/all'
    respuesta = requests.get(url = url)
    # Convertimos los datos a un array
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    # Imprimimos los datos
    print(tabulate(datos, headers= HEADERS_TABLE, tablefmt='fancy_grid'))


# Función para buscar un movimiento por ID
def buscar_movimiento():
    # Pedimos los datos
    id = input("Ingrese el id del movimiento: ")
    # Establecemos la url
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'movimientos/search/' + (id)
    respuesta = requests.get(url = url)
    # Convertimos los datos a un array
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    # Imprimimos los datos
    print(tabulate(datos, headers= HEADERS_TABLE, tablefmt='fancy_grid'))


#  Función para modificar el campo de un movimiento
def modificarMovimiento():
    # Pedimos los datos
    id = input("Ingrese el id del movimiento: ")
    campo = int(input("Ingrese el campo a modificar: \n- 1. Tipo \n- 2. Cantidad \n- 3. Fecha \n"))
    if(campo == 1):
        campo = 'tipo'
    elif(campo == 2):
        campo = 'cantidad'
    elif(campo == 3):
        campo = 'fecha'
    else:
        print('Opción inválida')
        campo = ''
        return

    new_valor = input("Ingrese el nuevo valor: ")
    data = {'campo': campo, 'new_valor': new_valor}
    # Establecemos la url
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'movimientos/update/' + (id)
    respuesta = requests.post(url = url, data=data)
    print(respuesta.text)


# Función para eliminar un movimiento
def eliminarMovimiento():
    # Pedimos los datos
    id = input("Ingrese el id del movimiento: ")
    # Establecemos la url
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'movimientos/delete/' + (id)
    respuesta = requests.post(url = url)
    print(respuesta.text)
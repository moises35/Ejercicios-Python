# Para realizar peticiones (pip install requests)
from locale import normalize
import requests
# Para imprimir en tablas
from tabulate import tabulate
# Importar constantes
from constantes import *

def registrar():
    # Obtener datos del producto
    nombre = input('Nombre del producto: ')
    descripcion = input('Descripcion del producto: ')
    precio = input('Precio del producto: ')
    # Crear un diccionario con los datos del producto
    producto = {
        'nombre': nombre,
        'descripcion': descripcion,
        'precio': precio
    }
    # Enviar petición POST al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'ventas/create'
    r = requests.post(url=url, data=producto)
    # Imprimir el resultado
    print(r.text)


def mostrarTodo():
    # Enviar petición GET al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'ventas/all'
    respuesta = requests.get(url=url)
    # Imprimir el resultado
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    print(tabulate(datos, headers=['ID', 'Nombre', 'Descripcion', 'Precio'], tablefmt='fancy_grid'))


def buscar():
    # Pedir el ID del producto
    id = input('Ingrese el ID del producto: ')
    # Enviar petición GET al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'ventas/search/' + id
    respuesta = requests.get(url=url)
    # Imprimir el resultado
    datos = []
    for dato in respuesta.json():
        temp = []
        for key, value in dato.items():
            temp.append(value)
        datos.append(temp)
    print(tabulate(datos, headers=['ID', 'Nombre', 'Descripcion', 'Precio'], tablefmt='fancy_grid'))


def modificar():
    # Pedir el ID del producto
    id = input('Ingrese el ID del producto: ')
    campo = int(input('Ingrese el campo que desea modificar: \n\t1) Nombre\n\t2)Descripcion\n\t3) Precio\n'))
    if(campo == 1):
        campo = 'nombre'
    elif(campo == 2):
        campo = 'descripcion'
    elif(campo == 3):
        campo = 'precio'
    else:
        print('Campo inválido')
        return
    valor = input('Ingrese el valor que desea asignar: ')
    data = {'campo': campo, 'valor': valor}
    # Enviar petición PUT al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'ventas/update/' + id
    r = requests.post(url=url, data=data)
    # Imprimir el resultado
    print(r.text)


def eliminar():
    # Pedir el ID del producto
    id = input('Ingrese el ID del producto: ')
    # Enviar petición DELETE al servidor
    url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'ventas/delete/' + id
    r = requests.post(url=url)
    # Imprimir el resultado
    print(r.text)    


def vender():
    cliente = input('Ingrese el nombre del cliente: ')
    total = 0
    productos = []
    print('Seleccione los productos: ')
    while True:
        id = input('Ingrese el ID del producto (0 para salir): ')
        if(id == '0'):
            break
        else:
            url = ROUTE_DB_SERVER + PORT_DB_SERVER + 'ventas/search/' + id
            respuesta = requests.get(url=url)
            if(len(respuesta.json())):
                nombre = respuesta.json()[0]['nombre']
                precio = respuesta.json()[0]['precio']
                cantidad = int(input('Ingrese la cantidad: '))
                total_producto = cantidad * float(precio)
                total += total_producto
                productos.append([id, nombre, precio, cantidad, total_producto])
                imprimir(productos, cliente, total)
            else:
                print('Producto no encontrado')

def imprimir(productos, cliente, total):
    print('\n\t\tComprobante de venta')
    print('Cliente: ' + cliente)
    print(tabulate(productos, headers=HEADER_VENTA, tablefmt='simple'))
    print('\t\t\tTotal: ' + str(total))


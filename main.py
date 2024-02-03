from csv_reader import csv_reader
from producto_dao import ProductoDao
import sys

def handler_name(event, context): 
    productos = csv_reader.read()

    for producto in productos:
        ProductoDao.createProducto(producto)

    ProductoDao.queryAllProducto()

    return {
        "statusCode": 200,
        "body": "{'Status': 'Archivos procesados'}",
        "headers": {
            'Content-Type': 'text/html',
        }
    }
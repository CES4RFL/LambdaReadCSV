from producto import Producto
from database_conf import conn

class ProductoDao:

    def queryAllProducto ():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM public.producto")
        print(cursor.fetchall())

    def createProducto(producto:Producto):
        cursor = conn.cursor()
        postgres_insert_query = """INSERT INTO public.producto (cliente, producto, direccion_envio) VALUES (%s, %s, %s)"""
        record_to_insert = (producto.cliente, producto.producto, producto.direccion_envio)
        cursor.execute(postgres_insert_query, record_to_insert)
        conn.commit()

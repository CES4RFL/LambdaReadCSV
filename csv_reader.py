from producto import Producto
import csv
import boto3
import base64

class csv_reader:
    def read() -> list:
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket('nao-reports')
        productos:list = list()
        for my_bucket_object in my_bucket.objects.all():
            print(my_bucket_object)
            document = s3.Object('nao-reports', my_bucket_object.key).get()['Body'].read().decode('utf-8').splitlines()
            csv_reader = csv.reader(document, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    producto = Producto()
                    producto.cliente = row[0]
                    producto.producto = row[1]
                    producto.direccion_envio = row[2]
                    productos.append(producto)
                    line_count += 1
        print(f'Processed {line_count} lines.')
        return productos
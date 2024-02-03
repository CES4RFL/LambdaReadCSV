from dataclasses import dataclass

@dataclass
class Producto:
    cliente: str
    producto: str
    direccion_envio: str

    def __init__(self):
        pass
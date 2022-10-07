class Producto:

    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo

    def set_codigo(self,codigo):
        if codigo==self.codigo:
            print(f'El producto con codigo {codigo} ha sido creado con exito')
        else:
            print(f'Ha habido un error en la creacion del producto {codigo}')

    def set_nombre(self,nombre):
        if nombre==self.nombre:
            print(f'El producto {nombre} se ha creado con exito')
        else:
            print(f'Ha habido un error en la nota de {nombre}')

    def set_precio(self,precio):
        if precio==self.precio:
            print(f'El producto {self.nombre} ha sido creado con exito con un precio de {precio}€')
        else:
            print(f'Ha habido un error en el establecimiento del precio {precio}')

    def set_tipo(self,tipo):
        if tipo==self.tipo:
            print(f'El alumno {self.nombre} es del tipo {tipo}')
        else:
            print(f'Ha habido un error en el establecimiento del tipo {tipo}')

    def __str__(self):
        return f'Codigo: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}€\nTipo: {self.tipo}\n'

    def modificar_precio(self,precio):
        self.precio=precio
        return f'El producto {self.nombre}, ha adquirido un nuevo precio de {self.precio}'
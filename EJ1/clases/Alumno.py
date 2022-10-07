class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def set_nombre(self,nombre):
        if nombre==self.nombre:
            print(f'El alumno {nombre} ha sido creado con exito')
        else:
            print(f'Ha habido un error en la creacion de {nombre}')

    def set_nota(self,nota):
        if nota==self.nota:
            print(f'El alumno {self.nombre} tiene una nota de {nota} puntos')
        else:
            print(f'Ha habido un error en la nota de {self.nombre}')
    
    def __str__(self):
        return f'Nombre del Alumno: {self.nombre}\nNota: {self.nota}\n'

    def calificacion(self):
        if self.nota<5 and self.nota>=0:
            print(f'El alumno {self.nombre} ha suspendido con un {self.nota}.')
        elif self.nota<=10 and self.nota>=5:
            print(f'El alumno {self.nombre} ha aprobado con un {self.nota}.')
        else:
            print(f'La nota {self.nota} no tiene sentido')
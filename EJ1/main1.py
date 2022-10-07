from clases.Producto import Producto
from clases.Alumno import Alumno

def main1():
    a1=Alumno('Diego',8)
    a2=Alumno('Alberto',9)
    a3=Alumno('Javier',3)
    a4=Alumno('Luis',-12)
    a5=Alumno('David',13)
    print(a1.__str__())
    print(a2.__str__())
    print(a3.__str__())
    print(a4.__str__())
    print(a5.__str__())
    a1.calificacion()
    a2.calificacion()
    a3.calificacion()
    a4.calificacion()
    a5.calificacion()
    print()
    print()
    print('Ejercicios 1 y 2 acabados\n______________________________')

    p1=Producto('01F','Manzana',0.25,'Alimento')
    print(p1.__str__())
    pr1=float(input('Que nuevo precio desea ponerle a la manzana (x.xx€): '))
    print(p1.modificar_precio(pr1))
    print()
    print(p1.__str__())

if __name__=='__main__':
    main1()
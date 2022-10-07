from clases.Alumno import Alumno

def main1():
    a1=Alumno('Diego',8)
    a2=Alumno('Alberto',9)
    a3=Alumno('Javier',3)
    a4=Alumno('Luis',-12)
    a5=Alumno('David',13)
    a1.__str__()
    a2.__str__()
    a3.__str__()
    a4.__str__()
    a5.__str__()
    a1.calificacion()
    a2.calificacion()
    a3.calificacion()
    a4.calificacion()
    a5.calificacion()


if __name__=='__main__':
    main1()
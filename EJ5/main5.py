from clases.vehiculo import Vehiculo
from clases.bicicleta import Bicicleta
from clases.camioneta import Camioneta
from clases.motocicleta import Motocicleta
from clases.coche import Coche


def main5():

    vehiculo=Vehiculo('Rojo',4)
    moto=Motocicleta('Rojo',2,'Deportiva',240,15)
    camion=Camioneta('Rojo',4,150,1200,1500)
    print(camion.__str__())
    bici=Bicicleta('Rojo',2,'Deportiva')
    coche=Coche('Rojo',4,150,1200)
    
    print(f'Vehiculo: {vehiculo.__str__()}\nCoche: {coche.__str__()}\n Bicicleta: {bici.__str__()}\nCamioneta: {camion.__str__()}\nMotocicleta: {moto.__str__()}')
    lista=[]
    lista.append(vehiculo)
    lista.append(moto)
    lista.append(camion)
    lista.append(bici)
    lista.append(coche)


if __name__=='__main__':
    main()
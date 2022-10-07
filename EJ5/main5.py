from clases.vehiculo import Vehiculo
from clases.bicicleta import Bicicleta
from clases.camioneta import Camioneta
from clases.motocicleta import Motocicleta
from clases.coche import Coche


def main():

    coche=Vehiculo('Rojo',4)
    print(coche.__str__())

if __name__=='__main__':
    main()
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo


    def __str__(self):
        return Vehiculo.__str__(self) + ", {} ".format(self.tipo)


def main():

    bici=Bicicleta('Rojo',2,'Deportiva')
    print(bici.__str__())

if __name__=='__main__':
    main()
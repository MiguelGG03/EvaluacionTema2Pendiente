from EJ5.clases.vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


def main():

    coche=Coche('Rojo',4,150,1200)
    print(coche.__str__())

if __name__=='__main__':
    main()
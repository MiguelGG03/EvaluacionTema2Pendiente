from coche import Coche

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return Coche.__str__(self) + ", {} kg".format(self.carga)


def main():

    camion=Camioneta('Rojo',4,150,1200,1500)
    print(camion.__str__())


if __name__=='__main__':
    main()
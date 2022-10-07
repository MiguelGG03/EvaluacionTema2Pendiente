from bicicleta import Bicicleta

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {} cm3 ".format(self.velocidad,self.cilindrada)


def main():

    moto=Motocicleta('Rojo',2,'Deportiva',240,15)
    print(moto.__str__())

if __name__=='__main__':
    main()
class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )



def main():

    coche=Vehiculo('Rojo',4)
    print(coche.__str__())

if __name__=='__main__':
    main()
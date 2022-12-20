'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana
'''
class Contribuyente:
    # Constructor
    def __init__(self,nombre , renta):
        self.nombre = nombre
        self.renta = renta
        
        if self.renta < 10000 :
            self.tasa = 0.05 
        elif self.renta < 20000:
            self.tasa = 0.15
        elif self.renta < 35000:
            self.tasa = 0.20
        elif self.renta < 60000:
            self.tasa = 0.30
        else:
            self.tasa = 0.45

    # Método imprimi el impuesto a pagar en archivo ejercicio_2.txt
    def imprimir_impuesto(self):
        impuesto = self.tasa * self.renta
        with open("ejercicio_2.txt", "w") as archivo:
            archivo.write(f"El impuesto a pagar por {self.nombre} asciende a $ {impuesto}")
        

    
        
def main(): 
    renta = int(input("Ingrese renta en CLP (sin comas): "))
    juan = Contribuyente("Juan", renta)
    juan.imprimir_impuesto()


if __name__ == '__main__':
    main()
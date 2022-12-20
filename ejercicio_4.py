'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana
'''
class Contribuyente:
    # Constructor
    def __init__(self, neto, tasa = 0.19):
        self.neto = neto
        self.tasa = tasa

    # Método
    def imprimir(self):
        iva = self.tasa * self.neto
        with open("ejercicio_4.txt", "w") as archivo:
            archivo.write(
            "El total de la factura es el siguiente:\n" + 
            "Neto (sin IVA): " + str(self.neto) + "\n" + 
            "I.V.A.: " + str(iva) + "\n" + 
            "Bruto (neto más I.V.A.): " + str(iva + self.neto) 
            )
        
def main(): 
    empresa = Contribuyente(100)
    empresa.imprimir()

if __name__ == '__main__':
    main()
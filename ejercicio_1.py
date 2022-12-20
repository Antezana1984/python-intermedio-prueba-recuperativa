'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana
'''
class Telefono:
    # Constructor
    def __init__(self, numero):
        self.numero = numero

    # Métodos
    def imprimir(self):
        cadena = self.numero
        cadena[4:12]
        with open("ejercicio_1.txt", "w") as archivo:
            archivo.write(f"El número sin el prefijo ni la extensión es : {cadena[4:12]}")

        
def main(): 
    numero = input("Ingrese número de en el formato +56-123456789-12, incluyendo el + y los guiones: ")
    telefono = Telefono(numero)
    telefono.imprimir()

if __name__ == '__main__':
    main()
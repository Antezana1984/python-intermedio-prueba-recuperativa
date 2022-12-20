'''
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana
'''
class Alumno:
    # Constructor
    def __init__(self):
        self.diccionario = {"matematica": 0.0, "fisica": 0.0, "quimica": 0.0, "historia": 0.0, "lengua": 0.0}
        
    # Método qu pregunta la nota al usuario
    def pregunta_notas(self):
        self.diccionario["matematica"] = float(input("Ingrese nota de matemáticas (float): "))
        self.diccionario["fisica"] = float(input("Ingrese nota de fisica (float): "))
        self.diccionario["quimica"] = float(input("Ingrese nota de quimica (float): "))
        self.diccionario["historia"] = float(input("Ingrese nota de historia (float): "))
        self.diccionario["lengua"] = float(input("Ingrese nota de lengua (float): "))
    
    # Escribe las asignaturas repetidas en el archivo
    def imprimir_notas(self):
        with open("ejercicio_3.txt", "w") as archivo:
            archivo.write(
                f"La lista de asignaturas que debe repetir son las siguientes {list(self.diccionario.keys())}"
            )
    # Elimina del diccionario los aprovados
    def elimina_aprobados(self):
        lista_de_aprobados = []

        # Se recorre el diccionario para encontrar los aprobados
        for contador in self.diccionario:
            if self.diccionario[contador] >= 4.0:
                # Una vez que se encuentra no se puede eliminar inmediatamente el elemento, es por esto 
                # que se guarda la ubicación para elimar el elemento más adelante
                lista_de_aprobados.append(contador)

        for contador in  range(len(lista_de_aprobados)):
            posicicion_a_eliminar = lista_de_aprobados[contador]
            # Se eliminan efectivamente los elementos del diccionario que están aprobados
            del self.diccionario[posicicion_a_eliminar] 
       
def main(): 
    juan = Alumno()
    juan.pregunta_notas()
    juan.elimina_aprobados()
    juan.imprimir_notas()

if __name__ == '__main__':
    main()
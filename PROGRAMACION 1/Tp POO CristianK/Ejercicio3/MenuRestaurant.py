import os 
from metodos import numeroPositivoEntero,numeroPositivoFlotante,esBebida
from Plato import Plato
from Ingrediente  import Ingrediente

class MenuRestaurant:
    platosMenu = []
    def main():
        print("\t---\nBienvenido al menu del restaurante X\n\t---")
        MenuRestaurant.cargarPlatos()
        os.system("cls")
        print("\t--MENU COMPLETO--\n")
        MenuRestaurant.mostrarPlatos()

    @staticmethod
    def cargarPlatos():
        while True:
            print("-------------------\n")
            nombre = input("Ingrese el nombre del plato: ")
            if  nombre == ""  or nombre == "FIN":
                break
            precio = numeroPositivoEntero(f"Ingrese el precio de {nombre}: ")
            bebida = input("¿Es una bebida? (True/False): ")
            if(not esBebida(bebida)):
                print("Ingredientes:\n")
                plato = Plato(nombre, precio, esBebida("false"))
                while True:
                    nombre = input("Nombre: ")
                    if nombre == "" or nombre.lower() in ("fin"):
                        break
                    cantidad = numeroPositivoEntero(f"Ingrese la cantidad de {nombre}: ")
                    undMedida =  input("Unidad de medida: ")
                    ingredienteX = Ingrediente(nombre,cantidad,undMedida)
                    plato.agregarIngrediente(ingredienteX)
                MenuRestaurant.platosMenu.append(plato)
            else:
                plato = Plato(nombre,precio,esBebida("true"))
                MenuRestaurant.platosMenu.append(plato)
            reiniciar = input(f"-----\nIngresar otro plato (S/N)?\n")
            print()
            if reiniciar in ("N","n"):
                break
    


    @staticmethod
    def  mostrarPlatos():
        for plato in MenuRestaurant.platosMenu:
            print(plato)



MenuRestaurant.main()
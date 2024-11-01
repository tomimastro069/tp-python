import os  #os.system("cls")
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
        cantidadPlatos = numeroPositivoEntero("Ingrese la cantidad de platos: ")
        for i in  range(cantidadPlatos):
            print("-------------------\n")
            nombre = input("Ingrese el nombre del plato: ")
            precio = numeroPositivoEntero(f"Ingrese el precio de {nombre}: ")
            bebida = input("¿Es una bebida? (True/False): ")
            if(not esBebida(bebida)):
                print("\tIngredientes:\n")
                listaIngredientes = MenuRestaurant.ingresarIngredientes()
                plato = Plato(nombre, precio, bebida)
                plato.agregarIngredientes(listaIngredientes)
                MenuRestaurant.platosMenu.append(plato)
            else:
                plato = Plato(nombre,precio,bebida)
                MenuRestaurant.platosMenu.append(plato)

    @staticmethod
    def ingresarIngredientes():
        lista_ingredientes = []
        while(True ):
            nombre = input("Ingrese el nombre del ingrediente: ")
            if(nombre == "FIN"):
                break
            cantidad = numeroPositivoEntero(f"Ingrese la cantidad de {nombre}: ")
            unidadMedida = input(f"Ingrese la unidad de medida de {nombre}: ")
            ingredientex = Ingrediente(nombre,cantidad,unidadMedida)
            lista_ingredientes.append(ingredientex)
        return  lista_ingredientes

    @staticmethod
    def  mostrarPlatos():
        for plato in MenuRestaurant.platosMenu:
            print(plato)



MenuRestaurant.main()
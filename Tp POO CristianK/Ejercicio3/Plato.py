class Plato:
    def __init__(self, nombreCompleto,precio,esBebida):
        self.name = nombreCompleto
        self.precio = precio
        self.esBebida = bool(esBebida)
        self.listaIngredientes = []

    def  agregarIngrediente(self, ingrediente):
        self.listaIngredientes.append(ingrediente)

    def getEsBebida(self):
        return self.esBebida

    def __str__(self):
        lista_ingredientes = "\n".join([str(ing) for ing in self.listaIngredientes])
        if  self.esBebida:
            return f"\t\nBebida: {self.name}\n\t Precio: {self.precio}"
        return f"\t\nPlato: {self.name}\n\t Precio: {self.precio}\n\t Ingredientes:\n{lista_ingredientes}"
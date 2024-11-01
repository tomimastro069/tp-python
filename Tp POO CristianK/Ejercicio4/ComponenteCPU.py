class ComponenteCPU:
    def __init__(self,componente,marca,cantidad,precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.componente}\t{self.marca}\t{self.cantidad}\t{self.precio}"
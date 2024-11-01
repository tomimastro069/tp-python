class Ingrediente:
    def __init__(self, nombre, cantidad,unidadMedida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadeMedida = unidadMedida
    def __str__(self):
        return f"---\n\t-Nombre: {self.nombre}\n\t-Cantidad: {self.cantidad}\n\t-Unidad de Medida: {self.unidadeMedida}\n---"
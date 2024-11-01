class Computadora:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.lista_ComponentesCPU = []

    def agregarComponente(self,componente):
        self.lista_ComponentesCPU.append(componente)

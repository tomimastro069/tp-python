from Computadora import Computadora
from ComponenteCPU import ComponenteCPU
from metodos import numeroPositivoEntero, numeroPositivoFlotante

class CostoComputadora:
    compu = Computadora()
    def main():
        CostoComputadora.cargarMarcaModelo()
        CostoComputadora.cargarComponentes()

    def cargarMarcaModelo():
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        compu = Computadora(marca,modelo)
        return compu
    
    def cargarComponentes(compu):
        cantComponentes = numeroPositivoEntero("Ingrese la cantidad de componentes: ")
        for i in range(cantComponentes):
            nombre = input("Nombre del componente: ")
            marca = input("Marca: ")
            cantidad = numeroPositivoEntero(f"Cantidad de {nombre}")
            precio = numeroPositivoFlotante("Ingrese el precio: ")
            componenteX = ComponenteCPU(nombre,marca,cantidad,precio)
            CostoComputadora.compu.agregarComponente(componenteX)
    
    def mostrarComponentes():
        print(f"Marca: {CostoComputadora.compu.marca}")
        print(f"Modelo: {CostoComputadora.compu.modelo}")
        
        for i in range(len(CostoComputadora.compu.lista_ComponentesCPU)):
            pass


CostoComputadora.main()
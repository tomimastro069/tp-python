from Computadora import Computadora
from ComponenteCPU import ComponenteCPU
from metodos import numeroPositivoEntero, numeroPositivoFlotante
import os
class CostoComputadora:
    compu = Computadora("","")
    def main():
        CostoComputadora.cargarMarcaModelo()
        os.system("cls")
        CostoComputadora.cargarComponentes()
        os.system("cls")
        CostoComputadora.mostrarComputadora()

    def cargarMarcaModelo():
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        compu = Computadora(marca,modelo)
        return compu
    
    def cargarComponentes():
        cantComponentes = numeroPositivoEntero("Ingrese la cantidad de componentes: ")
        for i in range(cantComponentes):
            nombre = input("Nombre del componente: ")
            marca = input("Marca: ")
            cantidad = numeroPositivoEntero(f"Cantidad de {nombre}: ")
            precio = numeroPositivoFlotante("Ingrese el precio: ")
            componenteX = ComponenteCPU(nombre,marca,cantidad,precio)
            CostoComputadora.compu.agregarComponente(componenteX)
    
    def determinarCostoTotal(cantidad,precio):
        costoTotal = 0
        if ( (cantidad * precio) <= 50000):
            costoTotal = (cantidad * precio) +  (cantidad * precio) * 0.40
        else:
            costoTotal = (cantidad * precio) +  (cantidad * precio) * 0.30
        return costoTotal

    def mostrarComputadora():
        total = 0
        print("---COMPUTADORA---")
        print(f"Marca: {CostoComputadora.compu.marca}")
        print(f"Modelo: {CostoComputadora.compu.modelo}")
        print("Componentes: ")
        print("Nombre\t Marca\t Cantidad\t PrecioXUnidad\t Subtotal")
        for componente in CostoComputadora.compu.lista_ComponentesCPU:
            subtotal = CostoComputadora.determinarCostoTotal(componente.cantidad, componente.precio)
            print(f"{componente.componente}\t {componente.marca}\t {componente.cantidad}\t\t {componente.precio}\t\t{subtotal}")
            total += subtotal
        if (total <= 50000):
            print(f"Precio sugerido de venta: ${total + (total*0.4)}")
        else:
            print(f"Precio sugerido de venta: ${total + (total*0.3)}")

CostoComputadora.main()
while(True):
    reiniciar = numeroPositivoEntero("Desea reiniciar la computadora\n1_SI\n2_NO\n")
    if  reiniciar == 1:
        os.system("cls")
        CostoComputadora.main()
    else:
        break
print("Fin del programa")

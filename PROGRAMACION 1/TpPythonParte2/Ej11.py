
import numpy
import random
def transpuestam(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 100)
            fila.append(valor)
        matriz.append(fila)
    return matriz


def matrizrotada90grados(matriz):
    matriz = transpuestam(matriz)
    for i in range(0,len(matriz)):
        matriz[i] = numpy.flip(matriz[i])
    return matriz


def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es:")
    for i in Matriz:
        print(i)
    matriz90 = matrizrotada90grados(Matriz)
    print("La matriz girada 90° hacia la derecha es: ")
    for i in matriz90:
        print(i)
        
if __name__ == "__main__":
    Main()






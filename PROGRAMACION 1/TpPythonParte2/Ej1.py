import numpy

def crear_matriz(Filas, Columnas):
    Array = numpy.arange(1, Filas * Columnas + 1)
    matriz = Array.reshape(Filas,Columnas)
    return matriz

def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = crear_matriz(Filas, Columnas)
    print(Matriz)
if __name__ == "__main__":
    Main()

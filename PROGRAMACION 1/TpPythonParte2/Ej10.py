import numpy

from Ej4 import transpuestam

def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"ingrese un valor para la fila {i}  columna {j}:"))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def esSimetrica(matriz):
    return numpy.array_equal(matriz,transpuestam(matriz))

def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es: ")
    for i in Matriz:
        print(i)
    simetrica = esSimetrica(Matriz)
    print("Es simetrica" if simetrica else "NO ES SIMETRICA")

if __name__ == "__main__":
    Main()
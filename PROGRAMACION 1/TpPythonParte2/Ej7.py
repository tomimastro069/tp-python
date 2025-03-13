
import random

def matriz_valida(matriz):
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            print("La matriz no es cuadrada")
            return False
    return True


def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 100)
            fila.append(valor)
        matriz.append(fila)
    return matriz

def diagonal(Matriz):
    diagonal= []
    for i in range(len(Matriz)):
                diagonal.append(Matriz[i][i])
    return diagonal
def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    if not matriz_valida(Matriz):
        print("La matriz no es cuadrada")
        return
    print("La matriz ingresada es:")
    for i in Matriz:
        print(i)
    diagonalm = diagonal(Matriz)
    print("La diagonal extraida dela matriz es: ", diagonalm)


if __name__ == "__main__":
    Main()


"""
Ejercicio 7: Diagonal de una Matriz Cuadrada 
Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
cuadrada.
"""


import numpy


def diagonalMatriz(matriz):
    diagonal = list()
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if i == j:
                diagonal.append(matriz[i][j])
    return diagonal

def main():
    matriz = numpy.array( [[11,2,3],[4,45,6],[7,8,99]] )
    print(f"Matriz: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
    primerEl , segundoEl, tercerEl = diagonalMatriz(matriz)
    print(f"\nDiagonal:\n{primerEl},{segundoEl},{tercerEl}")

if __name__ == "__main__":
    main()
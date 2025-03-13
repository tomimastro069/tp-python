"""
Ejercicio 4: Matriz Transpuesta 
Escribe  un programa  que  calcule  la transpuesta de  una matriz. La transpuesta de  una 
matriz intercambia sus filas por columnas
"""
import numpy

#Codigo propio
def transpuesta(matriz):
    matrizTran = [ [0 for _ in range(3)] for _ in range(3)] #Crea una matriz 3x3. Cada elemento vale 0
    #El simbolo "_" despues del for, significa que no importa el valor en ese espacio.
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            matrizTran[i][j] = (matriz[j][i]) 
    return matrizTran

def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"Matriz: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
    print("\nMatriz transpuesta Propia: ")
    matrizT = transpuesta(matriz)
    print(f"{matrizT[0]}\n{matrizT[1]}\n{matrizT[2]}")

    #Con numpy
    print("\nMatriz transpuesta con Numpy: ")
    matriz = numpy.array(matriz)
    matriz = matriz.T
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

if __name__ == "__main__":
    main()
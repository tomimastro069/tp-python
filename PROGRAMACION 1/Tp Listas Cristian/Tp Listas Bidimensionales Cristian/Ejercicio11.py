"""
Ejercicio 11: Rotar una Matriz 90 Grados 
Escribe  un programa que  gire  una lista bidimensional (matriz) 90 grados en el sentido 
de las agujas del reloj.
"""

#matriz transpuesta y revertir todas las filas con reverse
import numpy
from metodosListas import llenarMatriz,transpuesta

def matriz90Grados(matriz):
    matriz = transpuesta(matriz)
    for i in range(0,len(matriz)):
        matriz[i] = numpy.flip(matriz[i])
    return matriz

def main():
    matriz = llenarMatriz()
    print(matriz)
    matriz = matriz90Grados(matriz)
    print(f"Matriz rotada 90 grados: \n{matriz}")


if __name__ == "__main__":
    main()
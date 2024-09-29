"""
Ejercicio 6: Multiplicar una Matriz por un Escalar 
Escribe un programa que multiplique cada elemento de una lista bidimensional por un 
valor escalar dado por el usuario.
"""
import numpy
from metodosListas import numeroEntero

def multEscalar(matriz,nro):
    matrizNueva = []
    for fila in matriz:
        filaNueva = [elemento * nro for elemento in fila] #Crea una fila donde elemento * nro en cada indice
        matrizNueva.append(filaNueva) #Agrega la fila nueva(array) a la matriz
    return matrizNueva

def main():
    matriz = numpy.array( [[1,2,3],[4,5,6],[7,8,9]] )
    print(f"Matriz: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

    nro = numeroEntero("Ingrese un escalar para multiplicar cada elemento: ")
    matriz = multEscalar(matriz,nro)
    print(f"Matriz multiplicada por {nro}: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")


if __name__ == "__main__":
    main()
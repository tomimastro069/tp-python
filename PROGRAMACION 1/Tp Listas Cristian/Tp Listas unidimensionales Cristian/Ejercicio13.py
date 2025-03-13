"""
Ejercicio  13:  Explique  y  ejemplifique  la  librería  NumPy  para  trabajar  con  matrices  y 
arrays

Numpy: Tiene mayor cantidad de metodos para poder manipular, crear e interactuar con otras matrices o arrays. Cuenta con 
funciones matemáticas de alto nivel para operar con estos arrays.
"""
from metodosListas import llenarLista
import numpy as num


def main():
    lista= num.random.randint(0, 10, size=(3, 3)) #Crear una matriz de 3x3 Con numeros aleatorios entre 0 y 10
    print(f"Lista: {lista}")

    listaInversa = num.linalg.inv(lista) #Invertir la matriz lista y guardarla en otra
    print(f"Lista invertida: {listaInversa}")

if __name__ == "__main__":
    main()
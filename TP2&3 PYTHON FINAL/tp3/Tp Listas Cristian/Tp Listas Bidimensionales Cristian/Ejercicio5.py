"""
Ejercicio 5: Encontrar el Elemento Mayor 
Escribe un programa que encuentre el valor más grande en una lista bidimensional
"""

import numpy

def mayorElemento(matriz):
    mayor = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > mayor:
                mayor = elemento
    return mayor

def main():
    matriz = numpy.array([[10,20,30],[40,50,60],[70,80,90]])

    print(f"Matriz: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
    print(f"\nEl mayor elemento de la matriz es: {mayorElemento(matriz)}")

if __name__ == "__main__":
    main()
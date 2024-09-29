"""
Ejercicio 10: Verificar Matriz Simétrica 
Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique 
si una matriz es simétrica
"""
import numpy
from metodosListas import llenarMatriz,transpuesta

def esSimetrica(matriz):
    return numpy.array_equal(matriz,transpuesta(matriz))

def main():
    matriz = llenarMatriz()
    print(f"Matriz: \n{matriz}")
    simetrica = esSimetrica(matriz)
    print("Es simetrica" if simetrica else "No es simetrica")
    
    
if __name__ == "__main__":
    main()
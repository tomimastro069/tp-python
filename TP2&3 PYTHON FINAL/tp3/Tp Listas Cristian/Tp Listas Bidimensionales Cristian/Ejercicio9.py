"""
Ejercicio 9: Matriz Identidad Inversa 
Crea  un programa  que  genere  una  matriz  identidad  inversa  de  tamaño  n.  Una  matriz 
identidad  inversa  es una matriz  cuadrada donde  los elementos de  la diagonal inversa 
principal son 1 y el resto son 0. 
0 0 0 1 
0 0 1 0 
0 1 0 0 
1 0 0 0
"""
from Ejercicio8 import matrizIdentidad 

def matrizIdenInversa():
    matrizIde = matrizIdentidad() #Devuelve una matriz identidad
    for fila in matrizIde:
        fila.reverse() #Invierte cada fila de la matriz identidad
    return matrizIde

def main():
    matriz = matrizIdenInversa()
    print("Matriz identidad inversa: ")
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}")


if __name__ == "__main__":
    main()
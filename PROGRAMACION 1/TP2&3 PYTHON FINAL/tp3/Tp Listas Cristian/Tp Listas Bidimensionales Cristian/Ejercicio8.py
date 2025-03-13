"""
Ejercicio 8: Matriz Identidad 
Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad 
es una matriz cuadrada donde  los elementos de  la diagonal principal son 1 y el resto 
son:
1 0 0 0
0 1 0 0 
0 0 1 0 
0 0 0 1
"""
def matrizIdentidad():
    matriz = [[0 for _ in range(4)]for _ in range(4)] #Creo una matriz 4x4 con todos los elementos = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz)):
            if i == j:
                matriz[i][j] = 1
    return matriz

def main():
    matriz = matrizIdentidad()
    print(f"Matriz Identidad:")
    print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}")

if __name__ == "__main__":
    main()
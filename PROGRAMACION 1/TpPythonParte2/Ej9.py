from Ej8 import matrizindetidad1

def matrizinversa(Matriz):
    matrizI = matrizindetidad1(Matriz)
    for fila in matrizI:
        fila.reverse()
    return matrizI
def crear_matriz(Filas, Columnas):
    matriz = [[0 for _ in range(Columnas)] for _ in range(Filas)]
    return matriz
def validar(filas, columnas):
    if filas != columnas:
        print("tiene q ser una matriz cuadrada")
        return False
    return True

def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = crear_matriz(Filas, Columnas)
    validar(Filas, Columnas)
    if not validar(Filas, Columnas):
        return
    matriziinversa = matrizinversa(Matriz)
    print("La matriz generada es:")
    for fila in matriziinversa:
        print(fila)
if __name__ == "__main__":
    Main()

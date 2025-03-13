import random

def sumar_filas(matriz):
    sumas_filas = []
    for fila in matriz:
        suma_fila = sum(fila)
        sumas_filas.append(suma_fila)
    return sumas_filas

def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 100)
            fila.append(valor)
        matriz.append(fila)
    return matriz

def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es:")
    for fila in Matriz:
        print(fila)
    sumas_filas = sumar_filas(Matriz)
    print("Las sumas de cada fila son:")
    for i, suma in enumerate(sumas_filas):
        print(f"Fila {i + 1}: {suma}")

if __name__ == "__main__":
    Main()

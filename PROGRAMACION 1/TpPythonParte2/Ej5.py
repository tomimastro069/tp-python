import random

def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 100)
            fila.append(valor)
        matriz.append(fila)
    return matriz

def num_mayor(matriz):
    mayor = matriz [0][0]
    for i in matriz:
        for j in i:
            if j > mayor:
                mayor = j
    return mayor



def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es:")
    for i in Matriz:
        print(i)
    print(f"\nEl mayor elemento de la matriz es: {num_mayor(Matriz)}")
    
if __name__ == "__main__": 
    Main()
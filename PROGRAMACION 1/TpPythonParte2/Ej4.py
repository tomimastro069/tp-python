
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

def transpuestam(Matriz):
    transpuesta = [[Matriz[j][i] for j in range(len(Matriz))] for i in range(len(Matriz[0]))]
    print("la matriz transpuesta es: ")
    for i in transpuesta:
        print(i)
        

def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es:")
    for i in Matriz:
        print(i)
    transpuesta = transpuestam(Matriz)
    print (transpuesta)
if __name__ == "__main__": 
    Main()
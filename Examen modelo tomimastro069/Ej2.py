import random
def Crear_matriz(Filas, Columnas):
    matriz = [[0] * Columnas for _ in range(Filas)]
    for i in range(Filas):
        for j in range(Columnas):
            valor = int(input(f"ingrese el valor para la casilla | {i} {j} |  "))
            while valor > 999 or valor < 0:
                valor = int(input("Por favor ingrese un numero en el rango de 0 a 999: "))
            matriz[i][j] = valor
    return matriz

def Crear_matriz_aleatoria(Filas, Columnas):
    matriz = [[0] * Columnas for _ in range(Filas)]
    for i in range(Filas):
        for j in range(Columnas):
            valor = random.randint(0, 999)
            matriz[i][j] = valor
    return matriz
    
def consulta_de_valor( Filas, Columnas):
    valor = int(input("como quiere llenar la matriz?  \n | 1: valores Manuales \n | 2: valores Aleatorios \n"))
    match valor:
        case 1: 
            return Crear_matriz(Filas, Columnas)
        case 2:
            return Crear_matriz_aleatoria(Filas, Columnas)
        case _:
            print("Opción inválida, ingresa  1 o 2.")

def Main():
    Filas = int(input("ingrese la cantidad de filas: "))
    while Filas < 3:
        Filas = int(input("por favor ingrese un numero de filas mayor a 3: "))
    Columnas = int(input("ingrese la cantidad de columnas: "))
    while Columnas < 2:
        Columnas = int(input("por favor ingrese un numero de Columnas mayor a 2: "))
    Matriz = consulta_de_valor(Filas, Columnas)
    for i in Matriz:
        print(i)
    print("Las sumas de las filas de la matriz son: ")
if __name__ == "__main__":
    Main()
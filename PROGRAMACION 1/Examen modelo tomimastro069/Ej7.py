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

def sumar_filas(Matriz):
    sumar_fila = [0] * len(Matriz)

    for i in range(len(Matriz)):
        suma_valor_fila = 0
        for j in Matriz[i]:
            suma_valor_fila += j
        sumar_fila[i] = suma_valor_fila
    print("Las sumas de las filas de la matriz son: ")
    for i in range(len(sumar_fila)):
        print(f"Suma de la fila [{i}] = {sumar_fila[i]}")
    
    return sumar_fila

def mayor_menor_y_orden_original(sumadefilas):
    lista_tuplas = [(sumadefilas[i], i) for i in range(len(sumadefilas))]
    n = len(lista_tuplas)
    for i in range(n):
        for j in range(0, n-i-1): #forma de optimizacion del codigo, mientras itera va ordenando y no reordena lo q ya antes se ordenó
            if lista_tuplas[j][0] < lista_tuplas[j+1][0]: 
                lista_tuplas[j], lista_tuplas[j+1] = lista_tuplas[j+1], lista_tuplas[j]
    print("La Lista ordenada de mayor a menor con su orden original a la derecha es: ")
    for i in lista_tuplas:
        print(i)
    return lista_tuplas

def suma_de_todas_las_filas(sumar_filas):
    sumafinal = 0
    for i in range(len(sumar_filas)):
        sumafinal = sumafinal + sumar_filas[i]
    print(f"La suma final de todas las filas es: {sumafinal}")


    
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
    sumadefilas = sumar_filas(Matriz)
    mayor_menor = mayor_menor_y_orden_original(sumadefilas)
    sumafinal = suma_de_todas_las_filas(sumadefilas)
if __name__ == "__main__":
    Main()
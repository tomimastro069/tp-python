import random

def Suma_final(matrizsumada):
    sumafinal = sum(sum(fila) for fila in  matrizsumada)
    return sumafinal
    
def ingresar_valores(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1,100)
            fila.append(valor)
        matriz.append(fila)
    return matriz



def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    print("La matriz ingresada es:")
    print(Matriz)
    sumafinal = Suma_final(Matriz)
    print(f"La suma final de todos los elementos de la matriz es: {sumafinal}")
if __name__ == "__main__":
    Main()

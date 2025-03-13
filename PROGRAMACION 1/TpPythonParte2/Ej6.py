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

def MultiplicacionEscalar(Matriz, nro):
    Matrizmult = []
    for fila in Matriz:
        filaNueva = [elemento * nro for elemento in fila]
        Matrizmult.append(filaNueva)
    for i in Matrizmult:
        print(i)
    return Matrizmult


def Main():
    Filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    Columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
    Matriz = ingresar_valores(Filas, Columnas)
    nro = int(input("ingrese un numero: "))
    print("La matriz ingresada es:")
    for i in Matriz:
        print(i)
    print(f"La matriz multiplicada por {nro} es = ")
        
    Matriz = MultiplicacionEscalar(Matriz, nro)
   
if __name__ == "__main__": 
    Main()
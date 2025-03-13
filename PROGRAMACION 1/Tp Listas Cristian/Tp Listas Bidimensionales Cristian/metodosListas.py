import numpy
def numeroNatural(solicitud = ""):
    """
    Exige que el valor ingresado sea natural

    Args: 
        solicitud (String): Alguna solicitud en especifico
    
    Return:
        int: El numero natural ingresado
    """
    while True:
        try:
            natural = int(input(solicitud))
            if (natural > 0):
                break
        except ValueError:
            print("Valor incorrecto. Se espera un entero")
    return natural

def numeroEntero(solicitud = ""):
    """
    Exige que el valor ingresado sea entero

    Args: 
        solicitud (String): Alguna solicitud en especifico
    
    Return:
        int: El numero entero ingresado
    """
    while True:
        try:
            entero = int(input(solicitud))
            break
        except ValueError:
            print("Valor incorrecto. Se espera un entero")
    return entero

def llenarLista():
    """
    Devuelve una lista
   
    Return:
        list: La lista ingresada por el usuario
    """
    tamaño = numeroNatural("Ingrese el tamaño: ")
    lista = list()
    for i in range(0,tamaño):
        nro = numeroEntero(f"{i+1} Numero: ")
        lista.append(nro)
    return lista

def llenarMatriz():
    """
    Solicita al usuario que ingrese los elementos de una matriz

    Return :
        list: Una matriz con los elementos ingresados
    """
    matriz = list()
    tamaño = numeroNatural("Ingrese el tamaño de la matriz cuadrada: ")
    for i in range(0,tamaño):
        for j in range(0,tamaño):
            nro = numeroEntero(f"Numero [{i}][{j}]: ")
            matriz.append(nro)
    matriz = numpy.array(matriz)
    matriz = matriz.reshape(tamaño,tamaño)
    return matriz

def transpuesta(matriz):
    matrizTran = [ [0 for _ in matriz] for _ in matriz] #Crea una matriz 3x3. Cada elemento vale 0
    #El simbolo "_" despues del for, significa que no importa el valor en ese espacio.
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            matrizTran[i][j] = (matriz[j][i]) 
    return numpy.array(matrizTran)
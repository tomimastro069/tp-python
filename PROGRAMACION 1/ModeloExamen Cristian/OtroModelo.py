import random
"""
!1-Cargar una lista de números enteros de tamaño MxN y mostrar los datos cargados.
    El tamaño de la lista debe ser solicitado e ingresado por el usuario, indicando un valor entero para las filas (F) y un valor entero para las columnas (C).
    El valor mínimo válido será de 4x3 (4 filas y 3 columnas).
    Crear la lista y solicitar los valores numéricos para cada posición. 
    La carga de los datos puede ser manual (ingresados por el usuario) o automática (generados aleatoriamente), en el rango de 10 a 500.
    El programa debe preguntar cómo quiere hacer la carga de valores.

!2-Mostrar la lista resultante por pantalla en formato de lista (filas y columnas).

!3-Calcular el promedio de los valores en cada fila y generar una nueva lista con N filas por 1 columna, 
!donde cada celda contiene el promedio de la fila correspondiente de la lista original.

!4-Mostrar la lista de promedios por pantalla.

!5-Generar una nueva lista de tamaño N filas por 2 columnas, donde la primera columna contiene los promedios calculados en el punto 3, 
!pero ordenados de menor a mayor, y la segunda columna asigna el índice original de la fila de la lista del punto 3.

!6-Mostrar la nueva lista ordenada por pantalla.

!7Finalmente, calcular el promedio de los valores de la primera columna de la lista generada en el punto 5 y mostrar el resultado en pantalla.
"""
def main():
    F,C= (0,0)
    print("\t------Cargado de lista------")
    F,C = valorMinimoValido()
    print("\t------Punto 1------")
    lista = puntoUno(F,C)
    print("\t\n------Punto 2------")
    puntoDos(lista)
    print("\t\n------Punto 3------")
    listaPromedioFilas = puntoTres(lista,F,C)
    print("\t\n------Punto 4------")
    puntoCuatro(listaPromedioFilas)
    print("\t\n------Punto 5------")
    listaDosColumnas = puntoCinco(listaPromedioFilas,F)
    print("\t\n------Punto 6------")
    print(listaDosColumnas)
    print("\t\n------Punto 7------")
    punto7 = puntoSiete(listaDosColumnas)
    print(punto7)


#Funciones punto 1
def puntoUno(F,C):
    print("\nComo desea hacer la carga de datos")
    op = tipoCargaDeDatos()
    match (op):
        case 1: lista = cargaAutomatica(F,C)
        case 2: lista = cargaManual(F,C)
    return lista

def valorMinimoValido():
    while(True):
        F = validarNumeroEntero("Fila: ")
        C = validarNumeroEntero("Columna: ")
        if (F >= 4 and C>=3):
            return (F,C)

def tipoCargaDeDatos():
    print("1_Automatica\n2_Manual")
    while(True):
        opcion = validarNumeroEntero("Ingrese un numero entre 1 y 2: ")
        if(opcion in (1,2)):
            return opcion
        else:
            print("Error.")

def cargaAutomatica(F,C):
    return [[random.randint(10,500) for _ in range(C)] for _ in range(F)]

def cargaManual(F,C):
    lista = [ [0 for _ in range(C)] for _ in range(F)]
    print("\nRellenar Manualmente. Ingrese un numeros entre 10 - 500")
    for i in range(F):
        for j in range(C):
            while(True):
                num = validarNumeroEntero(f"Numero [{i}][{j}]: ")
                if (num >= 10 and num<=500):
                    lista[i][j] = num
                    break
                else:
                    print("Error. Fuera de rango")
    return lista    

def validarNumeroEntero(solicitud):
    while (True):
        try: 
            num = int(input(solicitud))
            return num
        except ValueError:
            print("Valor incorrecto. Numero entero esperado")

#Funciones punto dos
def puntoDos(lista):
    for i in range(len(lista)):
        filas = ""
        for j in range(len(lista[0])):
            filas += f"{str(lista[i][j])}  "
        print(filas)

#Funciones punto 3
def puntoTres(lista,F,C):
    listaPromedioFilas = []
    for i in range(F):
        suma = 0
        for j in range(C):
            suma += lista[i][j]
            promedio = suma / C
        listaPromedioFilas.append([promedio])
    return listaPromedioFilas

#Funciones punto 4
def puntoCuatro(lista):
    for i in range(len(lista)):
            print(f"{lista[i]} ")

#Funciones punto 5
def puntoCinco(listaPromedioFilas,F):
    listaDosColumnas = [[0 for _ in range(2)] for _ in range(F)]
    listaCopia = listaPromedioFilas.copy()
    listaPromedioOrdenada = ordenarMenorAMayor(listaCopia)
    for i in range(F):
        listaDosColumnas[i][0] = listaPromedioOrdenada[i][0]
        listaDosColumnas[i][1] = indiceOriginal(listaPromedioOrdenada[i][0],listaPromedioFilas)
    return listaDosColumnas

def indiceOriginal(valor, lista):
    for i, sublista in enumerate(lista):
        if sublista[0] == valor:
            return i
    return -1  # En caso de que no se encuentre el valor (esto no debería ocurrir si todo está correcto)

def ordenarMenorAMayor(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0,n - i - 1):
            if (lista[j] > lista[j+1]):
                lista[j] , lista[j+1] = lista[j+1] , lista[j]
    return lista

#Funciones punto 7
def puntoSiete(listaDosColumnas):
    suma = 0
    for i in range(len(listaDosColumnas)):
        suma += listaDosColumnas[i][0]      
    return f"Promedio de la lista dos culumnas: {suma / len(listaDosColumnas)} "

if __name__ == "__main__":
    main()
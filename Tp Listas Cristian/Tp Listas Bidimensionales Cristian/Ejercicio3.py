"""
Ejercicio 3: Suma de Cada Fila 
Modifica  el  programa  anterior  para  que  imprima  la  suma  de  cada  fila  de  la  lista 
bidimensional
"""

def sumaLista(lista):
    suma = 0
    for i in lista:
        for j in i:
            suma += j
    return suma

def sumaFilas(lista):
    sumasTotales = [0,0,0]
    cont = 0
    for i in lista:
        sumafila = 0
        for j in i:
            sumafila += j
        sumasTotales[cont] = sumafila
        cont+=1
    print(f"Suma de Fila 1: {sumasTotales[0]}")
    print(f"Suma de Fila 2: {sumasTotales[1]}")
    print(f"Suma de Fila 3: {sumasTotales[2]}")

def main():
    lista = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"Lista: \n{lista[0]}\n{lista[1]}\n{lista[2]}")
    #print(f"Suma de todos los elementos {sumaLista(lista)}") #Punto anterior
    sumaFilas(lista)

if __name__ == "__main__":
    main()
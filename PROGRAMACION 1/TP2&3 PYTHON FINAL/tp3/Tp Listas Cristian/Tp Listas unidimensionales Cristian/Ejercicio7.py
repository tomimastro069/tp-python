"""
Ejercicio 7: Promedio de una Lista 
Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
promedio de los elementos.
"""
from metodosListas import llenarLista

def promedio(lista):
    suma = 0
    for i in range(0,len(lista)):
        suma += lista[i]
    return suma / len(lista)

def main():
    lista = llenarLista()
    print(f"Promedio (aproximado) de la lista: {promedio(lista):3f}")

if __name__ == "__main__":
    main()
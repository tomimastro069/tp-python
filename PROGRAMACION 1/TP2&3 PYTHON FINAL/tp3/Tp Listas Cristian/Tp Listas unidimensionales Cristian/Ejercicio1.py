"""
Ejercicio 1: Suma de Elementos 
Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
suma de todos los elementos en la lista.
"""
from metodosListas import numeroEntero, numeroNatural

def suma(tamaño):
    lista_numeros = list()
    for i in range(0,tamaño):
        nro = numeroEntero(f"{i+1}_Numero: ")
        lista_numeros.append(nro)
    return sum(lista_numeros)
    

def main():
    tamaño = numeroNatural("Tamaño de la lista: ")
    print("Suma de los numeros: ",suma(tamaño))

if __name__ == "__main__":
    main()

"""
Ejercicio 2: Encontrar el Mayor y el Menor 
Escribe  un programa que  pida al usuario una lista de números y encuentre  el mayor y 
el menor de ellos. 
"""
from metodosListas import numeroNatural, numeroEntero

def llenarLista():
    tamaño = numeroNatural("Ingrese el tamaño: ")
    lista = list()
    for i in range(0,tamaño):
        nro = numeroEntero(f"{i+1} Numero: ")
        lista.append(nro)
    print("El minimo es: ",min(lista))
    print("El maximo es: ",max(lista))
    
llenarLista()

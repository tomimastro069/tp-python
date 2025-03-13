"""
Ejercicio 11: Contar Ocurrencias de un Elemento 
Escribe  un programa que  permita al usuario  ingresar una lista y un número, y cuente 
cuántas veces aparece ese número en la lista.
"""
from metodosListas import llenarLista,numeroEntero

def repeticionNumero(lista,nro):
    veces = 0
    for i in range(0,len(lista)):
        if nro == lista[i]:
            veces += 1
    return veces

def main():
    lista = llenarLista()
    nro = numeroEntero("Ingrese un numero para contar cuantas veces se repite en la lista: ")
    veces = repeticionNumero(lista,nro)
    print(f"El numero {nro} se repite {veces} veces")

if __name__ == "__main__":
    main()
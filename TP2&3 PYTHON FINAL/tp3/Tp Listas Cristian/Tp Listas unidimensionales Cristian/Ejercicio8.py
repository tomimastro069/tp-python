"""
Ejercicio 8: Encontrar Elementos Repetidos 
Escribe  un  programa  que  identifique  y  muestre  los  elementos  que  se  repiten  en  una 
lista. 

Pista: 
 Utiliza  un  diccionario  o  un  conjunto  (set)  para  hacer  el  seguimiento  de  los 
elementos.
"""

from metodosListas import llenarLista

def elementosRepetidos(lista):
    elementos = set()
    repetidos = set()

    for i in lista:
        if i in elementos: #Si el i esta en el set elementos, entonces esta repetido
            repetidos.add(i)
        else:
            elementos.add(i)
    return list(repetidos)

def main():
    lista = llenarLista()
    repetidos = elementosRepetidos(lista)
    print(f"\nLista: {lista}\nLista sin repeticiones: {set(lista)}\nElementos repetidos: {repetidos} ")

if __name__ == "__main__":
    main()
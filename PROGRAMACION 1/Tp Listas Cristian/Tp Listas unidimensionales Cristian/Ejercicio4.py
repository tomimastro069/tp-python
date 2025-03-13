"""
Ejercicio 4: Contar Elementos Pares e Impares 
Escribe  un  programa  que  pida  al  usuario  una  lista  de  números  y  cuente  cuántos  de 
ellos son pares y cuántos son impares.
"""
from metodosListas import llenarLista

def paresImpares(lista,pares=0,impares = 0):
    for i in lista:
        if i%2==0:
            pares+=1
        else:
            impares+=1
    print(f"Pares: {pares}\nImpares: {impares}")

def main():
    lista = llenarLista()
    paresImpares(lista)


if __name__ == "__main__":
    main()
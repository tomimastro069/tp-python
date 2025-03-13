"""
Ejercicio 9: Lista de Números Primos 
Escribe  un programa que  permita al usuario  ingresar una lista de  números y  filtre  los 
números primos. 
Pista: 
 Usa una función para verificar si un número es primo
"""
from metodosListas import llenarLista

def esPrimo(nro):
    count=0
    if(nro<0):
        return False
    else:
        for i in range(1,nro+1):
            if(nro %i==0):
                count+=1

    if(count>2):
        return False
    elif(count<=2 and count>=1):
        return True

def numerosPrimos(lista):
    primos = list()
    for i in range(0,len(lista)):
        if esPrimo(lista[i]):
            primos.append(lista[i])

def main():
    lista = llenarLista()
    print(f"Numeros primos: {numerosPrimos(lista)}")


if __name__ == "__main__":
    main()
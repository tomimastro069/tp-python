"""
Ejercicio 5: Multiplicar Elementos por un Valor 
Escribe  un programa  que  multiplique  cada  elemento  de  una  lista  de  números  por  un 
valor ingresado por el usuario
"""
from metodosListas import llenarLista

def listaPorNumero(lista):
    num = int(input("Ingrese un numero para multiplicar la lista: "))
    for i in range(0,len(lista)):
        lista[i] *= num
    return lista

def main():
    lista = llenarLista()
    print(listaPorNumero(lista))


if __name__ == "__main__":
    main()
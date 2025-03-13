"""
Ejercicio 3: Invertir una Lista 
Escribe un programa que permita al usuario ingresar una lista y la invierta
"""
from metodosListas import llenarLista

def invertirLista(lista):
    return lista[::1]


def main():
    lista = llenarLista()
    print("Metodo reverse")
    lista.reverse()
    print(lista)

    print("Metodo propio")
    listaInvertida = invertirLista(lista)
    print(listaInvertida)

if __name__ == "__main__":
    main()
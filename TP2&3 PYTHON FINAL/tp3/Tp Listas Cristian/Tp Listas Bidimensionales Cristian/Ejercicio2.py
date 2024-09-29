"""
Ejercicio 2: Suma de Todos los Elementos 
Escribe un programa que calcule la suma de todos los elementos en una lista 
bidimensional. Pista: Aplique la función sum
"""

def sumaLista(lista):
    suma = 0
    for i in lista:
        for j in i:
            suma += j
    return suma


def main():
    lista = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"Lista: {lista}")
    print(f"Suma de todos los elementos {sumaLista(lista)}")


if __name__ == "__main__":
    main()
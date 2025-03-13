"""
Ejercicio 12: Sumar Listas Elemento por Elemento 
Escribe  un  programa  que  sume  dos  listas  de  números  elemento  por  elemento.  Las 
listas deben tener la misma longitud
"""
from metodosListas import llenarLista,numeroEntero,numeroNatural

def llenarListaIgualTamaño(tamañoLista1,lista1):
    tamañoLista1 = numeroNatural("Ingrese el tamaño: ")
    while tamañoLista1 != len(lista1):
        tamañoLista1 = numeroNatural("Ingrese el tamaño: ")
    lista = list()
    for i in range(0,tamañoLista1):
        nro = numeroEntero(f"{i+1} Numero: ")
        lista.append(nro)
    return lista

def main():
    lista1 = llenarLista()
    lista2 = llenarListaIgualTamaño(len(lista1),lista1)
    lista3 = list(lista1 + lista2)
    #lista3 = lista1 + lista3
    print(f"Suma de listas: {lista3}")


if __name__ == "__main__":
    main()
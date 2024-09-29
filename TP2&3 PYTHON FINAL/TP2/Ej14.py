"""
En python no existe el pasaje Por Valor o Por refencia como tal. En python el pasaje de variables se realiza con objetos, es decir,
python pasa una refencia al objeto y todo dependera de si el objeto es inmutable o no.

Si el objeto es inmutable (int, float, str, etc), cualquier modificacion que se produzca creara una nueva instancia lo que es parecido a pasaje
por valor, en cambio las modificaciones en objetos mutables(listas, tuplas, diccionarios, etc) se realizan en el objeto original
"""

#? Ejemplo

def main():
    #Ejemplo de objeto inmutable
    x = 1
    sumarDiez(x) 
    print(x)

    #Ejemplo de objeto mutable
    lista = [1,2,3]
    sumarLista(lista) 
    print(lista)

def sumarDiez(x):
    x += 10

def sumarLista(lista):
    for i in range(len(lista)):
        lista[i] += 1 


if __name__ == "__main__":
    main()
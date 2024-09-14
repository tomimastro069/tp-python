"""
Ejercicio 10: Eliminar un Elemento por su Índice 
Escribe  un  programa  que  permita  al usuario  ingresar una  lista  de  números  y  eliminar 
un elemento en un índice especificado.
"""
from metodosListas import llenarLista

def indiceCorrecto(lista):
    while True:
        try:
            indice = int(input(f"Ingrese el indice desde 0 hasta {len(lista)-1}: "))
            if(indice >= 0 and indice <= (len(lista)-1) ):
                return indice
        except ValueError:
            print("Valor incorrecto. Ingrese un indice entero mayor a cero")
        

def main():
    lista = llenarLista()
    print("Borrar un elemento con el indice.")
    indice = indiceCorrecto(lista)    
    del lista[indice]
    print(f"Lista sin el elemento en el indice {indice}: {lista}")

if __name__ == "__main__":
    main()
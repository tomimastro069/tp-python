"""
Ejercicio 6: Eliminar Duplicados 
Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
elementos duplicados. 
Pista: 
 Utiliza la función set()
"""
from metodosListas import llenarLista

def main():
    lista = llenarLista()
    lista = set(lista)
    lista = list(lista)
    print(f"Elementos eliminados: \n{lista}")

if __name__ == "__main__":
    main()
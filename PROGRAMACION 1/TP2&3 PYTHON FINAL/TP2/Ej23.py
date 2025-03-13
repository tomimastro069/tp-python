import math
def main():
    cadena = input("Ingrese una cadena: ")
    recursion(cadena)

def recursion(cadena,i=-1): #Asigna un valor predeterminado a i.
    """Al trabajar con numeros negativos(para poder recorrer la cadena en reversa), 
calculo el valor absoluto del iterador y lo comparo con la cadena"""
    if (abs(i) == len(cadena)): #Caso base
        print(cadena[i])
        return
    else: #Caso recursivo
        print(cadena[i],end="")
        recursion(cadena,i-1)

if __name__ == "__main__":
    main()


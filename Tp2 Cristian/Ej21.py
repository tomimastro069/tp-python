def main():
    nro = valorPositivoEntero() #Revisa si el numero es positivo y entero
    resultado = recursion(nro)
    print(f"\nResultado {resultado}")


def recursion(nro):
    if (nro > 1):#Caso base
        print(nro," + ",end="") #Imprime los numeros que se van a sumar
        nro += recursion(nro - 1) #Caso recursivo
    else:
        print(nro,end="") #end = "" Imprime el numero sin salto de linea
        return 1
    return nro

def valorPositivoEntero():
    while True:
        try:
            nro = int(input("Ingrese un numero entero y mayor a cero: "))
            if (nro > 0):
                return nro
            else:
                print("Error. Numero negativo")
        except ValueError:
            print("Error. El programa necesita un numero entero")

if __name__ == "__main__":
    main()
def main():
    cadena = input("Ingrese una cadena: ")
    recursion(cadena)


def recursion(cadena,i = 0):
    if i == len(cadena): #Caso base
        return 
    else:   #Caso recursivo
        print(cadena[i])
        recursion(cadena,i+1)

if __name__ == "__main__":
    main()
from Ej21 import valorPositivoEntero    #Funcion del ejercicio anterior

def main():
    nro = valorPositivoEntero()
    nro = list(str(nro)) #Transforma los valores enteros en cadena y se guardan en una lista
    convertirAInt(nro)

    resultado = recursion(nro)
    print(f"\nResultado = {resultado}")

def convertirAInt(nro):
    i = 0
    while i < len(nro): #Transforma cada cadena de la lista en entero
        nro[i] = int(nro[i])
        i+=1

def recursion(nro,i=0):
    if i+1 == len(nro):#Caso base
        print(nro[i])
        return nro[i]
    else:   #Caso recursivo
        print(nro[i],"+ ",end="")
        return nro[i] + recursion(nro,i+1)


if __name__ == "__main__":
    main()
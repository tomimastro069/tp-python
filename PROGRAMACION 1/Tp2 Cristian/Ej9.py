def main():
    cadena = "La lluvia en Mendoza es escasa"
    asciiLista = ascii(cadena)
    print(" ".join(map(str, asciiLista))) #Convierte cada elemento de asciiLista en string y los imprime con espacios

def ascii(cad):
    asciiNumeros = list()   #Crea una lista vacia llamada asciiNumeros
    
    for i in cad:
        aux = ord(i)    #Obtiene el valor ASCII del carácter i y lo almacena en aux
        asciiNumeros.append(aux) #Agrega el valor ASCII al final de la lista
    return asciiNumeros

if __name__ == "__main__":
    main()
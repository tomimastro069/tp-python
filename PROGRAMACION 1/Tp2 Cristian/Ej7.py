def tamañoCadena(cadena):
    print(f"Tamaño de la frase: {cadena}")
    print(len(cadena))

def cantvocales(cadena):
    vocales = ("a","e","i","o","u")
    cantVocales = 0
    for caracter in cadena: #Itero sobre la cadena recibida en minuscula
        if caracter in vocales: #Revisa si el iterador (caracter) se encuentra en la tupla vocales
            cantVocales += 1    
    return cantVocales 

def main():
    cadena = input("Ingrese una cadena: ")
    tamañoCadena(cadena)
    #Le envio la cadena  en minusculas pero a el metodo cantVocales sin modificar la original. Para no hacer distincion entre Minuscula y Mayuscula
    cantVocales = cantvocales(cadena.lower())  
    print(f"Cantidad de vocales en \"{cadena}\" es: {cantVocales}")

if __name__ == "__main__":
    main()
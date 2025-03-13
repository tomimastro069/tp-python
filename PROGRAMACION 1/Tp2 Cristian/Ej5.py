def quitarEspacios(cadena):
    listaCadena = cadena.split()    #Divide la cadena en una lista de palabras y elimina los espacios en blanco
    return "".join(listaCadena)     #Une las cadenas de la lista en una sola sin espacios

def main():
    cadena = input("Ingrese una cadena: ")
    cadenaSinEspacio = quitarEspacios(cadena)
    print(cadenaSinEspacio)

if __name__ == "__main__":
    main()
def main():
    cadena = input("Ingrese una cadena: ")
    opcion = int(input("Desea convertirla en:\n1_Mayuscula\n2_Minuscula"))
    while opcion not in (1,2):  #Revisa si la opcion esta fuera de la tupla (1,2)
        opcion = int(input("Ingrese devuelta una opcion: "))
    mayusculas_minusculas(opcion,cadena)

def mayusculas_minusculas(n,cadena):
    resultado = cadena
    if n == 1:
        resultado = cadena.upper()  #Convierte la cadena entera a Mayuscula
    else:
        resultado = cadena.lower()  #Convierte la cadena entera a Minuscula
    print(resultado)

if __name__ == "__main__":
    main()
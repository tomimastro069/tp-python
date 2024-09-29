def recursiva(numero_str,cont,resultado):

    if cont == 0:
        
        print("la suma de los digitos de: ", numero_str, "es: " , resultado )

    else:
        digito = int(numero_str[cont-1])

        resultado += digito

        recursiva(numero_str, cont - 1, resultado)


numero= int(input("ingrese un numero de mas de un digito: "))

numero_str = str(numero)

cont = len(numero_str)

recursiva(numero_str, cont, 0)
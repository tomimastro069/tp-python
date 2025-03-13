cadena= input("ingresar una cadena")
A = input("Quiere transformar toda la cadena en MAYUSCULAS o minusculas? (M o m): ")
while True:
    A = input("Caracter invalido, ingrese (M o m)")

    if A == "M":
        cadena= cadena.upper()
        print(cadena)
        break
    elif A =="m":
        cadena = cadena.lower()
        print(cadena)
        break



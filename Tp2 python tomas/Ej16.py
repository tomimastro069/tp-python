def Cadena(cadena1):
    tieneletra = False
    for i in range(len(cadena1)):
        letra = cadena1[i]
        if "0" <= letra <= "9":
            tieneletra = True
            break
    if tieneletra:
        print(f"La cadena: {cadena1} tiene números")
    else:
        print(f"La cadena: {cadena1} NO tiene números")

cadena1 = input("Ingrese una cadena: ")
Cadena(cadena1)

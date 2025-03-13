A = 123456
cont = 0
while cont < 3:
    B = int(input("Ingrese la contraseña"))
    if B == A:
        print("Acceso correcto")
        cont = cont + 3
    else:
        print("Acceso denegado")
        cont = cont+1
        if cont == 3:
            print("Suficientes intentos")



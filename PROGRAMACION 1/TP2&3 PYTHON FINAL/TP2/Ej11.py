A = input("ingrese una palabra: ")
B = input("Ingrese otra palabra: ")
C = 0
while C != 1:
    if A==B:
        print("Las dos palabras son iguales")
    else:
        print("Las dos palabras son distintas")

    C= int(input("ingrese (1) para finalizar o (0) para continuar: "))
    if C == 1:
        break
    else:
         A = input("ingrese una palabra: ")
         B = input("Ingrese otra palabra: ")
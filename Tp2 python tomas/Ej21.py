def recursiva(A,resultado):
    if A == 0:
        print("el resultado de la suma de todos los numeros naturales es ", resultado)
    else:
        print(A,end=" | ")
        resultado = resultado + A
        A-= 1
        recursiva(A,resultado)
numero= int(input("ingrese un numero mayor a 0 "))
while numero <= 0:
    numero =int(input("ingrese un numero mayor a 0 "))
resultadofinal=recursiva(numero,0)
cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num
contpar = 0
contimp = 0
for i in range(len(Lista)):
    if Lista[i] % 2 == 0:
        contpar = contpar + 1
    else:
        contimp = contimp + 1
print("Hay: ",contpar ,"numeros pares y: ", contimp, "numeros impares")
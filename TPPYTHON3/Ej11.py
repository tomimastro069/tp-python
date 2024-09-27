cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista = [None] * cantidaddefilas
for i in range(len(Lista)):
    Num = int(input(f"Ingrese el número de la casilla {i}: "))
    Lista[i] = Num
num_iingresado= int(input("Ingrese un numero para verificar si esta repetido en la lista "))
cont = 0
for i in range(len(Lista)):
    if Lista[i] == num_iingresado:
        num_repetido = Lista[i]
        if num_iingresado == num_repetido:
            cont = cont + 1

if cont > 1:
    print("El numero ", num_iingresado, " se repite ", cont, " veces.")
elif cont == 1:
    print("El numero ingresado no se repite en la lista")
else:
    print("El numero ingresado no esta en la lista")
for i in range(len(Lista)):
    print(Lista[i],end= " | ")
        


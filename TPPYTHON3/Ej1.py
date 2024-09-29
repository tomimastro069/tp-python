cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num

sumadelista = 0
for i in range(len(Lista)):
    sumadelista = sumadelista + Lista[i]
    print(Lista[i],end= " | ")
print()
print("----------------------------------")
print("La suma de todos los valores es: ", sumadelista)
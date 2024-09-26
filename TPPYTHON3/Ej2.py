cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num
Mayor = Lista[0]
Menor = Lista[0]
for i in range(len(Lista)):
    if Lista[i] > Mayor:
        Mayor = Lista[i]
    if Lista[i] < Menor:
        Menor = Lista[i]
print("El numero mas grande de la lista es: ", Mayor)
print("El numero mas pequeño de la lista es: ", Menor)

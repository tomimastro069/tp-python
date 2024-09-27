cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
suma = 0
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num
    suma = suma + Lista[i]
promedio = suma / cantidaddefilas
print(f"El promedio de la Lista es: {promedio:.2f}")
cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num
Mult = float(input("Ingrese un numero por el cual se van a multiplicar todos los elementos de la lista: "))
Lista_multiplicada = [None] * cantidaddefilas
for i in range(len(Lista)):
    Lista_multiplicada[i] = Lista[i] * Mult

print("LISTA ORIGINAL: ")
for i in range(len(Lista)):
    print(Lista[i],end= " | ")
print()
print("----------------------------------")
print("LISTA MULTIPLICADA POR: ",  Mult)
for i in range(len(Lista_multiplicada)):
    print(Lista_multiplicada[i],end= " | ")

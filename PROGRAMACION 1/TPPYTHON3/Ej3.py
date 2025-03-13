cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista=[None] * cantidaddefilas
for i in range(len(Lista)):
    Num=int(input(f"ingrese el Numero de la casilla {i} "))
    Lista[i] = Num

Lista_invertida=[None] * cantidaddefilas

for i in range(len(Lista)):
    Lista_invertida[i]= str(Lista[len(Lista) - 1 - i])

print("LISTA ORIGINAL: ")
for i in range(len(Lista)):
    print(Lista[i],end= " | ")
print()
print("----------------------------------")
print("LISTA INVERTIDA: ")
for i in range(len(Lista_invertida)):
    print(Lista_invertida[i],end= " | ")
print()


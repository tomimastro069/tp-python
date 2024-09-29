cantidaddefilas = int(input("De cuantas filas quiere hacer la lista? "))
Lista = [None] * cantidaddefilas
for i in range(len(Lista)):
    Num = int(input(f"Ingrese el número de la casilla {i}: "))
    Lista[i] = Num

for i in range(len(Lista)):
    print(Lista[i],end= " | ")

elemento_eliminado = int(input(f"Elija un elemento para eliminar : "))
print("----------------------------------")
if elemento_eliminado in Lista:
    Lista.remove(elemento_eliminado)
    print(f"Elemento eliminado: {elemento_eliminado}")
else:
    print("Elemento no encontrado en la lista.")
    
for i in range(len(Lista)):
    print(Lista[i],end= " | ")
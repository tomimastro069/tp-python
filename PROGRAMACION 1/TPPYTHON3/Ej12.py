cantidaddefilas = int(input("De cuantas filas quiere hacer las lista? "))
Lista = [None] * cantidaddefilas

for i in range(len(Lista)):
    Num = int(input(f"Ingrese el número de la casilla {i}: "))
    Lista[i] = Num

print("----------------------------------")

Lista2 = [None] * cantidaddefilas

for i in range(len(Lista2)):
    Num2 = int(input(f"Ingrese el número de la casilla {i} de la lista 2: "))
    Lista2[i] = Num2

Lista_suma= [None] * cantidaddefilas

for i in range(cantidaddefilas):
    suma = 0
    suma = Lista[i] + Lista2[i]
    Lista_suma[i] = suma

print("Las listas sumadas elemento por elemento dan como resultado: ")
print("--------------------------------------------------------------")

for i in  range(len(Lista_suma)):
    print(Lista_suma[i],end= " | ")
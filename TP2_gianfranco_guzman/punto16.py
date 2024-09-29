"""16- Codifique un método que reciba como parámetro una cadena y determine si la
misma contiene o no números."""

cadena= input("Ingrese una oración: ")
tam= str(cadena)
cant_num= 0

for i in cadena:
    if i in "0123456789":
        cant_num += 1
        
print(f"La cadena {cadena}, tiene: {cant_num} numeros")

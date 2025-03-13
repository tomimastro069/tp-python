"""7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total. """

texto= input("Ingrese una oración: ")
tam= str(texto)
cant_vocales= 0
for i in texto:
    if i.lower() in "aeiou": # lower() convierte "i" a minuscula
        cant_vocales += 1
print(f"La cadena {texto}, tiene: {cant_vocales} vocales")

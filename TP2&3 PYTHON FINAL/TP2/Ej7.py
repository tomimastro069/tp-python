Cadena = input("Ingrese una cadena de texto")
B = Cadena.upper()
C = len(Cadena)
vocales= 0
for i in B:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vocales += 1
print(vocales)
"""5- Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre
la cadena resultante."""

texto= input("Ingrese una oración: ")

print(f"{texto} (original)")

nuevo_texto= texto.replace(" ","")

print(f"{nuevo_texto} (sin espacios)")
def cadenadentrodecadena(cadena1, cadena2):
    return cadena2 in cadena1

cadena1 = input("ingrese una cadena: ")
cadena2 = input("Ingrese otra cadena: ")

if cadenadentrodecadena(cadena1, cadena2):
    print(f"la segunda cadena: " , {cadena2} ," está en la primera")
else:
    print(f"la segunda cadena: " , {cadena2} ,"NO está en la primera")

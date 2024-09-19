"""10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario
pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el
resultado por pantalla. """

texto= input("Ingrese una cadena: ")

resp= int(input("Presione 1 para convertir a minuscula, 0 para convertir a mayuscula: "))

if  resp == 1:
    texto_mays= (texto.upper())
    print(f"{texto_mays}")
else:
    texto_mins= (texto.lower())
    print (f"{texto_mins}")
"""22- Suma los dígitos de un número ingresado por el usuario de forma recursiva.
Ejemplo: el usuario ingresa 1596
El programa debe sumar 1 + 5 + 9 + 6 """

cadena= str(input("Ingrese una numero entero de mas de 1 digito: "))

def sumar_digitos(cadena, suma=0 ,index= 0):
    if index >= len(cadena):
        return suma
    else:
        if cadena[index].isdigit():
            suma += int(cadena[index])
        return sumar_digitos(cadena, suma, index + 1)
        
resultado = sumar_digitos(cadena)
print(f"La suma de los digitos ingresados, {cadena} es: {resultado}")
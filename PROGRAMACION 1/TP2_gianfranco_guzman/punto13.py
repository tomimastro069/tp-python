"""13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se
encuentra dentro de la primera. """

cadena1= input("Ingrese la primer cadena: ")
cadena2= input("Ingrese la segunda cadena: ")

cadena1= cadena1.lower()
cadena2= cadena2.lower()

#find() devuelve el indice de la primera aparición de la subcadena en la cadena principal, sino devuelve -1
indice= cadena1.find(cadena2)
if indice != -1:
     print(f"La cadena 1: {cadena2}, se encuentran en la cadena: {cadena1}")
else:
    print(f"La cadena 1: {cadena2}, no se encuentran en la cadena: {cadena1}")

#index()este metodo arroja "ValueError"en vez de -1, se usa "try" con "except" ValueError
try:
    indice= cadena1.index(cadena2)
    print(f"La cadena 1: {cadena2}, se encuentran en la cadena: {cadena1}")
except ValueError:
    print(f"La cadena 1: {cadena2}, no se encuentran en la cadena: {cadena1}")

#Solo in
if cadena2 in cadena1:
    print(f"La cadena 1: {cadena2}, se encuentran en la cadena: {cadena1}")
else:
    print(f"La cadena 1: {cadena2}, no se encuentran en la cadena: {cadena1}")

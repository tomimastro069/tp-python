"""8- Reemplaza todas las vocales a de una cadena ingresada por teclado por una vocal e."""

texto= input("Ingrese una oración: ")
#para reemplazar mas de una subcadena se debe enlazar de la siguiente forma
texto_e = texto.replace("a", "e").replace("i", "e").replace("o", "e").replace("u", "e") 
   
print(f"La cadena {texto}, reemplazando vocales por e: {texto_e}")

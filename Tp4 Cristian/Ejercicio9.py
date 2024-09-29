"""
Ejercicio 9: Contar palabras en un texto 
Dado el siguiente texto: 
texto = "manzana naranja manzana pera pera pera naranja manzana" 
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
texto utilizando un diccionario. 
b) Imprime el diccionario resultante.
"""
texto = "manzana naranja manzana pera pera pera naranja manzana" 
print(f"{texto}")

tupla_texto = tuple(texto.split())
print(tupla_texto)

apariciones = {}

for palabra in tupla_texto:
    if palabra in apariciones:
        apariciones[palabra] += 1
    else:
        apariciones[palabra] = 1

print(f"Veces que aparecen las palabras en el texto\n{apariciones}")

texto = "manzana naranja manzana pera pera pera naranja manzana"

#a) Escribe un programa que cuente cuántas veces aparece cada palabra en el
#texto utilizando un diccionario.
palabras = texto.split()

conteo_frutas = {}

for i in palabras:
    if i in conteo_frutas:
        conteo_frutas[i] += 1
    else:
        conteo_frutas[i] = 1

#b) Imprime el diccionario resultante.
print(conteo_frutas) 
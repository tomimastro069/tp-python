texto = "manzana naranja manzana pera pera pera naranja manzana"

palabras = texto.split()

conteo_frutas = {}

for i in palabras:
    if i in conteo_frutas:
        conteo_frutas[i] += 1
    else:
        conteo_frutas[i] = 1

print(conteo_frutas) 
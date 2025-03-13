"""12- Dada la cadena “hipopotamo”, extraer la cuarta y quinta letra. """

cadena= "Hipopotamo"

def quitar_parte(cadena, inicio, fin):
    return cadena[:inicio] + cadena[fin:]

nueva_cadena= quitar_parte(cadena, 3,4) 
nueva_cadena= quitar_parte (nueva_cadena, 3,4) #la 5ta letra pasa a ser la 4ta

print(f"Cadena original: {cadena}")
print(f"Nueva cadena: {nueva_cadena}")

"""9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII.
Muéstralos en línea recta, separados por un espacio entre cada carácter. """

texto= "La lluvia en Mendoza es escasa"
print(f"{texto}")

for i in texto:
    codigo_ASCII = ord(i) # ord obtiene el codigo ASCII
    print(codigo_ASCII, end= " ") # end es para no saltar de linea
print( )
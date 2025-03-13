def leer_cadena_recursiva(cadena, cont=0):
    if cont == len(cadena): 
        return 
    else:
        print(cadena[cont]) 
        leer_cadena_recursiva(cadena, cont + 1) 

Cadena = input("ingrese una cadena de texto: ")
 
leer_cadena_recursiva(Cadena)
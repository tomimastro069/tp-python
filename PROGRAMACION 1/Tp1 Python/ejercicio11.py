#Escribe una aplicación con una variable que contenga una contraseña cualquiera.
#Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya
#no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”.
#Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden
#intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se
#ha bloqueado después de los 3 intentos”. Fin programa.

A = "asd123"
contador = 0
while contador < 3:
    B = (input("Ingrese la contraseña"))
    if B == A:
        print("Acceso Correcto")
        contador = contador + 3
    else:
        print("Acceso denegado")
        contador = contador+1
        if contador == 3:
            print("El acceso se ha bloqueado después de los 3 intentos")


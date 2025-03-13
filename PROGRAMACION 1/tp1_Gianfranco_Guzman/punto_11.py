#11) Escribe una aplicación con una variable que contenga una contraseña cualquiera.
#Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya
#no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”.
#Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden
#intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se
#ha bloqueado después de los 3 intentos”. Fin programa.       
i= 0
claveAzar= 1234

while True:
    clave=int(input("Ingrese la clave de usuario: "))
    i= i + 1
    if clave == claveAzar:
        print("Acceso Correcto")
        print("Intentos realizados:",i)
        break
    elif i==3:
       print("Intentos fallidos:",i)
       print("El acceso ha sido bloqueado")
       break
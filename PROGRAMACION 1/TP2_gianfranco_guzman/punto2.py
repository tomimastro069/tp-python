"""2- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique.""" 
#Cuando una variable esta por fuera de un rango establecido lo que ocurrira es que no ingresara a los procesos contiguos,
#provocando que no se puede continuar utilizando el numero ingresado, si el rango lo verificamos con un if, podriamos colocar
#toda la condición dentro de un bucle y al mismo colocarle un "brake" para el codigo siga pidiendo un numero hasta que este cumpla
#con las condiciones y poder seguir con el proceso.

#Ejemplo verificación con un if sin estar en un bucle: 

"""num= int(input("Ingrese un numero entre 10 y 100: "))
if 100 >= num >= 10:
     print(f"El numero ingresado esta en rango: {num}")
else:   
     print(f"El numero ingresado esta fuera de rango: {num}")"""

#Tras verificar que el número no cumple con los rangos minimos o maximos, se ingresa a la siguiente opción del if dando por terminado
#el proceso sin volver a ingresar un valor nuevamente.

#Ejemplo de if en un bucle:
while True:
    num= int(input(f"Ingrese un numero entre 10 y 100: "))
    if 100 > num > 10:  
         print(f"EXCELENTE el numero si esta en rango: {num}")
         break
    else: 
        print(f"Valor no valido, vuelva a intentarlo: ")


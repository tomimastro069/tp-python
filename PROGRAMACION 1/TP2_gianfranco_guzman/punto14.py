"""14- Indique si en Python existen o no variables de tipo valor y su contraparte tipo
referencia como sucede en otros lenguajes como Java. """

#En Python, todas las variables son referencias a objetos. Sin embargo, el comportamiento de las 
#variables puede variar dependiendo de si el objeto es mutable o inmutable. Los tipos inmutables se 
#comportan de manera similar a las variables de tipo valor en otros lenguajes, mientras que los tipos 
#mutables se comportan de manera similar a las variables de tipo referencia.

#Tipo inmutable
a= 10
b= a
b= 5 #Modificar b, no modifica a porque ya no apunta al mismo objeto (b=a)
print(f"a: {a}, b: {b}")

#Tipo mutable
lista1= [1, 2, 3]
lista2= lista1
lista2[0]= 0 #Al modificar la lista 2, tambien se modifica la lista 1, apunta al mismo objeto (lista1)
print(f"lista 1: {lista1}, lista 2: {lista2}")
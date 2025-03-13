num = int(input("Ingrese  un numero: "))
num_string = str(num)

#--------------------------------------------------

#comprobar si es divisible por dos
if (num % 2 == 0):
    print(f"El numero {num} es divisible por 2")

digitos = []

#--------------------------------------------------

#primero convierto cada caracter del string num en un numero y luego lo agrego a la lista digitos
for i in num_string:
    cifra = int(i)
    digitos.append(cifra)
    
#sumo todas las cifras en una sola  variable
sumaCifras = 0
for i in digitos:
    sumaCifras = sumaCifras + i
    
#verifico que la suma de las cifras sea divisible por 3
if (sumaCifras % 3 == 0):
    print(f"El numero {num} es divisible por 3")
    
#--------------------------------------------------

#veridifico que el ultimo digito del numero (el ultimo de la lista) sea un cinco o un cero
if (digitos[-1] == 0  or digitos[-1] == 5):
    print(f"El numero {num} es divisible por 5")

#--------------------------------------------------

#verifico que los criterios de divisibilidad del 2 y el 3 se cumplan para saber si es divisible por 6
if (num % 2 == 0 and sumaCifras % 3 == 0):
    print(f"El numero {num} es  divisible por 6")
    
#--------------------------------------------------

if (sumaCifras == 9 or sumaCifras % 9 == 0):
    print(f"El numero {num} es divisible por 9")
    
#--------------------------------------------------
#Verifico que el ultimo digito sea un cero
if (digitos[-1] == 0):
    print(f"El numero {num} es divisible por 10")

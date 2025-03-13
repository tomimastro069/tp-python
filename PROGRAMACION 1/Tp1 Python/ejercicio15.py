#Criterio de divisibilidad entre 2
def div_2 (num):
    if num % 2 == 0:
    
        return print("Es divisible entre 2")
    else:
        return print("NO es divisible entre 2")
#---------------------------------------
#Criterio de divisibilidad entre 3
def div_3 (num):
    suma = 0
    while num > 0:
        suma = suma + (num % 10)
        num = num // 10
    if suma % 3 == 0:
        return print("Es divisible entre 3")
    else:
        return print("NO es divisible entre 3")
#---------------------------------------
#Criterio de divisibilidad entre 5
def div_5 (num):
    ultimoDigito = num % 10
    if ultimoDigito == 5 or ultimoDigito == 0:
        return print("Es divisible entre 5")
    else:
        return print("NO es divisible entre 5")
#---------------------------------------
#Criterio de divisibilidad entre 6 
def div_6 (num):
    if num % 2 == 0 and num % 3 == 0:
        return print("Es divisible entre 6")
    else:
        return print("NO es divisible entre 6")
#---------------------------------------
#Criterio de divisibilidad entre 9
def div_9 (num):
    suma = 0 
    while num > 0:
        suma = suma + (num % 10)                                
        num = num // 10
    if suma == 9 or suma % 9 == 0:
        return print("Es divisible entre 9")
    else:
        return print("NO es divisible entre 9")
#---------------------------------------
#Criterio de divisibilidad entre 10
def div_10 (num):
    ultimoDigito = num % 10
    if ultimoDigito == 0:
        return print("Es divisible entre 10")
    else:
        return print("NO es divisible entre 10")
#------------------------------------------
#ALGORITMO PRINCIPAL
#------------------------------------------
num = int(input("Ingrese un número"))
div_2 (num)
div_3 (num)
div_5 (num)
div_6 (num)
div_9 (num)
div_10 (num)
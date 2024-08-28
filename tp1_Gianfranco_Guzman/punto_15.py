#Mis variables globales:
num= int(input("Ingrese un numero entero: "))

num_str= str(num) #str lo convierte a cadena
ultimo_digito= int(num_str[-1])
suma= 0
for caracter in num_str:
    suma += int(caracter)
#--------------------------------------------------------
#Criterio divisibilidad por 2:
def div_por_2(num):
    return num % 2 == 0

if div_por_2(num):
    print("El numero: ",num,"Es divisible por 2")
else:
    print("El numero: ",num,"No es divisible por 2")
#--------------------------------------------------------
#Criterio divisibilidad por 3:
def div_por_3(suma):
    return  suma % 3 == 0

if div_por_3(suma):
    print("El numero: ",num,"Es divisible por 3")
else:
    print("El numero: ",num,"No es divisible por 3")
#--------------------------------------------------------
#Criterio divisibilidad por 5:

ultimo_digito= int(num_str[-1])

def div_por_5(ultimo_digito):
    return ultimo_digito == 0 or ultimo_digito == 5

if div_por_5(ultimo_digito):
    print("El numero: ",num,"Es divisible por 5")
else:
    print("El numero: ",num,"No es divisible por 5")
#--------------------------------------------------------
#Criterio divisibilidad por 6:

def div_por_6(num):
    return div_por_2(num) and div_por_3(num)

if div_por_6(num):
    print("El numero: ",num,"Es divisible por 6")
else:
    print("El numero: ",num,"No es divisible por 6")
#--------------------------------------------------------
#Criterio divisibilidad por 9:
def div_por_9(suma):
    return suma % 9 == 0

if div_por_9(suma):
    print("El numero: ",num,"Es divisible por 9")
else:
    print("El numero: ",num,"No es divisible por 9")
#--------------------------------------------------------
#Criterio divisibilidad por 10:
ultimo_digito= int(num_str[-1])

def div_por_10(ultimo_digito):
    return ultimo_digito == 0

if div_por_10(ultimo_digito):
    print("El numero: ",num,"Es divisible por 10")
else:
    print("El numero: ",num,"No es divisible por 10")
#--------------------------------------------------------

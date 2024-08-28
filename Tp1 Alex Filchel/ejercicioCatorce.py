import random

num = random.randint(0,100)
cond = True
num2 = -10
i = 0

while (cond == True):
    while (num2 < 1 or num2 > 100):
        num2 = int(input("Ingrese un numero del 1 - 100: "))
    if (num2 > num):
        print("El numero ingresado es muy alto")
        i = i +1
        num2 = int(input("Ingrese un numero del 1 - 100: "))
    elif (num2 < num):
        print("El numero ingresado es muy bajo")
        i = i +1
        num2 = int(input("Ingrese un numero del 1 - 100: "))
    else:
        print(f"El numero ingresado es correcto, tardaste {i} intentos")
        print(f"El numero random era: {num}")
        cond = False
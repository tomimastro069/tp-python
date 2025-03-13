num1 = int(input("Ingrese un número"))
num2 = int(input("Ingrese un segundo número"))
if num1 == num2:
    print("Los valores ingresados son iguales")
else:
    if num1 > num2:
        print(num1, " es mayor a ", num2)
    else:
        print(num2, " es mayor a ", num1)
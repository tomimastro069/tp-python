"""21- Codifique un programa que solicite un número entero mayor a cero y que
mediante recursión sume todos los números números naturales desde el número
ingresado hasta 1.
Ejemplo: Ingreso 10
El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 + 1"""

def sumar_primeros_nums (num, suma):
    if num == 0:
        print(f"= {suma}")
        return suma
    else:
        print(num , end="")
        if num > 1:
            print(" + ", end="")
        suma += num
        return sumar_primeros_nums(num -1,suma)
    
num = int(input("Ingrese un número entero positivo: "))
suma = 0
resultado = sumar_primeros_nums(num, suma)
print(f"La suma de los primeros {num} números naturales es: {resultado}")

"""3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
14. Plantee el algoritmo planteando métodos para su resolución."""

while True:
    num= int(input(f"Ingrese un numero entero de 3 digitos: "))
    if 999 > num > 99:
        break
    else:
        print(f"Error!!")

i= 0
suma= 0
while i < 3:
    suma += num % 10
    num = int(num / 10)
    i += 1
print(f"La suma de los digitos del numero ingresado es: {suma}")
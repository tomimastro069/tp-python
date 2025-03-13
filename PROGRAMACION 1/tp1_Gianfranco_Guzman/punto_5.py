#5) Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es,
#también debemos indicarlo. 
num=int(input("Ingrese un numero"))

if (num % 2 == 0):
    print("El numero: ",num," es divisible por 2")
else: 
    print("El numero: ",num," NO es divisible por 2")
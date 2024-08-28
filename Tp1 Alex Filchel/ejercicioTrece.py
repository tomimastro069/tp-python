num = int(input("Ingrese un numero: "))
divisores = 0

for i in range(1,num + 1):
    if (num % i == 0):
        divisores = divisores + 1
        
if (divisores == 2):
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} NO es primo")
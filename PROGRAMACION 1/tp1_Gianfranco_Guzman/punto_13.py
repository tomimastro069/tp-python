#13) Pide un número por teclado e indica si es un número primo o no. Un número primo
#es aquel solo puede dividirse entre 1 y sí mismo. Por ejemplo: 25 no es primo, ya que
#25 es divisible entre 5, sin embargo, 17 si es primo. Un buen truco para calcular la raíz
#cuadrada del numero e ir comprobando que si es divisible desde ese número hasta 1.
#NOTA: Si se introduce un número menor o igual que 1, directamente es no primo. 
num= int(input("Ingrese un numero mayor que cero: "))
i= 1
div= 0
for i in range(1,num+1):
    if num % i == 0:
        div= div + 1

if div == 2:
    print(num,"Es un numero primo")
else: 
    print(num,"No es un numero primo")
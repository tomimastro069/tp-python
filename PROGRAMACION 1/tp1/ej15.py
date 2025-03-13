
B = int(input("Ingrese un número: "))
Digitos = str(B)
A = len(Digitos)
SumaDeDigitos = 0
for i in Digitos:
    SumaDeDigitos += int(i)
if B % 2 == 0:
    print(B, "es divisible por 2, porque es par")
    dos = True
else:
    dos = False

if SumaDeDigitos % 3 == 0:
    print(B, "es divisible por 3, porque la suma de sus dígitos es múltiplo de 3")
    tres = True
else:
    tres = False

if Digitos[-1] in '05':
    print(B, "es divisible por 5, porque termina en 0 o en 5")
    cinco = True
else:
    cinco = False

if dos and tres:
    print(B, "es divisible por 6, porque es divisible por 2 y por 3")

if SumaDeDigitos % 9 == 0:
    print(B, "es divisible por 9, porque la suma de sus dígitos es múltiplo de 9")

if Digitos[-1] == '0':
    print(B, "es divisible por 10, porque termina en 0")


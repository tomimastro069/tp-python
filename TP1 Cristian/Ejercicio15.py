nro = int(input("Ingrese un numero: "))
div2, div3 = False,False

print("El numero ", nro)
if(nro %2==0):
    print("Es divisible por dos")
    div2 = True

cadena = str(nro)
suma = 0
for i in cadena:
    suma += int(i)
if (suma%3==0):
    print("Es divisible por tres")
    div3 = True

if (nro %10 == 0 or nro %10 == 5):
    print("Es divisible por cinco")

if(div2 and div3):
    print("Es divisible por seis")

if (suma == 9 or suma % 9==0):
    print("Es divisible por nueve")

if (cadena[-1] == '0'):
    print("Es divisible por diez")
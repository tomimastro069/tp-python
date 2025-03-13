nro = int(input("Ingrese un numero: "))
count=0


if(nro<0):
    print("No es primo")
else:
    for i in range(1,nro+1):
        if(nro %i==0):
            count+=1

if(count>2):
    print("El numero no es primo")
elif(count<=2 and count>=1):
    print("El numero es primo")
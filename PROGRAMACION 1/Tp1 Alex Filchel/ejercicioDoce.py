dia = int(input("Ingrese un dia de la semana (1-7): "))

while (dia <= 0 or dia > 7):
    dia = int(input("Ingrese un dia de la semana (1-7): "))
    
if (dia == 6 or dia == 7):
    print("El dia no es laboral")
else:
    print("El dia es laboral")
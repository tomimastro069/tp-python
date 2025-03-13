#12) Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
#nuevamente. 

while True:
    dia=int(input("Ingrese un dia de la semana: "))
    if dia > 0 and dia < 6:
        print("Es un dia LABORABLE")
        break
    elif dia < 8:
        print("Es un dia NO LABORABLE")
        break
    else:
        dia=int(input("Valor no válido, vuelva a intentar: "))
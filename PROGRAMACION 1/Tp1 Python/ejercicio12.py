""" Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
nuevamente. Debe investigar cuales son las alternativas que se pueden codificar para
reemplazar o emular una estructura switch por ejemplo implementando diccionarios.
Dado que Python no posee esta estructura por defecto."""
#---------------------------------------------------
#Pido al usuario que ingrese el día de la semana
DiaIngresado = int(input("Ingrese el día de la semana en números 1-7"))
#---------------------------------------------------
#Condición para que el día ingresado esté entre 1-7
while (DiaIngresado < 1) or (DiaIngresado > 7):
    DiaIngresado = int(input("Ingrese el día de la semana en números 1-7"))
#---------------------------------------------------
#Asigno a cada "día" su valor (laboral o no laboral)
mi_diccionario = {
    1: "Día Laboral", #Lunes
    2: "Día Laboral", #Martes
    3: "Día Laboral", #Miercoles
    4: "Día Laboral", #Jueves
    5: "Día Laboral", #Viernes
    6: "Día NO Laboral", #Sabado
    7: "Día NO Laboral" #Domingo
}
#---------------------------------------------------
#Imprimo el resultado de acuerdo al día ingresado
print(mi_diccionario[DiaIngresado])
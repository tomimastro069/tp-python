
dias = int((input("Ingrese un numero 1-7:")))
while (dias<1 or dias>7):
    dias = int((input("Ingrese un numero 1-7:")))




if (dias == 1 or dias == 2 or dias == 3 or dias == 4 or dias == 5):
    diaLaboral= True
else:
    diaLaboral = False
"""
while (cont<7):
    if(dias ==6 or dias ==7):
        diaLaboral= False
    cont+=1
"""


print("El dia ",dias ,"\nEs laboral?",diaLaboral)
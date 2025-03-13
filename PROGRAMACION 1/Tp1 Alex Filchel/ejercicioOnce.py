contra = "Hola"
i = 0
cond = True

while(i < 3 and cond == True):
    contra2 = input("Ingrese una contrasena: ")
    if(contra == contra2):
        print("Contrasena correcta!!!!!!!")
        cond = False
    i = i + 1
#10) Lee un número por teclado y comprueba que este número es mayor o igual que
#cero, si no lo es lo volverá a pedir (do while), después muestra ese número por
#consola
while True:  #Al colocar true se ingresa siempre al while
    num= int(input("Ingrese un numero mayor o igual a cero: "))
    if num > 0: #verifico si el numero es mayor o igual a cero
        print("El numero: ",num,"> 0")
        break #si no se cumple la condición se frena el codigo
    elif num == 0:
         print("El numero: ",num,"= 0")
         print("Finalizando ...")
         break #si no se cumple la petición se frena el codigo
    else:
        print("El numero: ",num,"< 0") # si el numero es mayor o cero se implime
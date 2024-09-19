"""23- Crea un programa donde se pida el ingreso de una cadena y por medio de
recursión mostrar la cadena de forma inversa.
Ejemplo: Ingreso “computadora de escritorio”
Invertir cadena “oirotircse ed arodatupmoc”"""

cadena= str(input("Ingrese una cadena para invertirla: "))

def str_inverso(cadena, i = -1):
   if (abs(i) == len(cadena)):
      print(cadena[i])
   else:
         print(cadena[i], end="")
         str_inverso(cadena, i - 1)
        
resultado = str_inverso(cadena)



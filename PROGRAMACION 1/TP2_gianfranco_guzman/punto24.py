"""Crea un programa que lea una cadena de texto carácter por carácter usando recursión. """

cadena= str(input("Ingrese una cadena para invertirla: "))

def leer_str_DxD(cadena, index= 0):
   if index >= len(cadena):
      return ""
   else:
         print(cadena[index])
         return leer_str_DxD(cadena, index + 1)
        
resultado = leer_str_DxD(cadena)
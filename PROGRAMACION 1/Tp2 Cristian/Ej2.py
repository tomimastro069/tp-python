"""
Si se  asigna un valor a una variable  fuera de  rango  (mayor de  lo  establecido) ¿Qué 
ocurre? ¿Existe alguna forma de resolverlo? 
Ejemplifique.
"""
Numero = 2**63 + 8
Vlong=int(Numero)
if Vlong < -2*63 or Vlong > (2*63)-1  :
     print("Valor fuera del rango de 'long' 64 bits")
     if Numero > 0:
        print(((2*63)-1), " + " , Numero - 2*63)
     elif Numero <= 0:
         print(-2*63, " + ", Numero + ((2*63) - 1))
    
else:
    print("Valor long: ",Vlong)
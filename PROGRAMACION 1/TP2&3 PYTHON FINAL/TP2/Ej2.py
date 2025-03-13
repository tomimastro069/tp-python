"""
por lo menos en python no hay un limite de una variable fuera de rango, ya que short y long no existen
tienen q ser simulados, y el limite de long es tan grande (-2^63/2^63-1) q directamente fue incluido en el float.
En el caso de que sea simulado y el limite sea alcanzado mi unica idea es mostrar el ultimo numero posible sumando
el numero q sobre, y advertir q ese limite se a sobrepasado.

"""
Numero = -32769
Vshort=int(Numero)
if Vshort < -32768 or Vshort > 32767:
     print("Valor fuera del rango de 'short' 16 bits")
     if Numero > 0:
        print(32767, " + " , Numero - 32767)
     elif Numero <= 0:
         print(-32768, " + ", Numero + 32768)
    
else:
    print("Valor short: ",Vshort)
Numero = 2**63 + 8
Vlong=int(Numero)
if Vlong < -2**63 or Vlong > (2**63)-1  :
     print("Valor fuera del rango de 'long' 64 bits")
     if Numero > 0:
        print(((2**63)-1), " + " , Numero - 2**63)
     elif Numero <= 0:
         print(-2**63, " + ", Numero + ((2**63) - 1))
    
else:
    print("Valor long: ",Vlong)
"""
def none():
    x = None 
    print(x) 

Al ejecutar este codigo el programa muestra por pantalla "None".
La palabra None es el equivalente a null en Java. Significa que no existe
valor en la variable que contiene None o que la variable esta vacia.
No es lo mismo que valores como "0" o "" ya que son valores validos y 
distintos a None.
"""


#Ejemplo con una funcion que no devuelve nada

def main():
    variableImprimir = sinRetorno()
    print(variableImprimir)

def sinRetorno():
    print("")

if __name__ == "__main__":
    main()
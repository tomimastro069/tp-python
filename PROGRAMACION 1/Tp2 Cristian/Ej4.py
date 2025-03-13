def nroBilletes(dinero):
    billetes = [200,100,50,20,10,5,2,1,0.50,0.25,0.10,0.05] #Lista para seleccionar las denominaciones
    cantBilletes = dict.fromkeys(billetes,0) #Crea un diccionario donde cada denominacion en billetes es una clave y cada clave tiene un valor de 0                         


    # Iteramos sobre las claves del diccionario
    for billete in billetes:
        if dinero >= billete:
            cantBilletes[billete] = int(dinero // billete) #Accedo al valor de la clave en cantBilletes 
            dinero = round(dinero % billete, 2) #Actualiza el valor de dinero. Deja el resto de dividir por billete y lo redondea a dos decimales
    return cantBilletes

#Muestra los billetes en orden con cantidad y denominacion
def mostrarBilletes(denominacion):
    for i in denominacion:
        valor = denominacion[i]     #Asigna a la variable "valor" el valor de clave numero i(o en la posicion i)
        if (valor != 0):
            print(f"{valor} billete de {i}", end=", ")  #Imprime la cantidad y denominacion

#metodo Main
def main():
    dinero = float(input("Ingrese una cantidad de dinero: "))
    billetes = nroBilletes(dinero)
    mostrarBilletes(billetes)
    


#if para que main se ejecute primero
if __name__ == "__main__":
    main()
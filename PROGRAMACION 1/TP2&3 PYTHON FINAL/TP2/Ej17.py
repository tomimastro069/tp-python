import Ej17e    #Fichero python que contiene diccionarios con los dias y meses
from num2words import num2words #Libreria que transforma un numero a palabras

class FuncionesPrograma:       
    @staticmethod
    def getFechaString(dia,mes,año):
        #Le da valor a cada dia, mes y año. Si son incorrectos se le asigna False
        dia = FuncionesPrograma.validarDia(dia,mes)
        mes = FuncionesPrograma.validarMes(mes)
        año = FuncionesPrograma.validarAño(año)
        
        if (dia & mes & año)!= False: #Revisa si el año,mes,dia son correctos 
            FuncionesPrograma.mostrarFecha(dia,mes,año)
        else:
            print("Fecha invalida")


    def mostrarFecha(dia,mes,año):
        #Separa cada dia,mes,año representados en enteros por su equivalente en palabras
        StringDia = Ej17e.dias[dia] 
        StringMes = Ej17e.meses[mes]
        StringAño = FuncionesPrograma.miles(año)
        print(f"{StringDia} de {StringMes} de {StringAño}")

    def miles(año):
        año_en_palabras = num2words(año,lang='es')
        return año_en_palabras


    #Metodos para validar si los dias, meses y años son correctos
    
    def validarDia(dia,mes):
        match mes:
            case 2:
                if (dia>= 1 and dia<=29):
                    return dia
            case 4 | 6 | 9 | 11:
                if(0 <= dia <= 30):
                    return dia
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if (0 <= dia <= 31):
                    return dia
            case _:
                return False
            
    def validarMes(mes):
        if(mes>=1 and mes<=12):
            return mes
        else:
            return False
    
    def validarAño(año):
        if (año>=0):
            return año
        else:
            return False
    



def main():
    fechaRecibida = input("Ingrese una fecha con este formato 00/00/0000: ")
    listaDiaMesAño = fechaRecibida.split("/") #Creo una lista con cada numero de la cadena separado por "/"
    #Convierto cada posicion de la lista a entero y se lo asigno a dia,mes,año
    dia = int(listaDiaMesAño[0])    
    mes = int(listaDiaMesAño[1])
    año = int(listaDiaMesAño[2])
    FuncionesPrograma.getFechaString(dia, mes, año)



if __name__ == "__main__":
    main()
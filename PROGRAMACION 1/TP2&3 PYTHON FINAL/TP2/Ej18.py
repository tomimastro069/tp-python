import Ej17e
from num2words import num2words

class FuncionesPrograma:       
    @staticmethod
    def getFechaString(fechaRecibida):
        listaDiaMesAño = fechaRecibida.split("/")
        dia = int(listaDiaMesAño[0])
        mes = int(listaDiaMesAño[1])
        año = int(listaDiaMesAño[2])
        if (FuncionesPrograma.validarDia(dia,mes) & FuncionesPrograma.validarMes(mes) & FuncionesPrograma.validarAño(año))!= False:
            FuncionesPrograma.mostrarFecha(dia,mes,año)
        else:
            print("Fecha invalida")

    @staticmethod
    def getFechaDate(dia,mes,año):
        if (FuncionesPrograma.validarDia(dia, mes) and FuncionesPrograma.validarMes(mes) and FuncionesPrograma.validarAño(año))!= False:
            FuncionesPrograma.mostrarFecha(dia,mes,año)
        else:
            print("Fecha invalida")

    def mostrarFecha(dia,mes,año):
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
        return 1 <= mes <= 12
    
    def validarAño(año):
        return año >= 0
    



def main():
    fechaRecibida = input("Ingrese una fecha con este formato 00/00/0000: ")
    
    FuncionesPrograma.getFechaString(fechaRecibida)

    print("----------------\n\tCambio de formato")
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    FuncionesPrograma.getFechaDate(dia,mes,año)

if __name__ == "__main__":
    main()
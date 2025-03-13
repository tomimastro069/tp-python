class FuncionesPrograma:
    @staticmethod
    def getFechaString(fecha):
        # Diccionarios para convertir números a palabras
        dias = {
            '01': 'Uno', '02': 'Dos', '03': 'Tres', '04': 'Cuatro', '05': 'Cinco',
            '06': 'Seis', '07': 'Siete', '08': 'Ocho', '09': 'Nueve', '10': 'Diez',
            '11': 'Once', '12': 'Doce', '13': 'Trece', '14': 'Catorce', '15': 'Quince',
            '16': 'Dieciséis', '17': 'Diecisiete', '18': 'Dieciocho', '19': 'Diecinueve',
            '20': 'Veinte', '21': 'Veintiuno', '22': 'Veintidós', '23': 'Veintitrés',
            '24': 'Veinticuatro', '25': 'Veinticinco', '26': 'Veintiséis', '27': 'Veintisiete',
            '28': 'Veintiocho', '29': 'Veintinueve', '30': 'Treinta', '31': 'Treinta y uno'
        }

        meses = {
            '01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04': 'Abril', '05': 'Mayo',
            '06': 'Junio', '07': 'Julio', '08': 'Agosto', '09': 'Septiembre', '10': 'Octubre',
            '11': 'Noviembre', '12': 'Diciembre'
        }

        unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
        decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
        centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

        def numero_a_palabras(numero):
            if numero == 1000:
                return 'mil'
            elif numero > 1000:
                return 'mil ' + numero_a_palabras(numero - 1000)
            elif numero > 100:
                return centenas[numero // 100] + ' ' + numero_a_palabras(numero % 100)
            elif numero > 10:
                return decenas[numero // 10] + ' ' + numero_a_palabras(numero % 10)
            else:
                return unidades[numero]

        # Separar la fecha en día, mes y año
        dia, mes, año = fecha.split('/')

        # Convertir el día, mes y año a palabras
        dia_palabra = dias[dia]
        mes_palabra = meses[mes]
        año_palabra = numero_a_palabras(int(año))

        # Formatear la salida
        return f"{dia_palabra} de {mes_palabra} de {año_palabra}".capitalize()

# Ejemplo de uso
fecha = "30/10/1900"
print(FuncionesPrograma.getFechaString(fecha))

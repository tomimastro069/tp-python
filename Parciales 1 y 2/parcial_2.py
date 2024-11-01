
lista_articulos = [
    [101, "Leche", 250],
    [102, "Gaseosa", 300],
    [103, "Fideos", 150],
    [104, "Arroz", 280],
    [105, "Vino", 1200],
    [106, "Manteca", 200],
    [107, "Lavandina", 180],
    [108, "Detergente", 460],
    [109, "Jabón en Polvo", 960],
    [110, "Galletas", 600]
]


clientes = {
    "20110425417": "Rodolfo Fernandez",
    "30527419655": "Los Pollos Hnos",
    "27289425478": "Andrea Pereira",
    "33536549878": "Multimarca Repuestos",
    "20291122568": "Luis Peric"
}


def crear_factura():

    return {
        "fecha": "",
        "numero": 0,
        "letra": "",
        "total": 0.0,
        "monto_iva": 0.0,
        "cliente": "",
        "detalles": [[0]*5 for _ in range(100)], 
        "cantidad_articulos": 0
    }

def solicitar_datos_factura(factura):


    factura["fecha"] = input("Ingrese la fecha de la factura: ")
    factura["numero"] = int(input("Ingrese el número de la factura: "))

def solicitar_cuit(factura):


    while True:
        cuit = input("Ingrese el CUIT del cliente: ")
        if len(cuit) == 11 and (cuit[:2] in ["20", "27", "30", "33"] and (cuit in clientes)):
            print(f"Bienvenido {clientes[cuit]}")
            factura["cliente"] = clientes.get(cuit, "Consumidor Final")
            return cuit
        else:
            print("CUIT inválido. Debe comenzar con 20, 27, 30 o 33 y tener 11 caracteres.")

def solicitar_articulos(factura):


    while True:
        codigo = input("Ingrese el código del artículo (o 0000 para finalizar): ")
        if codigo == "0000":
            break
        encontrado = False
        for articulo in lista_articulos:
            if int(codigo) == articulo[0]:
                encontrado = True
                cantidad = int(input(f"Ingrese la cantidad de {articulo[1]}: "))
                subtotal = articulo[2] * cantidad
                factura["detalles"][factura["cantidad_articulos"]] = [articulo[0], articulo[1], cantidad, articulo[2], subtotal]
                factura["cantidad_articulos"] += 1
                break
        if not encontrado:
            print("Código incorrecto. Intente nuevamente.")

def calcular_total(factura):


    total = 0
    for i in range(factura["cantidad_articulos"]):
        total += factura["detalles"][i][4]
    return total

def calcular_iva(cuit, total):


    if cuit[:2] in ["20", "27"] or total == "Consumidor Final":
        return 0
    else:
        return total * 0.21

def asignar_letra_factura(cuit):


    if cuit[:2] in ["20", "27"] or cuit == "Consumidor Final":
        return "B"
    else:
        return "A"

def calcular_total_factura(factura, total, monto_iva):


    if factura["letra"] == "B":
        factura["total"] = total + monto_iva
    else:
        factura["total"] = total

def imprimir_factura(factura):

    print(f"\nFecha: {factura['fecha']}")

    print(f"Número: {factura['numero']}")

    print(f"Letra: {factura['letra']}")

    print(f"Cliente: {factura['cliente']}")

    print(f"\nCódigo Artículo   Nombre Artículo   Cantidad   Precio Unitario   Subtotal")

    for i in range(factura["cantidad_articulos"]):

        detalle = factura["detalles"][i]
        print(f"{detalle[0]:<16} {detalle[1]:<16} {detalle[2]:<10} {detalle[3]:<17} {detalle[4]}")

    print(f"\nIVA: {factura['monto_iva']}")
    
    print(f"Total: {factura['total']}")

def main():

    factura = crear_factura()
    solicitar_datos_factura(factura)
    cuit = solicitar_cuit(factura)
    solicitar_articulos(factura)
    total = calcular_total(factura)
    monto_iva = calcular_iva(cuit, total)
    letra = asignar_letra_factura(cuit)
    factura["monto_iva"] = monto_iva
    factura["letra"] = letra
    calcular_total_factura(factura, total, monto_iva)
    imprimir_factura(factura)


if __name__ == "__main__":
    main()

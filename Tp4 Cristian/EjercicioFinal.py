def main():
    inventario = {
        "A001": ("PlayStation 5 Pro", 1500),
         "A002": ("Mouse", 25),
         "A003": ("Teclado", 45),     
         "A004": ("Procesador I9", 300),     
         "A005": ("Monitor", 120)}
    mostrar_inventario(inventario)

    codigo = input("\t-----\nBuscar un producto por su codigo\nIngrese el codigo: ")
    buscar_producto(inventario,codigo)
    
    codigo = input("\t-----\nModificar un producto con codigo y nuevo precio\nIngrese el codigo: ")
    nuevo_precio = int(input("Ingrese el nuevo precio: "))
    modificar_precio(inventario, codigo, nuevo_precio)
    
    codigo = input("\t-----\nEliminar un producto con codigo y nuevo precio\nIngrese el codigo: ")
    eliminar_producto(inventario, codigo)

    min_precio = float(input("\t-----\nProductos dentro del rango de precio\nPrecio minimo: "))
    max_precio = float(input("Precio maximo: "))
    productos_por_rango_de_precio(inventario,min_precio,max_precio)

#Metodos del ejercicio final

def mostrar_inventario(inventario):
    print(f"\tInventario\n\t{inventario}")

def buscar_producto(inventario,codigo):
    print(f"Producto de inventario: {inventario[codigo]}" if codigo in inventario else "No existe el codigo en el inventario")

def modificar_precio(inventario, codigo, nuevo_precio):
    nombre,precio_Actual = inventario[codigo]
    try:
        inventario[codigo] = (nombre,nuevo_precio)
        print(f"Nuevo precio: {inventario[codigo]}")
        inventario = tuple(inventario)
    except KeyError:
        print("No se existe el codigo en el inventario")
        inventario = tuple(inventario)
        
def eliminar_producto(inventario, codigo):
    try:
        inventario.pop(codigo)
    except KeyError:
        print("Error. No existe ese codigo")
    print(f"Elemento eliminado: {inventario}")

def productos_por_rango_de_precio(inventario,min_precio,max_precio):
    for codigo in inventario:
        if max_precio > inventario[codigo][1] > min_precio :
            print(inventario[codigo])


if __name__ == "__main__":
    main() 
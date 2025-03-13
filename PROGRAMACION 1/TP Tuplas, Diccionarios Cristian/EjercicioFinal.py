def main():
    inventario = {
        "01": ("PlayStation 5 Pro", 1500),
         "02": ("Mouse", 25),
         "03": ("Teclado", 45),     
         "04": ("Procesador I9", 300),     
         "05": ("Monitor", 120)}
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
    if codigo in inventario:
        print(f"Producto: {inventario[codigo]}")
    else:
        print("El codigo no esta en el inventario")

def modificar_precio(inventario, codigo, nuevo_precio):
    producto = inventario.get(codigo)
    if producto:
        # Actualizar el precio
        inventario[codigo] = (producto[0], nuevo_precio)
        print(f"El precio del producto con código {codigo} ha sido actualizado a ${nuevo_precio}")
    else:
        print(f"El código {codigo} no existe en el inventario")
        
def eliminar_producto(inventario, codigo):
    if codigo in inventario:
        inventario.pop(codigo)
        print(f"El producto con codigo {codigo} fue eliminado")
    else:
        print(f"El codigo {codigo} no existe")

def productos_por_rango_de_precio(inventario,min_precio,max_precio):
    print(f"Productos en el rango de precio entre {min_precio} y  {max_precio}")
    for clave,valor in inventario.items():
        if min_precio < valor[1] < max_precio:
            print(f"Codigo: {clave}, Descripcion: {valor}")


if __name__ == "__main__":
    main() 
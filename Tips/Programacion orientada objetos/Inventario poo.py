class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}€, Stock: {self.cantidad}"
    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad
        return f"Stock actualizado: {self.cantidad} unidades."
    def vender_producto(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return f"Venta realizada. Quedan {self.cantidad} unidades."
        else:
            return "No hay suficiente stock para realizar la venta."
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, nombre, precio, cantidad):
        if nombre in self.productos:
            return f"El producto {nombre} ya está en el inventario."
        self.productos[nombre] = Producto(nombre, precio, cantidad)
        return f"Producto {nombre} agregado al inventario."
    def mostrar_inventario(self):
        if not self.productos:
            return "El inventario está vacío."
        inventario_str = "\n".join([producto.mostrar_info() for producto in self.productos.values()])
        return inventario_str
    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            return self.productos[nombre].actualizar_stock(cantidad)
        return "Producto no encontrado en el inventario."
    def vender_producto(self, nombre, cantidad):
        if nombre in self.productos:
            return self.productos[nombre].vender_producto(cantidad)
        return "Producto no encontrado en el inventario."
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Actualizar stock de producto")
    print("4. Vender producto")
    print("5. Salir")
    return input("Selecciona una opción: ")
def main():
    inventario = Inventario()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto (€): "))
            cantidad = int(input("Cantidad en stock: "))
            print(inventario.agregar_producto(nombre, precio, cantidad))
        elif opcion == '2':
            print("\nInventario actual:")
            print(inventario.mostrar_inventario())
        elif opcion == '3':
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Cantidad a añadir o restar (negativa para restar): "))
            print(inventario.actualizar_producto(nombre, cantidad))
        elif opcion == '4':
            nombre = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            print(inventario.vender_producto(nombre, cantidad))
        elif opcion == '5':
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
if __name__ == "__main__":
    main()

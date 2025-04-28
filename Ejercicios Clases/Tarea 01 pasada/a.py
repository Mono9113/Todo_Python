class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

class Carrito:
    def __init__(self):
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.items:
            self.items[producto.nombre]['cantidad'] += cantidad
        else:
            self.items[producto.nombre] = {'producto': producto, 'cantidad': cantidad}

    def calcular_total(self):
        total = 0
        for item in self.items.values():
            total += item['producto'].precio * item['cantidad']
        return total

    def aplicar_descuentos(self):
        total = self.calcular_total()
        cantidad_total = sum(item['cantidad'] for item in self.items.values())
        if cantidad_total >= 10:
            total *= 0.90  # Descuento del 10%
        elif any(item['cantidad'] > 5 for item in self.items.values()):
            total *= 0.98  # Descuento del 2%
        return total

def mostrar_categorias(categorias):
    print("Categorías disponibles:")
    for i, categoria in enumerate(categorias):
        print(f"{i + 1}. {categoria.nombre}")

def mostrar_productos(categoria):
    print(f"Productos en la categoría '{categoria.nombre}':")
    for i, producto in enumerate(categoria.productos):
        print(f"{i + 1}. {producto.nombre} - ${producto.precio:.2f}")

def main():
    # Crear categorías y productos
    dulces = Categoria("Dulces")
    dulces.agregar_producto(Producto("Caramelo", 0.50))
    dulces.agregar_producto(Producto("Chocolate", 1.00))

    salados = Categoria("Salados")
    salados.agregar_producto(Producto("Chips", 1.50))
    salados.agregar_producto(Producto("Galletas Saladas", 2.00))

    helados = Categoria("Helados")
    helados.agregar_producto(Producto("Helado de Vainilla", 3.00))
    helados.agregar_producto(Producto("Helado de Chocolate", 3.50))

    colaciones = Categoria("Colaciones")
    colaciones.agregar_producto(Producto("Frutos Secos", 2.50))
    colaciones.agregar_producto(Producto("Barra de Granola", 1.75))

    categorias = [dulces, salados, helados, colaciones]
    carrito = Carrito()

    while True:
        mostrar_categorias(categorias)
        seleccion_categoria = int(input("Seleccione una categoría (0 para salir): ")) - 1
        if seleccion_categoria == -1:
            break
        if seleccion_categoria < 0 or seleccion_categoria >= len(categorias):
            print("Categoría no válida. Intente de nuevo.")
            continue

        categoria_seleccionada = categorias[seleccion_categoria]
        while True:
            mostrar_productos(categoria_seleccionada)
            seleccion_producto = int(input("Seleccione un producto (0 para salir): ")) - 1
            if seleccion_producto == -1:
                break
            if seleccion_producto < 0 or seleccion_producto >= len(categoria_seleccionada.productos):
                print("Producto no válido. Intente de nuevo.")
                continue

            cantidad = int(input("Ingrese la cantidad: "))
            carrito.agregar_producto(categoria_seleccionada.productos[seleccion_producto], cantidad)

            continuar = input("¿Desea agregar más productos en esta categoría? (s/n): ")
            if continuar.lower() != 's':
                break

    # Datos del cliente
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección: ")

    # Forma de pago
    forma_pago = input("Seleccione forma de pago (1. Tarjeta de crédito, 2. Tarjeta de débito, 3. Transferencia): ")
    if forma_pago == '3':
        print("Envío gratis a su domicilio.")
    elif forma_pago == '2':
        print("Se aplicará un descuento del 2% por pago con tarjeta de débito.")

    # Calcular total y aplicar descuentos
    total = carrito.aplicar_descuentos()
    if forma_pago == '2':
        total *= 0.98  # Descuento adicional del 2% por pago con débito

    #
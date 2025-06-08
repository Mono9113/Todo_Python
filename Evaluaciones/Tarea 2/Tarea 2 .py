class libro:
    def __init__(self,isbn,titulo,especialidad,autor,editorial,edicion,año,costo):
        self.isbn=isbn
        self.titulo=titulo
        self.especialidad=especialidad
        self.autor=autor
        self.editorial=editorial
        self.edicion=edicion
        self.año=año
        self.costo=costo

    def mostrar(self):
        return f"""ISBN: {self.isbn}
        Libro: {self.titulo} 
Especialidad: {self.especialidad}
Autor: {self.autor}
Editorial: {self.editorial}
Edicion: {self.edicion}
Año: {self.año}
Costo: {self.costo}"""

class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_libro(self,isbn,titulo,especialidad,autor,editorial,edicion,año,costo):
        if titulo and isbn in self.productos:
            return f"El libro: {titulo},ISBN:{isbn} ya está en el inventario."
        self.productos[titulo] = libro(isbn,titulo,especialidad,autor,editorial,edicion,año,costo)
        return f"Libro {titulo} agregado al inventario."
    def mostrar_inventario(self):
        if not self.productos:
            return "El inventario está vacío."
        inventario_str = "\n".join([producto.mostrar_info() for producto in self.productos.values()])
        return inventario_str
    def actualizar_producto(self, titulo, cantidad):
        if titulo in self.productos:
            return self.productos[titulo].actualizar_stock(cantidad)
        return "Libro no encontrado en el inventario."
    def vender_producto(self, titulo, cantidad):
        if titulo in self.productos:
            return self.productos[titulo].vender_producto(cantidad)
        return "Libro no encontrado en el inventario."



#COSTO
while True:
    try:
        costo = int(input("Ingrese el costo del libro (máximo $3000): "))
        if costo <= 3000 and costo > 0:
            break
        else:
            print("El costo debe ser un número mayor a 0 y menor o igual a $3000. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

#CODIGO PROGRAMA
def mostrar_menu():
    print("\n--- SISTEMA DE PRESTAMO DE LIBROS ---")
    print("1. Ingresar datos de los libros")
    print("2. Ingresar datos de las personas que prestan")
    print("3. Visualizar datos ded los libros prestados")
    print("4. Visualizar datos de las personas que prestan")
    print("5. Visualizar grafico del ingreso monto a pagar de las personas que prestaron libros")
    print("6. Salir del programa")
    return input("Selecciona una opción: ")
def main():
    inventario = Inventario()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            titulo = input("Nombre del producto: ")
            precio = float(input("Precio del producto (€): "))
            cantidad = int(input("Cantidad en stock: "))
            print(inventario.agregar_producto(titulo, precio, cantidad))
        elif opcion == '2':
            print("\nInventario actual:")
            print(inventario.mostrar_inventario())
        elif opcion == '3':
            titulo = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Cantidad a añadir o restar (negativa para restar): "))
            print(inventario.actualizar_producto(titulo, cantidad))
        elif opcion == '4':
            titulo = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad a vender: "))
            print(inventario.vender_producto(titulo, cantidad))
        
        
        elif opcion == '6':
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

#PROGRAMA 
if __name__ == "__main__":
    main()
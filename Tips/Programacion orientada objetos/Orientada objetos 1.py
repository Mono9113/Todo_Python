class Producto:   #Define la clase producto.
    def __init__(self,nombre,precio):   #__init__ es un constructor lo que pide todo lo ingresado en init.
        self.nombre=nombre
        self.precio=precio

    def __str__(self):  #Sirve para imprimir con formato (trozo de cosas)
        return f"{self.nombre}: ${self.precio:.2f}"

class Factura: #Define la clase factura.
    def __init__(self,cliente):
        self.cliente=cliente
        self.productos=[]

    def agregar_producto(self,producto):
        self.productos.append(producto)

    def mostrar_lista(self):
        print(self.productos)

    def calcular_total(self):
        return sum(p.precio for p in self.productos)
    
    def __str__(self):
        detalle=f"Factura para: {self.cliente}\n"
        detalle+="-"*30+"\n"
        for p in self.productos:
            detalle+=f"{p}\n"
        detalle+="-"*30+"\n"
        detalle+=f"Total: ${self.calcular_total():.2f}"
        return detalle
    
######
producto1= Producto("Laptop",1200)   #Si lo hago con input se definen variable y se queda (a,b)
producto2= Producto("Mouse",25.50)
producto3= Producto("Teclado",45)

factura = Factura("Ana")
factura.agregar_producto(producto1)
factura.agregar_producto(producto2)
factura.agregar_producto(producto3)
factura.mostrar_lista()

print(factura)


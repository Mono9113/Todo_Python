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

    def agregar_producto(self,isbn,titulo,especialidad,autor,editorial,edicion,año,costo ):
        if titulo in self.productos:
            return f"El Libro {titulo},ISBN: {isbn} ya está en el inventario."
        self.productos[titulo] = libro(isbn,titulo,especialidad,autor,editorial,edicion,año,costo )
        return f"Libro {titulo} agregado al inventario."

#MENU
def mostrar_menu():
    print("\n--- SISTEMA DE PRÉSTAMO DE LIBROS ---")
    print("1. Ingresar datos de los libros prestados")
    print("2. Ingresar datos de las personas que prestan")
    print("3. Visualizar datos de los libros prestados")
    print("4. Visualizar datos de las personas que prestan")
    print("5. Visualizar gráfico del ingreso monto a pagar de las personas que prestaron libros ")
    print("6. Salir de programa")
    return input("Selecciona una opción: ")

def main():
    inventario = Inventario()
    while True:
        opcion = mostrar_menu()
        if opcion == '1': #Ingresar daros libros prestados
            isbn = int(input("ISBN: "))
            titulo = input("Titulo: ")
            especialidad = input("Especialidad: ")
            autor= input("Autor: ")
            editorial = input("Editorial: ")
            edicion = input("Edicion: ")
            año = int(input("Año: "))
            #Costo
            while True:
                try:
                    costo = int(input("Ingrese el costo del libro (máximo $3000): "))
                    if costo <= 3000 and costo > 0:
                        break
                    else:
                        print("El costo debe ser un número mayor a 0 y menor o igual a $3000. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")
            print(inventario.agregar_producto(isbn,titulo,especialidad,autor,editorial,edicion,año,costo))
        elif opcion == '2': #Ingresar datos personas prestan
            print()
        elif opcion == '3': #V. datos libros prestados
            print()
        elif opcion == '4': #V. datos personas prestan
            print()
        elif opcion == '5': #Grafico
            print()
        elif opcion == '6': #Salir
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

#Programa
if __name__ == "__main__":
    main()

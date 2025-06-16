import matplotlib.pyplot as plt


datos_libros = []
datos_personas = []

nombres = []
costos = []


class Libro:
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
        global datos_libros
        self.datos_libros = datos_libros

    def agregar_producto(self,isbn,titulo,especialidad,autor,editorial,edicion,año,costo ):
        if titulo in self.datos_libros:
            return f"El Libro {titulo},ISBN: {isbn} ya está en el inventario."
        datos_libros[titulo] = Libro(isbn,titulo,especialidad,autor,editorial,edicion,año,costo )
        return f"Libro {titulo} agregado al inventario."

class Personas:
    global datos_personas
    global nombres
    def __init__(self, rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, phono, email, nacimiento, direccion):
        self.rut = rut
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.phono = phono
        self.email = email
        self.nacimiento = nacimiento
        self.direccion = direccion
        
    def agregar_personas(self, rut, primer_nombre, segundo_nombre,apellido_paterno, apellido_materno, phono, email, nacimiento, direccion):
        if primer_nombre in datos_personas:
            return f"La persona {primer_nombre} {apellido_paterno} {apellido_materno},rut: {rut} ya está ingresada."
        datos_personas[primer_nombre] = Personas(self, rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, phono, email, nacimiento, direccion)
        return f"Usuario {primer_nombre} ingresado exitosamente."
        

    def __str__(self):
        return f"""Nombres y apellidos: {self.primer_nombre} {self.segundo_nombre} {self.apellido_paterno} {self.apellido_materno}
        Rut: {self.rut}
        Nacimiento: {self.nacimiento}
        Email: {self.email}
        Phono: {self.phono}
        Direccion: {self.direccion}
        """
    
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
    while True:
        opcion = mostrar_menu()
        if opcion == '1': #Ingresar daros libros prestados
            datos_libros_ingresados = True
            isbn = str(input("Ingrese ISBN: "))
            titulo = str(input("Ingrese título del libro: "))
            especialidad = str(input("Ingrese especialidad: "))
            autor = str(input("Ingrese el nombre del autor: "))
            editorial = str(input("Ingrese editorial: "))
            edicion = str(input("Ingrese edición del libro: "))
            año = str(input("Ingrese año del libro: "))
            while True:
                try:
                    costo = int(input("Ingrese el costo del libro (máximo $3000): "))
                    if costo <= 3000 and costo > 0:
                        costo=costo
                        break
                    else:
                        print("El costo debe ser un número mayor a 0 y menor o igual a $3000. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")
            libro = Libro(isbn, titulo, especialidad, autor, editorial, edicion, año, costo)
            datos_libros.append(libro)
            costos.append(costo)
            Inventario.agregar_producto(isbn,titulo,especialidad,autor,editorial,edicion,año,costo)

        elif opcion == '2': #Ingresar datos personas prestan
            datos_personas_ingresados=True
            print("opcion 2")
            rut=str(input("ingrese rut:"))
            primer_nombre=str(input("ingrese primer nombre: "))
            segundo_nombre=str(input("ingrese segundo nombre: "))
            apellido_paterno=str(input("ingrese apellido paterno: "))
            apellido_materno=str(input("ingrese apellido materno: "))
            phono=str(input("ingrese numero de telefono: "))
            email=str(input("ingrese correo electronico: "))
            nacimiento=str(input("ingrese fecha de nacimiento dd/mm/aa: "))
            direccion=str(input("ingrese su dirección: "))
            print(f"Costo: {costo}")
            people = Personas(rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, phono, email, nacimiento, direccion)
            nombres.append(primer_nombre)

        elif opcion == '3': #V. datos libros prestados
            if datos_libros_ingresados == True:
                for i in range(0,len(datos_libros)):
                    libro.mostrar()
            else:
                print("No hay datos ingresados")

        elif opcion == '4': #V. datos personas prestan
            if datos_personas_ingresados == True:
                print("opcion 4")
                for i in range(0,len(datos_personas)):
                    people.__str__()
            else:
                print("No hay datos ingresados")

        elif opcion == '5': #Grafico
            print("opcion 5")
            if datos_libros_ingresados == True and datos_personas_ingresados == True:
                plt.bar(nombres, costos, color="skyblue")
                plt.title("Grárfico de barras")
                plt.xlabel("Personas")
                plt.ylabel("Monto a pagar")
                plt.show()

        elif opcion == '6': #Salir
            print("¡Gracias por usar el sistema de inventario!")
            break
        


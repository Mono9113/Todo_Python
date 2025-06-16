import matplotlib.pyplot as plt

datos_libros = []
datos_personas = []

nombres = []
costos = []


class libros:
    def __init__(self, ISBN, titulo, especialidad, autor, editorial, edicion, año, costo):
        self.ISBN = ISBN
        self.titulo = titulo
        self.especialidad = especialidad
        self.autor = autor
        self.editorial = editorial
        self.edicion = edicion
        self.año = año
        self.costo =costo

    def __repr__(self):
        return (f"\nISBN: {self.ISBN}\n"
                f"Titulo: {self.titulo}\n"
                f"Especialidad: {self.especialidad}\n"
                f"Autor: {self.autor}\n"
                f"Editorial: {self.editorial}\n"
                f"Edición: {self.edicion}\n"
                f"Año: {self.año}\n"
                f"Costo: ${self.costo}\n")


class personas:
    def __init__(self, rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, phono, email,
                nacimiento, direccion):
        self.rut = rut
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.phono = phono
        self.email = email
        self.nacimiento = nacimiento
        self.direccion = direccion

    def __repr__(self):
        return (f"\nRut: {self.rut}\n"
                f"Primer nombre: {self.primer_nombre}\n"
                f"Segundo nombre: {self.segundo_nombre}\n"
                f"Apellido paterno: {self.apellido_paterno}\n"
                f"Apellido materno: {self.apellido_materno}\n"
                f"Phono: {self.phono}\n"
                f"Email: {self.email}\n"
                f"Fecha de nacimiento: {self.nacimiento}\n")


datos_libros_ingresados = False
datos_personas_ingresados = False

# ----------------- ejecución ------------------------
while True:
    print("--------- MENU ----------")
    print("1) Ingresar datos de libros prestados")
    print("2) Ingresar datos de personas que prestan")
    print("3) Visualizar datos de los libros prestados")
    print("4) Visualizar datos de las personas que prestan")
    print("5) Visualizar gráfico del ingreso monto a pagar de las personas que prestaron libros")
    print("6) Salir del programa")
    op = int(input("\nIngrese opción: "))

    if op == 1:
        datos_libros_ingresados = True
        isbn = str(input("Ingrese ISBN: "))
        titulo = str(input("Ingrese título del libro: "))
        especialidad = str(input("Ingrese especialidad: "))
        autor = str(input("Ingrese el nombre del autor: "))
        editorial = str(input("Ingrese editorial: "))
        edicion = str(input("Ingrese edición del libro: "))
        año = str(input("Ingrese año del libro: "))
        try:
          costo = int(input("ingrese un valor entre 0 y 3000: "))
          while  costo>3000:
            print("valor invalido, ingrese un valor entre 0 y 3000: ")
        except (ValueError,IndexError)  :
            print("ingrese valores validos")


        libro = libros(isbn, titulo, especialidad, autor, editorial, edicion, año, costo)
        datos_libros.append(libro)
        costos.append(int(costo))

    elif op == 2:
        datos_personas_ingresados = True
        rut = str(input("Ingrese rut: "))
        primer_nombre = str(input("Ingrese primer nombre: "))
        segundo_nombre = str(input("Ingrese segundo nombre: "))
        apellido_paterno = str(input("Ingrese apellido paterno: "))
        apellido_materno = str(input("Ingrese apellido materno: "))
        phono = str(input("Ingrese phono: "))
        email = str(input("Ingrese email: "))
        nacimiento = str(input("Fecha de nacimiento (dd-mm-aa): "))
        direccion = str(input("Ingrese dirección: "))

        persona = personas(rut, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, phono, email,
                           nacimiento, direccion)
        datos_personas.append(persona)
        nombres.append(primer_nombre)

    elif op == 3:
        if datos_libros_ingresados:
            print("\n--- Datos de los libros prestados ---")
            for libro in datos_libros:
                print(libro)
        else:
            print("Primero debe ingresar los datos de los libros (opción 1).")

    elif op == 4:
        if datos_personas_ingresados:
            print("\n--- Datos de las personas que prestan ---")
            for persona in datos_personas:
                print(persona)
        else:
            print("Primero debe ingresar los datos de las personas (opción 2).")

    if op == 5:

        if datos_libros_ingresados == True and datos_personas_ingresados == True:
            plt.bar(nombres, costos, color="skyblue")

            plt.title("Gráfico de barras")

            plt.xlabel("Personas")

            plt.ylabel("Monto a pagar")

            plt.show()

            print("Debe ingresar datos de libros y personas para ver el gráfico (opciones 1 y 2).")

    elif op == 6:
        print("Salir del programa.")
        break

    elif op < 1 or op > 6:
        print("Opción ingresada inválida. Intente nuevamente.")

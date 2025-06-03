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


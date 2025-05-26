class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio

    def descripcion(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Anio: {self.anio}")


######
libro1= Libro("Casa","Pepe",2010)
#print(libro1)
libro1.descripcion()

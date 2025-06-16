f=0
#Definicion de clase.
class ventas():
    def __init__(self,nombre_vendedor,precio_articulo,monto_comision): #Constructor 
        global f
        self.nombre_vendedor=str(nombre_vendedor)
        self.precio_articulo=int(precio_articulo)
        self.monto_comision=int(monto_comision*0)
        f=1
    def calcular_comision(self): #Metodo de calculo de comision.
        if self.precio_articulo < 30000:
            self.monto_comision = self.precio_articulo*0.02
        elif self.precio_articulo in range (30000,50000):
            self.monto_comision = self.precio_articulo*0.04
        elif self.precio_articulo >= 50000:
            self.monto_comision = self.precio_articulo*0.05
    def __str__(self):
        return f"""
\n---------------------
Nombre vendedor: {self.nombre_vendedor}
Precio articulo: {self.precio_articulo}
Monto comision: {self.monto_comision}
---------------------"""

#Programa principal.
while True:
    print("\n---Menu---")
    print("1.Ingreso de datos y creacion del objeto.")
    print("2.Calcular comision.")
    print("3.Mostrar datos (estado) del objeto.")
    print("4.Salir")
    op=int(input("Ingrese opcion: "))
    if op not in range(1,4):
        print("\nNumero no valido, intente nuevamente.")
    if op==1:
        a=input("\nIngrese nombre vendedor: ")
        b=int(input("Ingrese precio articulo: "))
        c=0
        comision=ventas(a,b,c)
    if op==2:
        if f==1:
            print("\nSe ha calculado la comision.")
            comision.calcular_comision()
        elif f==0:
            print("\nNo se a creado el articulo.\nEliga opcion 1.")
    if op==3:
        if f==1:
            print(comision)
        elif f==0:
            print("\nNo se a creado el articulo.\nEliga opcion 1.")
    if op==4:
        print("\n<PROGRAMA TERMINADO>\n")
        break


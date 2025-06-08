
f=0
class compra():
    def __init__(self,nombre_cliente,monto_compra):
        global f
        self.nombre_cliente= str(nombre_cliente)
        self.monto_compra=float(monto_compra)
        f=1
    def calcular_descuento(self):
        if self.monto_compra <= 100:
            self.monto_descuento=0
        elif self.monto_compra in range (100,501):
            self.monto_descuento=self.monto_compra*0.05
        elif self.monto_compra >= 500:
            self.monto_descuento=self.monto_compra*0.1 

    def __str__(self):
        return f"\n---------------\nNombre: {self.nombre_cliente} \nMonto sin descuento: {self.monto_compra} \nMonto con decuento: {self.monto_descuento}\n --------------------------"
        

#Programa


while True:
    print("\n---MENU TIENDA---")
    print("1. Ingresar datos y crear compra")
    print("2. Calcular descuento")
    print("3. Mostrar detalles dela compra")
    print("4. Salir")
    op=int(input("Ingrese opcion: "))

    if op==1:
        a=input("\nIngrese Nombre: ")
        b=float(input("Ingrese Monto: "))
        obj=compra(a,b)
    if op==2:
        if f==1:
            print("\n Desceunto calculado.")
            obj.calcular_descuento()
        elif f==0:
            print("\nNo se a creado una compra, eliga opcion 1.")
    if op==3:
        if f==1:
            print(obj)
        elif f==0:
            print("\nNo se a creado una compra, eliga opcion 1.")
    if op==4:
        break
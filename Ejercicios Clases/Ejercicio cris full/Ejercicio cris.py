t=1
op=0
while t==1 or op==0:
    print("---------Plataforma areas figuras geometricas----------")
    print("1)Area trinagulo.")
    print("2)Area rectangulo.")
    print("3)Area circulo.")
    print("4) Salir del programa.")
    op=int(input("Ingrese opcion: "))
    if op==0:
        print("---------Plataforma areas figuras geometricas----------")
        print("1)Area trinagulo.")
        print("2)Area rectangulo.")
        print("3)Area circulo.")
        op=int(input("Ingrese opcion: "))
    elif op==1:
        a=0
        h=float(input("Ingrese altura del triangulo: "))
        b=float(input("Ingrese la base del trinagulo: "))
        a=(b*h)/2
        print(f"El area del tirangulo es {a}")
        op=int(input("Presione 0 para volver al menu: "))
    elif op==2:
        a=0
        h=float(input("Ingrese altura del rectangulo: "))
        b=float(input("Ingrese la base del rectangulo: "))
        a=(b*h)
        print(f"El area del tirangulo es {a}")
        op=int(input("Presione 0 para volver al menu: "))
    elif op==3:
        a=0
        pi=3.14
        r=float(input("Ingrese radio del circulo: "))
        a=pi*(r**2)
        print(f"El area del circulo es de {a}.")
        op=int(input("Presione 0 para volver al menu: "))
    elif op==4:
        print("Programa terminado....... Hasta pronto...")
        t=2

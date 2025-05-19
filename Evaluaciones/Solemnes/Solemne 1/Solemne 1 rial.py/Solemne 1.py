t=1
while t==1:
    print("SUPERMENU")
    print("1. Arriendo departamentos.")
    print("2. Intereses de ganancia.")
    print("3. Cantidad de pintura.")
    print("4. Cerrar programa.")
    op=int(input("Ingrese opcion: "))
    if op==1:
        p=1
        print("ARRIENDO DEPTO")
        nombre=input("Ingrese su nombre: ")
        rut=input("Ingrese su rut: ")
        while p==1:
            print("1. Depto 1 Habitacion")
            print("2. Depto 2 Habitacion")
            print("3. Depto 3 Habitacion")
            print("4. Factura.")
            print("5. Terminar dia.")
            op1=int(input("Ingrese opcion: "))
            th2=0
            dh2=0
            th1=0
            dh1=0
            dh3=0
            th3=0
            desc=0
            total=0
            h1=0
            h2=0
            h3=0
            totald=0
            if op1==1:
                print("Valor diario depto 1 habitacion: $30000")
                h1+=1  #cantidad por numero de hab
                dh1=int(input("Ingrese cantidad de dias: "))
                th1=dh1*30000
                totald+=dh1
                total+=th1
            if op1==2:
                print("Valor diario depto 2 habitacion: $45000")
                h2+=1  #cantidad por numero de hab
                dh2=int(input("Ingrese cantidad de dias: "))
                th2=dh2*45000
                totald+=dh2
                total+=th2
            if op1==3:
                print("Valor diario depto 1 habitacion: $55000")
                h3+=1  #cantidad por numero de hab
                dh3=int(input("Ingrese cantidad de dias: "))
                th3=dh3*55000
                totald+=dh3
                total+=th3
            if op1==4:
                print("FACTURA")
                print(f"Nombre: {nombre}")
                print(f"Rut: {rut}")
                if dh1>7 or dh2>7 or dh3>7:
                    desc=(th1+th2+th3)*0.085
                    print(f"Descuento por mas de 7 dias: {desc}")
                print(f"Monto Bruto a pagar: {total}")
                print(f"Total a pagar: {(total)-desc}")
            if op1==5:
                promdias=(totald)/3
                prommont=(total)/3
                print(f"1. Depto 1 habitacion arrendados: {h1}")
                print(f"1. Depto 2 habitacion arrendados: {h2}")
                print(f"1. Depto 3 habitacion arrendados: {h3}")
                print(f"El promedio de dias de todos los deptos: {promdias}")
                print(f"Departamentos arrendados: {h1+h2+h3}")
                p=2
    if op==2:
        print("Interses y ganancias.")
        capital=int(input("Ingrese su capital: "))
        tasa=int(input("Ingrese tasa en %: "))
        tiempo=int(input("Ingrese meses a depositar: "))
        tiempo2=(tiempo/100)/12
        montint=capital*tasa*tiempo2
        captotal=capital+montint
        print(f"Ganara a un plazo de {tiempo} mese un interes de ${montint}")
        print(f"Su capital total en {tiempo} meses sera de ${captotal}")
    if op==3:
        a1=float(input("Ingrese ancho muro 1 mts: "))
        a2=float(input("Ingrese ancho muro 2 mts: "))
        a3=float(input("Ingrese ancho muro 3 mts: "))
        a4=float(input("Ingrese ancho muro 4 mts: "))
        l1=float(input("Ingrese alto muro 1 mts: "))
        l2=float(input("Ingrese alto muro 2 mts: "))
        l3=float(input("Ingrese alto muro 3 mts: "))
        l4=float(input("Ingrese alto muro 4 mts: "))
        lp=float(input("Ingrese alto puerta mts: "))
        ap=float(input("Ingrese ancho puerta mts: "))
        areap=ap*lp
        aream=((a1*l1)+(a2*l2)+(a3*l3)+(a4*l4))-areap
        pintura=aream/3
        print(f"Para pintar {aream:.2f} mts cuadrados de muro necesitas {pintura:.2f} Lts de pintura.")
    if op==4:
        print("Programa terminado")
        print("Vuelava pronto")
        t=2
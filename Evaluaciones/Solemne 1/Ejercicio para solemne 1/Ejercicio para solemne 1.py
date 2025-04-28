p=1
t=0
cen=0
cea=0
ceam=0
op=1
print("Bienvenidom al parque de diversiones fantasiputa")
n=input("Ingrese su nombre: ")
while p==1:
    print("*******************************************")
    print("1. Entrada niño (3 a 12 años) valor: $8000 c/u")
    print("2. Entrada adulto (13 a 64 años) valor: $12000 c/u")
    print("3. Entrada adulto mayor (65 años o mas) valor: $7000")
    print("4. Ir a pagar.")
    op=int(input("Ingrese una opcion: "))
    while op<0 or op>4:
        print("Numero no valido. \nIntente nuevamente.")
        print("Bienvenidom al parque de diversiones fantasiputa")
        print("1. Entrada niño (3 a 12 años) valor: $8000 c/u")
        print("2. Entrada adulto (13 a 64 años) valor: $12000 c/u")
        print("3. Entrada adulto mayor (65 años o mas) valor: $7000")
        print("4. Ir a pagar.")
        op=int(input("Ingrese una opcion: "))
    while op==0:
        print("*******************************************")
        print("1. Entrada niño (3 a 12 años) valor: $8000 c/u")
        print("2. Entrada adulto (13 a 64 años) valor: $12000 c/u")
        print("3. Entrada adulto mayor (65 años o mas) valor: $7000")
        print("4. Ir a pagar.")
    op=int(input("Ingrese una opcion: "))
    while op==1:
        print("*******************************************")
        print("Valor entrada niños: $8000")
        print("Presione 0 para volver al menu.")
        cen=int(input("Ingrese cantidad de entradas: "))
        vtotal=cen*8000
        et+=cen
    while op==2:
        print("*******************************************")
        print("Valor entrada adulto: $12000")
        print("Presione 0 para volver al menu.")
        cea=int(input("Ingrese cantidad de entradas: "))
        vtotal=cea*12000
        et+=cea
    while op==3:
        print("*******************************************")
        print("Valor entrada adulto mayor: $7000")
        print("Presione 0 para volver al menu.")
        ceam=int(input("Ingrese cantidad de entradas: "))
        vtotal=ceam*7000
        et+=ceam
    while op==4:
        print("**************BOLETA****************")
        print(f"Nombre comprador: {n}")
        print(f"Cantidad de boletos comprados: {et}")
        print(f"Monto Bruto a pagar: ${vtotal}")
        if et>=5:
            desct=vtotal*0.10
            print(f"Monto descuento compra mas de 5 entradas: ${desct}")
            print(f"Monto total a pagar: {vtotal-desct}")
        else:
            print(f"Monto total a pagar: ${vtotal}")
        p=2
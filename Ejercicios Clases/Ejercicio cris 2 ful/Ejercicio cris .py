t=1
while t==1:
    print("""\n--------Menu principal-----------
1) Promedio tres numeros.
2) Determina si numero es par o impar.
3) Elevacion a la potencia.
4) Salir del programa.""")
    op=int(input("Ingrese opcion: "))
    while op<1 or op>4:
        print("\nNumero no valido.")
        print("Intente nuevamente")
        print("""--------Menu principal-----------
1) Promedio tres numeros.
2) Determina si numero es par o impar.
3) Elevacion a la potencia.
4) Salir del programa.""")
        op=int(input("Ingrese opcion: "))
    if op==1:
        i=1
        suma=0
        while i<=3:
            n1=float(input("\nIngrese Numero para promedio: "))
            suma=suma+n1
            i+=1
        print(f"Promedio = {suma/3}")
    elif op==2:
        n=int(input("\nIngrese un numero para saber si es par: "))
        if n%2==0:
            print(f"El numero {n} es par.")
        else:
            print(f"El numero {n} es impar.")
    elif op==3:
        n=int(input("\nIngrese numero entero base: "))
        p=int(input("Ingrese numero exponente: "))
        print(f"{n}^{p}= {n**p}")
    elif op==4:
        print("\nPrograma terminado...hasta pronto...")
        t=2
    
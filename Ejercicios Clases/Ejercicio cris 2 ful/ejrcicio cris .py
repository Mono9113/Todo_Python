t=1
while t==1:
    print("****************************************")
    print("Multiplataforma")
    print("1. Promedio de tres numeros.")
    print("2. Saber si un numero es par o impar.")
    print("3. Elevar un numero a la potencia dada.")
    print("4. Salir del programa.")
    op=int(input("Ingrese opcion: "))
    if op==1:
        print("****************************************")
        n1=float(input("Ingrese primer numero: "))
        n2=float(input("Ingrese segundo numero: "))
        n3=float(input("Ingrese tercer numero: "))
        prom=(n1+n2+n3)/3
        print(f"El promedio es {prom}")
    if op==2:
        print("****************************************")
        n=int(input("Ingrese numero para determinar si es par o no: "))
        if n%2==0:
            print(f"El {n} es par.")
        else:
            print(f"El {n} es impar.")
    if op==3:
        print("****************************************")
        b=int(input("Ingrese numero base: "))
        e=int(input("Ingrese numero exponente: "))
        c=b**e
        print(f"{b}**{e}={c}")
    if op==4:
        print("****************************************")
        print("Programa terminaddo..... Hasta pronto...")
        print("****************************************")
        t=2
"""Realice un programa que permita al usuario ingresar un numero entre el 1 y el 12 (debe validar) y muestre la divisi
on de los numeros del 1 al 12 por el numero ingresado
Ejemplo:
Ingrese un numero entre el 1 y el 12 entero: 13
El numero ingresado no es valido. Intente nuevamente
Ingrese un numero entre el 1 y el 12 entero: 3
1 / 3 = 0.3333333333333333
2 / 3 = 0.6666666666666666
3 / 3 = 1.0
4 / 3 = 1.3333333333333333
5 / 3 = 1.6666666666666667
6 / 3 = 2.0
7 / 3 = 2.3333333333333335
8 / 3 = 2.6666666666666665
9 / 3 = 3.0
10 / 3 = 3.3333333333333335
11 / 3 = 3.6666666666666665
12 / 3 = 4.0"""
n=int(input("Ingrese un numero [1----12]: "))
i=1
while n<1 or n>12:
    print("Numero no valido.")
    print("Intente nuevamente.")
    n=int(input("Ingrese un numero [1----12]: "))
while i<=12:
    print(f"{i}/{n}=",round(i/n,2))  #Funcion round(###,2) dice que define a 2 decimales la lectura del numero.
    i+=1 
    
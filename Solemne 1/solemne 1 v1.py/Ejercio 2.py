"""Realice un programa que permita al usuario ingresar un numero entre el 1 y el 12 (debe validar) y muestre las tablas de
multiplicar de dicho numero:"""

n=int(input("Ingrese numero [1-----12]: "))
i=1
#Este while valida que el numero este entre los rangos solicitados
while n<1 or n>12:
    print("Numero no valido.")
    n=int(input("Ingrese numero [1-----12]: "))
while i<= 12:
    print(f"{i} x {n} = {i*n}")
    i+=1

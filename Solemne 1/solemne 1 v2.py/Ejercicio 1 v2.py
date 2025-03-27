"""Solicite al usuario ingresar un numero entero positivo y que imprima cuales son los numeros pares desde el 1 hasta
el numero ingresado, ambos inclusive.
Ejemplo:
Bienvenido
Ingrese un entero positivo para mostrar los pares: 5
El 2 es par
El 4 es par"""
i=2
print("Bienvenido")
n=int(input("Ingrese un numero positivo para mostrar los pares: "))
while n<1:
    print("Numero no valido.")
    n=int(input("Ingrese un numero positivo para mostrar los pares: "))
while i<=n:
    print(f"El {i} es par")
    i+=2
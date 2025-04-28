"""Solicite al usuario ingresar un numeroentero positivo y que imprima cuales son los numeros impares desde el 1 hasta
el numero ingresado, ambos inclusive.
Ejemplo:
Bienvenido
Ingrese un entero positivo para mostrar los impares: 5
El 1 es impar
El 3 es impar
El 5 es impar"""
n=int(input("Ingrese Numero positivo: "))
while n<1:
    print("Numero no valido.")
    n=int(input("Ingrese Numero positivo: "))
i=1
while i <= n:
    print(f"El {i} es impar")
    i+=2


#Este es par avalidar el numero   
# while n<1:
#     print("Numero no valido.")
#     n=int(input("Ingrese Numero positivo: "))
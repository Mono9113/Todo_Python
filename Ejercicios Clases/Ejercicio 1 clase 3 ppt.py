"""A continuacion, realizar una aplicacion practica de condicionales, comparadores y algunos operadores matematicos
Para este ejercicio se pedira in diseño simple que compare la multiplicacion de variables ingresadas por el ususario.
Lo primordial es que el programa indique si el resultado de la multiplicacion es par o impar."""

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
multi= a*b
resu= multi%2
if resu==0:
    print("El resultado de la multiplicacion es par")
else:
    print("El resultado de la multiplicacion es impar")


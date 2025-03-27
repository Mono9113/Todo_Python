# Solicite al usuario ingresar un numero entero positivo y que imprima cuales son los numeros divisibles por 3 desde
# el 1 hasta el numero ingresado, ambos inclusive.
# Ejemplo:
# Bienvenido
# Ingrese un entero positivo para mostrar los divisibles por 3: 13
# El 3 es divisible por 3
# El 6 es divisible por 3
# El 9 es divisible por 3
# El 12 es divisible por 3

n=int(input("Ingrese un numero entero positivo: "))
i=1
while i<=n: #Mientras i (numero que representa el 1) 
    if i%3==0:
        print(f"El {i} es divisible por 3")
    i+=1

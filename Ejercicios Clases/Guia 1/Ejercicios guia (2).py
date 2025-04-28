"""Ingresa dos numeros por teclado, Imprimir los numeros naturales que hay entre ambos numeros empezando por el mas
pequeño, contar cuantos hay contar cuantos son pares y calcular la suma de los impares"""

n1=int(input("Introduzca primer numero: "))
n2=int(input("Introduzca segundo numero: "))
Inicio=min(n1,n2)
fin=max(n1,n2)
Numeros_naturles= 0
Numeros_pares=0
Suma_impares=0
print(f"Los numeros naturales entre {Inicio} y {fin} son:")
for i in range(Inicio,fin+1):
    print(i, end="")
    Numeros_naturles+= 1
    if i%2==0:
        Numeros_pares+=1
    else:
        Suma_impares+=i
print(f"\nHay {Numeros_naturles} numeros naturales entre {Inicio} y {fin}")
print(f"Hay {Numeros_pares} numeros pares entre {Inicio} y {fin}")
print(f"La suma de los impares entre {Inicio} y {fin} es: {Suma_impares}")



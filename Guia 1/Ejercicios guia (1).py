"""Primer ejercicio: Para el intervalo cerrado [347,2342]:
-Imprimir y contar los multiplos de 7 y sumar el cuadrado de ellos.
-Contar los multiplos de 3 """
inicio= 347
fin= 2342
contador_mult_7= 0
Suma_cuadrados_mult_7= 0
Contador_mult_3= 0

for num in range(inicio,fin+1):
          if num % 7 == 0:
              contador_mult_7 += 1
              Suma_cuadrados_mult_7 += num**2
          if num % 3 == 0:
              Contador_mult_3 += 1
print(f"El contador de multiplos de 7 es: {contador_mult_7}")
print(f"La suma de los cuadrados de los multiplos de 7 es: {Suma_cuadrados_mult_7}")
print(f"El contador de multiplos de 3 es: {Contador_mult_3}")


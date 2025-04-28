# Lea los valores de los lados de un triángulo. Determine y muestre un mensaje si corresponde a
# 1.Equilatero
# 2. Isósceles
# 3. Escaleno
lado_1=int(input("Introduzca primer lado: "))
lado_2=int(input("Introduzca segundo lado: "))
lado_3=int(input("Introduzca tercer lado: "))
if lado_1 == lado_2 == lado_3:
    print("Es un trinagulo equilatero")
elif lado_1==lado_2 or lado_1==lado_3 or lado_2==lado_3:
    print("Es un triangulo isosceles")
elif lado_1!=lado_2!=lado_3:
    print("Es un trinagulo escaleno.")
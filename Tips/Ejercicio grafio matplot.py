import matplotlib.pyplot as plt 

#Datos de ejemplo
categoria=[]
valores= []

#Programa
c=int(input("Cantidad de categorias: "))
i=1
while i<=c:
    frut=input("Ingrese nombre de la fruta: ")
    categoria.append(frut)
    cant=int(input(f"Ingrese cantidad de {frut}: "))
    valores.append(cant)
    i+=1

#Crear el grafico de barras
print("DEFINICION DE COLORES")
r=input("Cantidad de Rojo de 00 a ff hexadecimal: ")
g=input("Cantidad de Azul de 00 a ff hexadecimal: ")
b=input("Cantidad de Verde de 00 a ff hexadecimal: ")
plt.bar(categoria,valores,color="#"+r+g+b)
#Añadir titulo y etiquetas
plt.title('Cantidad de Frutas')
plt.xlabel('Fruta')
plt.ylabel('Cantidad')
plt.show()
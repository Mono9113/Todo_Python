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
<<<<<<<< HEAD:Tips/Ejercicio grafio matplot.py
print("DEFINICION DE COLORES")
========
print("\nDEFINICION DE COLORES")
>>>>>>>> d5412742b97485d92f0d69223b96c7207f4f7989:Tips/a.py
r=input("Cantidad de Rojo de 00 a ff hexadecimal: ")
g=input("Cantidad de Azul de 00 a ff hexadecimal: ")
b=input("Cantidad de Verde de 00 a ff hexadecimal: ")
plt.bar(categoria,valores,color="#"+r+g+b)
<<<<<<<< HEAD:Tips/Ejercicio grafio matplot.py
========

>>>>>>>> d5412742b97485d92f0d69223b96c7207f4f7989:Tips/a.py
#Añadir titulo y etiquetas
plt.title('Cantidad de Frutas')
plt.xlabel('Fruta')
plt.ylabel('Cantidad')
<<<<<<<< HEAD:Tips/Ejercicio grafio matplot.py
plt.show()
========
plt.show()

>>>>>>>> d5412742b97485d92f0d69223b96c7207f4f7989:Tips/a.py

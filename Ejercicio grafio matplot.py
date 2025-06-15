import matplotlib.pyplot as plt

#Datos de ejemplo
categoria=[]
valores= []

#Crear el grafico de barras
plt.bar(categoria,valores,color='skyblue')

#Añadir titulo y etiquetas
plt.title('Cantidad de Frutas')
plt.xlabel('Fruta')
plt.ylabel('Cantidad')

#Mostrar grafico
def mostrar():
    plt.show()

#Programa
while True:
    frut=input("Ingrese nombre de la fruta: ")
    cant=int(input(f"Ingrese cantidad de {frut}: "))
    op=print("Para mostrar grafico presione 0")
    if op ==0:
        mostrar()
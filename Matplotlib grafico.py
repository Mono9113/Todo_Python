import matplotlib.pyplot as plt 

#Datos de ejemplo
categoria=['Manzana','Bananas','Cereza','Naranjas']
valores= [10,15,7,12]

#Crear el grafico de barras
plt.bar(categoria,valores,color='skyblue')

#Añadir titulo y etiquetas
plt.title('Cantidad de Frutas')
plt.xlabel('Fruta')
plt.ylabel('Cantidad')

#Mostrar grafico
plt.show()
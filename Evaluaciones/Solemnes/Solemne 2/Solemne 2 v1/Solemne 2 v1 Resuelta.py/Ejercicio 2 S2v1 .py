def llenarTemperaturas():
    temperaturas=[]
    for i in range(24):
        temp=float(input(f"Ingrese temperatura para la hora {i}: "))
        temperaturas.append(temp)
    return temperaturas
def obtenerPromedios(lista):
    return sum(lista)/len(lista)
def detectarAnomalias(lista,promedio):
    with open("Anomalias.txt","w") as archivo:
        for i, temp in enumerate(lista):
            if abs(temp-promedio)>=5:
                archivo.write(f"Dia {i}: Temperatura anomala = {temp} °c \n")

temps = llenarTemperaturas()
prom = obtenerPromedios(temps)
detectarAnomalias(temps, prom)
print(temps)
print(prom)
print("Análisis completado. Revisa el archivo 'anomalías.txt'.")
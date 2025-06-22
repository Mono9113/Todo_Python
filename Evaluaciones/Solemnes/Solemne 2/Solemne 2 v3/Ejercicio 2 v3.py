def registrar_notas():
    notas=[]
    i=1
    while len(notas) < 24:
        try:
            n=float(input(f"Ingrese la nota del estudiante {i}: "))
            if 1<=n<=7:
                notas.append(n)
                i+=1
            else:
                print("Valor no valido rango[1-7]. Intente nuevamente.")
        except ValueError:
            print("Entrada no valida.")
    return notas

def obtener_promedios(lista):
    return sum(lista)/len(lista)

def detectar_anomalias(lista,promedio):
    with open("Anomalias.txt","w") as archivo:
        for i, n in enumerate(lista):
            if abs(n-promedio)>=5:
                print(f"Anomalía detectada: estudiante {i+1}, nota = {n}")
                archivo.write(f"Estudiante {i+1} tiene un rendimiento anomalo: {n:.1f}\n")

notas=registrar_notas()
promedios=obtener_promedios(notas)
detectar_anomalias(notas,promedios)
print(notas)
print(promedios)
print("Análisis completado. Revisa el archivo 'anomalías.txt'.")
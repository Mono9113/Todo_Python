def r_rendimiento():
    rendimiento=[]
    i=1
    while len(rendimiento) < 24:
        try:
            rend=float(input(f"Ingrese el rendimiento del jugador {i}: "))
            if 0 <= rend <= 100:
                rendimiento.append(rend)
                i+=1
            else:
                print("Valor fuera del rango [0-100], intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
    return rendimiento

    # for i in range(1,25):
    #     rend=float(input(f"Ingrese el rendimiento del jugador {i}: "))
    #     if rend >= 0 and rend <= 100:
    #         rendimiento.append(rend)
    #     else:
    #         print(f"Valor feura de los rangos [0-100], intente nuevamente.")
    # return rendimiento

def o_promedio(lista):
    return sum(lista)/len(lista)

def d_anomalias(lista,promedio):
    with open("anomalias.txt","w") as archivo:
        for i,rend in enumerate(lista):
            if abs(rend-promedio)>=5:
                archivo.write(f"Jugador {i+1} con rendimiento anomalo= {rend:.2f} %\n")

rendimientos= r_rendimiento()
promedios= o_promedio(rendimientos)
d_anomalias(rendimientos,promedios)
print()
print(rendimientos)
print(promedios)
print("Análisis completado. Revisa el archivo 'anomalías.txt'.")

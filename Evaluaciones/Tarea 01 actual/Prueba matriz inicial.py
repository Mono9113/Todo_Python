# matriz=[]
# i=0
# npoleras=int(input("Ingrese cantidad de tipos de poleras: "))
# ndias=int(input("Ingrese cantidad de dias: "))
# while i<npoleras:   #La remplazare con npoleras=... por 10
#     n=1
#     p=0
#     #while p<npoleras: 
#     matriz.append(f"Tipo polera ")  #Se podria definir variable tipo n que sea un input que sea tanto como para matriz como para tipo polera
#     matriz.append(("\t0")*ndias)  #Se podria multipicar esa matriz por la cantidad de n
#     i+=1
# i=0
# matriz[0]="\t" #Este cambiar por dias
# matriz[1]="\tDias"  #se podria cambiar el dias por numeros y el primer dias de la fila se remplaza arriba con 
# #matriz[1].append(Dias)
# while i<(npoleras*ndias):  #hacer que se repita con formula i+=n y hacer while haciendo que matriz se genere
#     print(f"{matriz[i]} {matriz[i+1]} {matriz[i+2]} {matriz[i+3]} ")
#     i+=1

#******************************************************************************************

matriz=[]
numero_dias=int(input("Ingrese numero de dias: "))
i=0
while i<10:
    matriz.append(f"Tipo polera ")   #Se podria definir variable tipo n que sea un input que sea tanto como para matriz como para tipo polera
    matriz.append("\t")  #Se podria multipicar esa matriz por la cantidad de n
    matriz.append("\t")
    matriz.append("\t")
    i+=1
i=0
matriz[0]="\t" #Este cambiar por dias
for j in range(1,numero_dias+1):
        matriz.append(j)


#matriz[1]=matriz[2]=matriz[3]="\tDias"  #se podria cambiar el dias por numeros y el primer dias de la fila se remplaza arriba con 
#matriz[1].append(Dias)
while i<40:  #hacer que se repita con formula i+=n y hacer while haciendo que matriz se genere
    print(f"{matriz[i]} {matriz[i+1]} {matriz[i+2]} {matriz[i+3]} ")
    i+=4
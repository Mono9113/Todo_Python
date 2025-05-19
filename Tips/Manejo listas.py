#Generacion de matrtiz nxn
l=[["Fila 1 =",1,2,3,4],["Fila 2 =",1,2,3,4],["Fila 3 =",1,2,3,4],["Fila 4 =",1,2,3,4],["","","","",""]]
print(len(l))
i=0
while i<len(l):
    j=0
    print("")
    while j<len(l):
        print(l[i][j],end=" ")
        j+=1
    i+=1

#Tabla de doble entrada
titulo="Plan de fabricacion"
filas="Tipos de poleras"
columnas="Dias"
print(f"*************{filas}**************")
nf=int(input(f"Cantidad de {filas}: "))
nc=int(input(f"Cantidad de {columnas}: "))
matriz=[nf],[nc]

#Leer una lista desde el valor dado 
i=1   
while i<len(matriz):
    print(matriz[i])
    i+=1

#Matriz
#****************************************************
matriz=[]
i=0
while i<10:
    n1=1
    matriz.append(f"Tipo polera ")   #Se podria definir variable tipo n que sea un input que sea tanto como para matriz como para tipo polera
    matriz.append("\t0")  #Se podria multipicar esa matriz por la cantidad de n
    matriz.append("\t0")
    matriz.append("\t0")
    i+=1
i=0
matriz[0]="\t" #Este cambiar por dias
matriz[1]=matriz[2]=matriz[3]="\tDias"  #se podria cambiar el dias por numeros y el primer dias de la fila se remplaza arriba con 
#matriz[1].append(Dias)
while i<40:  #hacer que se repita con formula i+=n y hacer while haciendo que matriz se genere
    print(f"{matriz[i]} {matriz[i+1]} {matriz[i+2]} {matriz[i+3]} ")
    i+=4
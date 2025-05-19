def plan():
    nt=int(input("Ingrese cantidad de tipos de poleras: "))
    nd=int(input("Ingrese cantidad de numero de dias: "))
    lp=[]
    for i in range(1,nt +1):
        nombre=f"Tipo polera {i}"
        cantidades=[0]*nd
        lp.append([nombre]+cantidades)
    d="Dia:\t".ljust(12)+" ".join(str(i).ljust(4)for i in range(1,nd+1))
    print(d)
    for listas in lp:
        alineado=listas[0]+" ".join(str(x).ljust(4) for x in listas [1:])
        print(alineado)

def pxd():
    precio=[]
    for i in range (1,nt+1):
        print(f"Tipo de polera {i}")
        print("")
        pxd=[]
        for j in range (1,nd+1):
            precio=int(input(f"Ingrese precio de polera tipo {i} para el dia {j}: "))
            pxd.append(precio)
        precio.append(pxd)
#*******************************************************************************************

print("MENU")
print("SISTEMA DE PLANIFICACION DE FABRICACION DE POLERAS")
print("1. Genrerar plan de fabricacion.")
print("2. Ingresar cantidad y precio de fabricacion por tipo de polera y dia.")
print("3. Visualizar el ingreso total de un tipo de polera especifica.")
print("Visualizar el iungreso total de todos los tipos de poleras en un dia especifico.")
print("Salir del programa.")
op=int(input("Ingrese su opcion: "))

if op==1:
    plan()
if op==2:
    pxd()
if op==3:
    a
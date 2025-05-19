# precio=[]
# for i in range (1,nt+1):
#     pxd=[]
#     for j in range (1,nd+1):
#         precio=int(input(f"Ingrese precio de polera tipo {i} para el dia {j}: "))
#         pxd.append(precio)
#     precio.append(pxd)
nt = []
nd=[]
precios=[]
def plan():
    nt=int(input("Ingrese cantidad de tipos de poleras: "))
    nd=int(input("Ingrese cantidad de numero de dias: "))
    lp=[]
    for i in range(1,nt +1):
        nombre=f"Tipo polera {i}  "
        cantidades=[0]*nd
        lp.append([nombre]+cantidades)
    d="Dia:\t".ljust(12)+" ".join(str(i).ljust(4)for i in range(1,nd+1))
    print(d)
    for listas in lp:
        alineado=listas[0]+" ".join(str(x).ljust(4) for x in listas [1:])
        print(alineado)
        return
def pxd():
    global nt
    global nd
    for t in range(1,nt+1):
        print(f'\nTipo polera {t}')
        for d in range(1,nd+1):
            while True:
                cantidad = int(input(f'Ingrese cantidad de poleras a fabricar en el día {d}: '))
                if 100 <= cantidad <= 5500:
                    nd.append(cantidad)
                    break
                else:
                    print('Error, la cantidad de poleras debe estar entre 100 y 5500.')
        precio = float(input(f'Ingrese el precio de este tipo de polera: '))
        precios.append(precio)
        return

    # precio=[]
    # for i in range (1,nt+1):
    #     print(f"Tipo de polera {i}")
    #     for j in range (1,nd+1):
    #         cantidad=int(input(f"Ingrese cantidad para el dia {j}: "))
    #         precio.append(precios)


    # precio=[]
    # for i in range (1,nt+1):
    #     print(f"Tipo de polera {i}")
    #     print("")
    #     pxd=[]
    #     for j in range (1,nd+1):
    #         precio=int(input(f"Ingrese precio de polera tipo {i} para el dia {j}: "))
    #         pxd.append(precio)
    #     precio.append(pxd)


plan()
pxd()
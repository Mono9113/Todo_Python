candidatos= [('Farkas','F'),('Boris','B'),('Profe de progra','P')]
votos=[('I','BFBBBFFPPFP'),('II','PPBFFBBFP'),('RM','PPPFFBBPFP')]

def local(region,votos):
    for reg, p in votos:
        if reg==region:
            CF=CB=CP=0
            for letra in p:
                if letra == 'F':
                    CF+=1
                if letra == 'B':
                    CB+=1
                if letra == 'P':
                    CP+=1
            if CF >= CB and CF>= CP:
                return 'F'
            if CB >= CF and CB>= CP:
                return 'B'
            else:
                return 'P'
    return None
def ganador(candidatos,votos):
    TF=TB=TP=0
    for _, p in votos:
        for letra in p:
            if letra =='F':
                TF+=1
            elif letra =='B':
                TB+=1
            elif letra =='P':
                TP+=1
    if TF >= TB and TF>= TP:
        MV='F'
    if TB >= TF and TB >= TP:
        MV='B'
    if TP >= TF and TP >= TB:
        MV='P'
    for nombre, a in candidatos:
        if a == MV:
            return nombre
    

print(local('I',votos))
print(local('II',votos))
print(local('III',votos))
print(local('RM',votos))

print(ganador(candidatos,votos))

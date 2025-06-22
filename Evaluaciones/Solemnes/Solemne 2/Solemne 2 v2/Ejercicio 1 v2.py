equipos= [('Equipo A','A'),('Equipo B','B'),('Equipo C','C')]
goles=[('Region 1','BACABBC'),('Region 2','CCAABBBA'),('Region N','CABBACB')]

def local(region,goles):
    for reg,i in goles:
        if reg==region:
            GA=GB=GC=0
            for letra in i:
                if letra=='A':
                    GA+=1
                if letra=='B':
                    GB+=1
                if letra=='C':
                    GC+=1
            if GA >= GB and GA>= GC:
                return 'A'
            elif GB > GA and GB >= GC:
                return 'B'
            else:
                return 'C'
    return None
def ganador(equipos,goles):
    TA=TB=TC=0
    for _ , i in goles:
        for letra in i:
            if letra == 'A':
                TA+=1
            if letra == 'B':
                TB+=1
            if letra == 'C':
                TC+=1
        if TA >= TB and TA >= TC:
            Goleador='A'
        elif TB >= TA and TB >= TC:
            Goleador='B'
        else:
            Goleador='C'
    for nombre, i in equipos:
        if i == Goleador:
            return nombre

print(local('Region 1',goles))
print(local('Region 2',goles))
print(local('Region 3',goles))
print(local('Region N',goles))
print(ganador(equipos,goles))
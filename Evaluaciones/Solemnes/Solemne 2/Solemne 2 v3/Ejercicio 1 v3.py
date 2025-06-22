personajes=[("Deadpool","D"),("Coloso","C"),("Negasonic","N")]
chistes=[("Escena 1","DCNDCDCD"),("Escena 2","DNDDCDD")]

def local(escena,chistes):
    for esc,p in chistes:
        if esc==escena:
            CD=CC=CN=0
            for letra in p:
                if letra=="D":
                    CD+=1
                if letra=="C":
                    CC+=1
                if letra=="N":
                    CN+=1
            if CC<=CD>=CN:
                return "D"
            elif CD<=CC>=CN:
                return "C"
            else:
                return "N"
    return None
def ganador(personajes,chistes):
    TD=TC=TN=0
    for _ , i in chistes:
        for letra in i:
                if letra=="D":
                    TD+=1
                if letra=="C":
                    TC+=1
                if letra=="N":
                    TN+=1
        if TC<=TD>=TN:
            MC="D"
        elif TD<=TC>=TN:
            MC= "C"
        else:
            MC= "N"
    for nombre,a in personajes:
        if a == MC:
            return nombre

print(local("Escena 1",chistes))
print(local("Escena 2",chistes))
print(local("Escena 3",chistes))
print(ganador(personajes,chistes))


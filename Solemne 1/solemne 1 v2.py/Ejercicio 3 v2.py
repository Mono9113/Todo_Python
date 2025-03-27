# altura=float(input("Ingrese la altura que lanzara la pelota en Mts: "))
# altura_f=altura
# alt_max_rebote=0
# botes=0
# while altura_f>=0.03:
#     alt_max_rebote=altura_f-(altura_f*(5/7))
#     altura_f=alt_max_rebote
#     botes+=1
#     print(f"la altura de lanzamiento es {altura} metros y dio {botes} botes en total.")
# if altura_f >=0.03:
#     print(f"La cantidad total de bote es: {botes}")

altura=float(input("Altura de lanzamiento dew la pelota en Mts: "))
saltos=0
while altura>0.03:
    print(f"Altura: {round(altura,2)} bote: {saltos}")
    altura*=5/7
    if altura>0.03:
        saltos+=1
print(f"Cantidad de botes {saltos}")
ar=int(input("Eliga donde va a atajar [1--6]: "))
ju=int(input("Eliga donde va a lanzar [1--6]: "))
if ar==ju:
    print("LA PARO EL PORTEROOOOOOOO!!!!")

else:
    print("GOOOOOOOOOOOOL")
    if (ar!=ju)and (ju==1)or(ju==6):
        print("El gol fue por la derecha")
    if (ar!=ju)and (ju==2)or(ju==5):
        print("El gol fue por el centro")
    if (ar!=ju)and (ju==3)or(ju==4):
        print("El gol fue por la Izquierda")
        

# ar = int(input("Eliga donde va a atajar [1--6]: "))
# ju = int(input("Eliga donde va a lanzar [1--6]: "))

# if ar == ju:
#     print("LA PARO EL PORTEROOOOOOOO!!!!")
# else:
#     print("GOOOOOOOOOOOOL")
#     if ju in [1, 6]:
#         print("El gol fue por la derecha")
#     elif ju in [2, 5]:
#         print("El gol fue por el centro")
#     elif ju in [3, 4]:
#         print("El gol fue por la Izquierda")
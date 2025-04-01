#Determino las variables e introduccion de datos del libro
isbn=input("Ingrese ISBN del libro: " )
titulo=input("Ingrese Titulo del libro: ")
tapa=int(input("Ingrese el tipo de la portada: \n1.Suave \n2.Dura \nOpcion: "))
pag=int(input("Ingrese Cantidad de paginas: "))
pre_tap=0
pre_pag=0
desc_total=0

#Introduccion y presentacion de datos entregados
print("*******************************")
print("DATOS DEL LIBRO")
print(f"ISBN del libro: {isbn}")
print(f"Titulo del libro: {titulo}")
#Condicion para eleccion de tipo de portada y precio asociado
if tapa==1:
    print(f"Tipo de portada: {tapa} --- Suave")
    pre_tap=10000
elif tapa==2:
    print(f"Tipo de portada:{tapa} ---- Dura")
    pre_tap=15000
print(f"Cantidad de paginas del libro: {pag} ")
print("RESULTADOS:")
pre_pag=pag*10
#Descuentos aplicados asociados a cantidad de paguinas y total del valor de la compra
if pag < 500:
    print(f"Costo del libro: {pre_tap+pre_pag}")
    print("Descuento del libro: 0")
    print(f"Precio Total del libro: {pre_tap+pre_pag}")
    print("****************************************")
if pag>=500 and pag<=1000:
    print(f"Costo del libro: {pre_tap+pre_pag}")
    desc_total=(pre_tap+pre_pag)*0.03
    print(f"Descuento del libro: {desc_total}")
    print(f"Precio Total del libro: {(pre_tap+pre_pag)-desc_total}")
    print("****************************************")
if pag>=1001 and pag<=2000:
    print(f"Costo del libro: {pre_tap+pre_pag}")
    desc_total=(pre_tap+pre_pag)*0.07
    print(f"Descuento del libro: {desc_total}")
    print(f"Precio Total del libro: {(pre_tap+pre_pag)-desc_total}")
    print("****************************************")
if pag>2000:
    print(f"Costo del libro: {pre_tap+pre_pag}")
    desc_total=(pre_tap+pre_pag)*0.09
    print(f"Descuento del libro: {desc_total}")
    print(f"Precio Total del libro: {(pre_tap+pre_pag)-desc_total}")
    print("****************************************")
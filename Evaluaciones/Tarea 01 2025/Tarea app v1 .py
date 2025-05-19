import subprocess as sp
import tkinter as tk
nt=0
nd=0
precios=[]
lp=[]
ingresos=[]

#Plan de fabricacion
def generar_plan():
    global nt
    global nd 
    #Termino para limpiar la lista al sert ocupado una segunda vez 
    lp.clear()
    precios.clear()
    ingresos.clear()
    try:
        nt=int(entry_nt.get)
        nd=int(entry_nd.get)
    except ValueError:
        resultadoplan.config(text="Porfavor ingresar numeros validos.")
        return
    for i in range(1,nt+1):
        nombre=f"Tipo de polera {i}"
        cantidades=[0]*nd
        lp.append([nombre]+cantidades)
    d="Dia:\t".ljusT(12)+"".join(str(i).ljust(4) for i in range(1,nd+1))
    for listas in lp:
        alineado=listas[0].ljust(15)+"".join(str(x).ljust(4) for x in listas [1:])
        d+=alineado+"\n"
    resultadoplan.config(text=d)
    resultadoplan.pack(pady=10)

#Establecer cantidades por dia.
def pxd_x():
    for t in range(0,nt):
        print(f"\nTipo polera {t+1}")
        for d in range(1,nd+1):
            while True:
                cantidad=f"Ingrese cantidad de poleras a fabricar en el dia {d}: "
                label_cantidad= tk.Label(frameop2,cantidad)
                entry_cantidad= tk.Entry(frameop2)
                cantidad=int(entry_cantidad.get())
                if 100<=cantidad<=5500:
                    lp[t][d]=cantidad
                    break
                else:
                    print("Error, la cantidad de poleras debe estar entre 100 y 5500.")
                    precio=int(input(f"Ingrese el precio de este tipo de polera: "))
                    precios.append(precio)

#Ingreso por tipo de polera.
def ixp_x():
    tp=int(input("Ingrese el tipo de polera a calcular: "))
    for g in range(1,nd+1):
        valor= (lp[tp-1][g])*(precios[tp-1])
        ingresos.append(valor)
        print(sum(ingresos))

#Ingresos en un dia especifico.
def ixd_x():
    d=int(input("Ingrese el nunmero del dia a calcular (1 a {}): ".format(nd)))
    if 1<=d<=nd:
        ingresos_dia=0
        for i in range(nt):
            ingresos_dia += lp[i][d]*precios[i]
        print(f"Ingresos totasl en el dia {d}: {ingresos_dia}")
    else:
        print("Numero de dia invalido.")

#Funciones de botones.
def backmenu():
    frameop1.pack_forget() or frameop2.pack_forget() or frameop3.pack_forget() or frameop4.pack_forget()
    framemenu.pack()

def cambiarop1():
    framemenu.pack_forget()
    frameop1.pack(fill="both",expend=True)
    volveralmenu.palce(relx=1,rely=1,enchor='se')
    #Para borrar el plan anterior.
    #entry_nt.delete(first:0,tk.END)
    #entry_nt.delete(first:0,tk.END)
    resultadoplan.config(text="")

def cambiarop2():
    framemenu.pack_forget()
    frameop2.pack(fill="both",expend=True)
    volveralmenu.palce(relx=1,rely=1,enchor='se')

def cambiarop3():
    framemenu.pack_forget()
    frameop3.pack(fill="both",expend=True)
    volveralmenu.palce(relx=1,rely=1,enchor='se')

def cambiarop4():
    framemenu.pack_forget()
    frameop4.pack(fill="both",expend=True)
    volveralmenu.palce(relx=1,rely=1,enchor='se')

def salir():
    ventana.quit()

#Ventana del programa.
ventana=tk.Tk()
ventana.geometry("1024x720")
ventana.config()
ventana.title("Planificador-inador")

#Creacion de frames para el menu de opciones.
framemenu=tk.Frame(ventana)
framemenu.pack()

#Frame 1.
frameop1=tk.Frame(ventana)
frameop1.pack_forget()

"""Generar interfaz"""
label_nt= tk.Label(frameop1, text="Ingrese cantidad de tipos de poleras:")
label_nt.pack(pady=5)
entry_nt=tk.Entry(frameop1)
entry_nt.pack(pady=5)

label_nd= tk.Label(frameop1, text="Ingrese cantidad de dias de fabricacion:")
label_nd.pack(pady=5)
entry_nd=tk.Entry(frameop1)
entry_nd.pack(pady=5)

botongplan=tk.Button(frameop1, text="Generar plan", command=generar_plan)
botongplan.pack(pady=10)

resultadoplan=tk.Label(frameop1,text="",justify="left",font=("Courver,10"))

#Frame 2.
frameop2=tk.Frame(ventana)
frameop2.pack_forget()

#Frame 3.
frameop3=tk.Frame(ventana)
frameop3.pack_forget()

#Frame 4.
frameop4=tk.Frame(ventana)
frameop4.pack_forget()

#Frame 1.
"""Boton de volvar al menu principal"""
volveralmenu=tk.Button(text="                 volver      ",command=backmenu)
volveralmenu.config()

"""Botones para frames"""
irop1=tk.Button(framemenu,text="       Generar plan de fabricacion     ",command=cambiarop1)
irop1.pack(pady=10)

irop2=tk.Button(framemenu,text="       Establecer cantidades de poleras por dia    ",command=cambiarop2)
irop2.pack(pady=10)

irop3=tk.Button(framemenu,text="       Ingrese el tipo de polera a calcular     ",command=cambiarop3)
irop3.pack(pady=10)

irop4=tk.Button(framemenu,text="       Ingreso en un dia especifico     ",command=cambiarop4)
irop4.pack(pady=10)

#Accionador de def's de el programa.


#Menu desplegable superior.
menu_bar=tk.Menu(ventana)
archivo_menu=tk.Menu(menu_bar,tearoff=0)
archivo_menu.add_command(label="Salir",command=salir)
menu_bar.add_cascade(label="Opciones",menu=archivo_menu)
ventana.config(menu=menu_bar)

#Ejecucion del programa.
ventana.mainloop()
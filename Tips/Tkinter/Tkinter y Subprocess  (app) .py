import subprocess as sp
import tkinter as tk

def open_paint():
    c_paint="mspaint.exe"
    try:
        resul=sp.run(c_paint, check=True)
        print("Paint abierto con éxito.")
    except sp.CalledProcessError as e:
        print(f"Error al abrir Paint: {e}")
    except FileNotFoundError:
        print("No se encontró ms.paint.exe. Asegurece de tenerlo instalado.")

def open_notepad():
    sp.run("notepad")

def salir():
    ventana.quit()

#***********************
ventana=tk.Tk()
ventana.title("Gestor de aplicaciones.")
ventana.geometry("300x200")
ventana.resizable()
inicio=tk.Label(ventana,text="Eliga que aplicacion que desea abrir")
inicio.config(font=("Courier",16,"bold"))
inicio.config(bg="grey")
inicio.place(x=10,y=10) #Da un lugar específico
boton1=tk.Button(ventana,text="Paint",command=open_paint)
boton1.config(bg="green")
boton1.place(x=10,y=40)
boton2=tk.Button(ventana,text="notepad",command=open_notepad)
boton2.config(bg="green")
boton2.place(x=10,y=70)
ventana.configure(bg='grey')

#************************
menu_bar=tk.Menu(ventana)
archivo_menu=tk.Menu(menu_bar,tearoff=0)
archivo_menu.add_command(label="Salir",command=salir)
menu_bar.add_cascade(label="Opciones",menu=archivo_menu)
ventana.config(menu=menu_bar)

ventana.mainloop()

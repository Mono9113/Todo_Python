import tkinter as tk
from tkinter import Menu

# Paleta corporativa
bg_color = "#F4F4F4"
text_color = "#2D2D2D"
title_color = "#005B96"
primary_button_color = "#005B96"
secondary_button_color = "#D6D6D6"
hover_color = "#007ACC"
border_color = "#B0B0B0"

root = tk.Tk()
root.title("Sistema de planificación de fabricación de poleras")
root.configure(bg=bg_color)
root.geometry("800x600")

# Menú
menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menú", menu=file_menu)
file_menu.add_command(label="Salir", command=root.quit)

# Título
title = tk.Label(root, text="Sistema de planificación de Fabricación de poleras",
bg=bg_color, fg=title_color, font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Instrucciones
instructions = (
    "Este es un sistema para planear la fabricación de poleras. A continuación usted observará las instrucciones:\n\n"
    "1. Cada botón es una opción del menú. El primero (azul) genera la matriz (se reinicia cada vez).\n"
    "2. Los botones grises sirven para editar el planificador.\n"
    "3. Si no encuentra el botón de volver, lo puede ubicar en el menú desplegable (esquina superior izquierda)."
)

label_instr = tk.Label(root, text=instructions, bg=bg_color, fg=text_color, justify="left", font=("Arial", 10))
label_instr.pack(pady=10, padx=20, anchor="w")

# Función para crear botones con estilo
def create_button(root,text, bg, fg, command=None):
    btn = tk.Button(root, text=text, bg=bg, fg=fg, font=("Arial", 10, "bold"),
                    relief="flat", activebackground=hover_color, padx=10, pady=5, command=command)
    btn.pack(pady=8, padx=20, anchor="w")
    return btn

# Botones
btn1 = create_button("Generar plan de fabricación", primary_button_color, "white")
btn2 = create_button("Establecer cantidades de poleras por día", secondary_button_color, text_color)
btn3 = create_button("Ingrese el tipo de polera a calcular", secondary_button_color, text_color)
btn4 = create_button("Ingreso en un día específico", secondary_button_color, text_color)

root.mainloop()

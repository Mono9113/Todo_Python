import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

def on_resize(event):
    # Reubica el botón en la esquina inferior derecha
    btn.place(x=event.width - 0, y=event.height - 0)  # Ajusta tamaño del botón

# Botón que se moverá
btn = tk.Button(root, text="Aceptar", width=12)
btn.place(x=394,y=335)  # Posición inicial

# Evento que se llama cada vez que se redimensiona la ventana
root.bind("<Configure>", on_resize)

root.mainloop()


# Establecer cantidades por dia.
def pxd_x():
    for t in range(0, nt):
        print(f"\nTipo polera {t + 1}")
        for d in range(1, nd + 1):
            # Crear un Label y Entry para cada día
            cantidad_label = tk.Label(frameop2, text=f"Ingrese cantidad de poleras a fabricar en el dia {d}:")
            cantidad_label.pack()
            entry_cantidad = tk.Entry(frameop2)
            entry_cantidad.pack()
            
            # Esperar a que el usuario ingrese la cantidad
            ventana.wait_window(entry_cantidad)  # Esperar a que se complete la entrada
            
            try:
                cantidad = int(entry_cantidad.get())
                if 100 <= cantidad <= 5500:
                    lp[t][d] = cantidad
                else:
                    print("Error, la cantidad de poleras debe estar entre 100 y 5500.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

# Función para cambiar a la opción de ingresar producción
def cambiarop2():
    framemenu.pack_forget()
    frameop2.pack(fill="both", expand=True)
    pxd_x()  # Llamar a la función para establecer cantidades

# Actualizar el botón en el menú
irop2 = boton1(framemenu, "Ingresar producción por tipo y día", "#D6D6D6", "#2D2D2D", cambiarop2)
irop2.place(x=20, y=350)

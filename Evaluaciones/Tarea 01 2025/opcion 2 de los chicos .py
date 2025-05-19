tipos = int(input('Ingrese el número de tipos de poleras: '))
dias = int(input('Ingrese el número de días de fabricación: '))
fabricaciones = []
precios = []

for t in range(tipos):
    print(f'\nTipo polera {t+1}')
    cantidad_poleras = []
    for d in range(dias):
        while True:
            cantidad = int(input(f'Ingrese cantidad de poleras a fabricar en el día {d+1}: '))
            
            if 100 <= cantidad <= 5500:
                cantidad_poleras.append(cantidad)
                break
            else:
                print('Error, la cantidad de poleras debe estar entre 100 y 5500.')
    fabricaciones.append(cantidad_poleras)
    precio = float(input(f'Ingrese el precio de este tipo de polera: '))
    precios.append(precio)

print('Plan de fabricación')
print('*')
for i in range(tipos):
    print(f'Tipo polera {i+1:<3}      ', end='')
    for cantidad in fabricaciones[i]:
        print(f'{cantidad:<8}', end='')
    print()
print('*')
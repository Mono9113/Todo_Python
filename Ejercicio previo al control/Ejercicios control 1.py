"""En un circuito electro hay tres interruptores, los cuales pueden estar en estado cerrado (1) o abierto (0).
Para que un equipo funcione, se requiere que al menos dos estén cerrados. Si los datos son el estado de los interruptores, determine si el equipo funcionará."""

i1= int(input("Interruptor 1: 1 (apagado) o 0 (encendido): "))
i2= int(input("Interruptor 2: 1 (apagado) o 0 (encendido): "))  
i3= int(input("Interruptor 3: 1 (apagado) o 0 (encendido): "))
if (i1==1 and i2==0 and i3==0) or (i1==0 and i2==1 and i3==0) or (i1==0 and i2==0 and i3==1):
    print("Maquina encendida")
else:
    print("Maquina apagada")

# i1 = int(input("Interruptor 1: 1 (cerrado) o 0 (abierto): "))
# i2 = int(input("Interruptor 2: 1 (cerrado) o 0 (abierto): "))
# i3 = int(input("Interruptor 3: 1 (cerrado) o 0 (abierto): "))

# cerrados = i1 + i2 + i3
# if cerrados >= 2:
#     print("Equipo funcionando")
# else:
#     print("Equipo no funcionando")
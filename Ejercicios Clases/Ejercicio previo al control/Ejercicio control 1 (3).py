"""Un almacén rebaja 10% del precio de un producto si se adquieren más de 20 unidades y 5% si adquieren hasta 20 unidades, pero más de 10, no hay descuento para cantidades menores o iguales a 10 unidades
Con el precio unitario del producto y al cantidad adquirida, realice un algoritmo para mostrar el valor a pagar."""
print("Chocolates: $1500")
desc=0
prod=int(input("Ingrese cantidad de producto: "))
if prod <= 21:
    desc=int((prod+1500)*0.10)
    print("Total con descuento: $",(1500*prod)-desc)
elif prod <=20 and prod >=10 :
    desc=int((prod+1500)*0.05)
    print("Total con descuento: $",(1500*prod)-desc)
elif prod<=10:
    print("Total a pagar: ",1500*prod)
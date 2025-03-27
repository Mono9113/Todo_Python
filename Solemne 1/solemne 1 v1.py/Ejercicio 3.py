"""Las ecuaciones de Lotka-Volterra describen como cambian las poblaciones de dos especies en un ecosistema, en el que una
de ellas es depredadora de la otra. En un dia cualquiera, y representa el numero de depredadores (por ejemplo, lobos),
x el numero de presas (por ejemplo, conejos), y el cambio de estas cantidades de un dia para el otro estan dados por las
ecuaciones:
dx = x (a - b y)
dy = -y (c - d x)
donde a, b, c y d son parametros que dependen de las caracteristicas del ecosistema y dx y dy representan el crecimiento
de las poblaciones en cada iteracion. Para que el modelo funcione, x e y deben ser tratados como numeros reales, no como
enteros.
Suponga que en un ecosistema inicialmente hay x = 300 conejos e y = 600 lobos, y que la dinamica del sistema es descrita
por los valores a = 3 x 10-3, b = 8 x 10-5, c = 5 x 10-3 y d = 6 x 10-6. Los conejos se extinguiran en 195 dias.
Escriba un programa en Python solicite la cantidad de conejos y de lobos y muestre en cuantos dias se extinguiran los
conejos (es decir, x < 1)."""
a=3e-3
b=8e-5
c=5e-3
d=6e-6
x=int(input("Cuantos conejos hay: "))
y=int(input("Cuantos lobos: "))
dias=0
dx=0
dy=0
while x>1:
    dx =x*(a - (b*y))
    dy= -y*(c-(d*x))
    x+=dx
    y+=dy
    dias+=1
print(f"Los conejos se extinguiran en {dias} dias.")
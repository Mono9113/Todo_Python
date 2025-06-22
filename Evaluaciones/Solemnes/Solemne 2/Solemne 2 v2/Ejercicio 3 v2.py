def sqrt(n):
    return n**0.5

def cuadratica(a,b,c):
    Np= b**2-4*a*c
    if Np < 0:
        return "Error: No existe solucion en los numeros reales."
    raiz = sqrt(Np)
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    return f"El valor de x1 = {x1:.2f}  y x2 = {x2:.2f}"

def main():
    a=int(input("Ingrese valor de a: "))
    b=int(input("Ingrese valor de b: "))
    c=int(input("Ingrese valor de c: "))
    resultado=cuadratica(a,b,c)
    print(resultado)

main()
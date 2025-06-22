def calcular_potencia(base,exponente):
    resul=base**exponente
    return resul

def aproximar_logaritmo(N,x):
    suma=0
    for n in range(1,N+1):
        signo = (-1)**(n+1)
        numerador=calcular_potencia(x-1,n)
        termino=signo*numerador/n
        suma+=termino
    return suma

def main():
    N=int(input("Ingrese el numero del termino N: "))
    x=float(input("Ingrese el valor de x (>0): "))
    if x <= 0: 
        print("X debe sert mayor a 0 para calcular ln(x).")
    resultado= aproximar_logaritmo(N,x)
    print(f"La aproximacion de ln({x}) con N={N} es: {resultado:.6f}")

main()

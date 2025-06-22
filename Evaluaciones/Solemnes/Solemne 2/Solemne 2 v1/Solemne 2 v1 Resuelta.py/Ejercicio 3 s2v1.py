def factorial(x):
    resultado=1
    for i in range (1,x+1):
        resultado *=i
    return resultado
def nEuler(n):
    e=1
    for x in range (1,n+1):
        e+=1 / factorial(x)
    return e
def main():
    n=int(input("Ingrese el valor de N para aproximar a e: "))
    resultado=nEuler(n)
    print(f"La aproximacion de e con N: {n} es {resultado:.10f}")

main()
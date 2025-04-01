p=1
s=2
dif=s-p
e=s
i=2
while dif>0.00001:
    f=1
    fac=1
    while f<=i:
        fac=fac*f
        f=f+1
    print(f"{i} factorial= {fac}")
    s=e+1/fac
    dif=s-e
    print(s)
    e=e+1/fac
    i+=1
print(f"Euler= {e}")

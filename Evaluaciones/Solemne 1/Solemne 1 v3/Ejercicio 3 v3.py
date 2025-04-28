euler=1
i=1
dif=1
fact=1
while dif >=0.001:
    fact*=i
    num_act=1/fact
    euler+= num_act
    i+=1
    fact*=i
    num_sig=1/fact
    dif= num_act - num_sig

print(euler)
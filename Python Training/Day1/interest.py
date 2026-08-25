def SimpleInterest(principle, rate , time):
    return ((principle*rate*time)/100)


def CompoundInterest(principle, rate , time):
    return (((principle*(1+rate/100)**2)-principle)*time)



u_principle=int(input("Enter principle : "))
u_rate=float(input("Enter rate : "))
u_time= int(input("Enter number of years : "))

print(f"The simple interest is {SimpleInterest(u_principle,u_rate,u_time)}")
print(f"The Compound interest is {CompoundInterest(u_principle,u_rate,u_time)}")


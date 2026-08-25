even=[]
odd=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(f"The even numbers are : {even}")
print(f"The odd numbers are : {odd}")
print(f"sum of even: {sum(even)}")
print(f"avg of even: {sum(even)/len(even)}")
print(f"sum of odd : {sum(odd)}")
print(f"avg of odd: {sum(odd)/len(odd)}")

print(f"The sum of even and odd is : {sum(even)+sum(odd)}")
print(f"The count of even and odd is : {len(even)} and {len(odd)}")
print(f"The average of even and odd is : {(sum(even)+sum(odd))/(len(even)+len(odd))}")
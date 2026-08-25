marks=[]

for i in range (1,6):

    mark=int(input(f"Enter marks for subject {i} :"))
    marks.append(mark)


print(f"The sum is : {sum(marks)}")
print(f"The average is : {sum(marks)/len(marks)}")
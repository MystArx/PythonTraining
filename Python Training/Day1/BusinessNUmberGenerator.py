for i in range(1,501):
    if i%6==0:
        print("Skipping number divisible by 6")
        continue
    if i%41==0:
        print("Breaking the loop as number is divisible by 41")
        break
    if i%2!=0:
        print(i)
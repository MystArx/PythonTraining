while True:
    amount=int(input("Enter purchase amount : "))
    if amount<0:
        print("INVALID INPUT!")
        break
    if amount==0:
        print("Skipping 0")
        continue
    if amount>1000:
        print(f"Amount : {amount}")
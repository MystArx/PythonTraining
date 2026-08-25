def generateIDs(num):
    ids = []
    for i in range(num):
        if i%5==0:
            print("Maintainence ID , Skipped")
            continue
        if i==37:
            print("Reached 37, stopping ID generation.")
            break
        ids.append(i)
        if i>20:
            print(f"Generated Id : {i} ")  

          
    return ids

generateIDs(50)
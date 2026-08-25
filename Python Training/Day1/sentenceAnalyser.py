sentence=input("Enter a sentence: ")
for ch in sentence:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            print(f"{ch} is a vowel")
        else:
            print(f"{ch} is a consonant")
    elif ch==" ":
        continue
    elif ch=="!":
        break
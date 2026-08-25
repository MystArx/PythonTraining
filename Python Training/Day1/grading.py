def validatemarks(marks):
    if marks < 0 or marks > 100:
        return False
    else:
        return True


def grade(marks):
    if marks<40:
        return "Fail"
    elif marks<60:
        return "C"
    elif marks<75:
        return "B"
    elif marks<95:
        return "A"
    else:
        return "S"


marks=int(input("Enter marks : "))
if validatemarks(marks):
    print(f"Grade : {grade(marks)}")
else:
    print("Invalid marks")
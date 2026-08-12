age = int(input("Enter age: "))

if age < 24:
    student = input("Is student?: ")
    if student == "yes":
        print("APPROVED")
    else:
        print("DENIED")

elif age > 60:
    credit = input("Is credit rating excellent?: ")
    if credit == "yes":
        print("APPROVED")
    else:
        print("DENIED")

else:
    print("APPROVED")
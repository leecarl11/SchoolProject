mark=int(input("Enter student mark: "))

if mark >= 70 and 100:
    print("A")
elif mark >= 60 and 69:
    print("B")
elif mark >= 50 and 59:
    print("C")
elif mark >= 40 and 49:
    print("D")
elif mark >= 30 and 39:
    print("E")
elif mark >= 20 and 29:
    print("F")
else:
    print("Invalid input. Please enter a numeric value.")

operator=input("Enter an operator(+-*/): ")
num1=float(input("Enter a number: "))
num2=float(input("Enter a number: "))
if operator=="+":
    print(round(num1+num2,5))
elif operator=="-":
    print(round(num1-num2,5))
elif operator=="*":
    print(round(num1*num2,5))
elif operator=="/":
    print(round(num1/num2,5))
else:
    print("You entered an invalid operator! ")
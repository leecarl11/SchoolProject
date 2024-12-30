
def factorial_number():

    n=int(input("enter a whole number: "))
    fact=1
    for factorial in range(n,1,-1):
        fact=fact*factorial
    print("(The factorial of", n, "is", fact)

factorial_number()
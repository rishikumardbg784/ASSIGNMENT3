def fact(n):
    if n < 2:
        return 1

    return n *(fact(n-1))
n=int(input("Enter a number: "))
result=fact(n)
print("Factorial of",n,"is",result)
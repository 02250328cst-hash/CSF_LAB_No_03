def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function
number = int(input("Enter a number: "))
fact = factorial(number)
print("The factorial of", number, "is:", fact)
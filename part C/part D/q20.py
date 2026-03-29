# Define the function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function
number = int(input("Enter a number: "))
result = check_even_odd(number)
print("The number", number, "is", result)
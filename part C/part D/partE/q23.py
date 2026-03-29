def print_even_odd(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is Even")
        else:
            print(i, "is Odd")

# Call the function
number = int(input("Enter a number: "))
print_even_odd(number)
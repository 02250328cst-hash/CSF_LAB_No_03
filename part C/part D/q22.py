def multiplication_table(num):
    print("Multiplication table of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Call the function
number = int(input("Enter a number: "))
multiplication_table(number)
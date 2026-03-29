n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a number greater than 0")
else:
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print("The sum of numbers from 1 to", n, "is:", total)
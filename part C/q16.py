numbers = [2 , 4, 6, 8, 10]
search_num = int(input("Enter the number to search: "))

found = False

for num in numbers:
    if num == search_num:
        found = True
        print(search_num, "found in the list!")
        break

if not found:
    print(search_num, "not found in the list.")
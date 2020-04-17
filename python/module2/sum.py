number_list = [int(input("Please enter a number: "))]

while sum(number_list) != 0:
    try:
        i = int(input("Please enter a number: "))
    except ValueError:
        print("This is not a number")
        continue
    number_list.append(i)
    # print(sum(number_list))
else:
    print([s**2 for s in number_list])



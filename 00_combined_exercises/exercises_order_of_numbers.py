while True:

    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter a number: "))
    third_number = int(input("Enter a number: "))

    number_list = [first_number, second_number, third_number]

    ascending_numbers = number_list.sort()
    descending_numbers = number_list.sort(reverse=True)

    print(ascending_numbers)
    print(descending_numbers)


# Exercise 1: Counting
def count_a_number(numbers: list, number: int):
    count = 0
    for i in numbers:
        if i == number:
            count += 1
    return count

print("Occurence of the number in the list of numbers is: ", count_a_number([1,2,7,4,7,6,7,8,7,10],7))

# Exercise 2: Playing with lists
def play_with_lists(numbers: list, number: int):
    numbers.reverse()
    print(numbers)

    numbers[numbers.index(1)] = number
    print(numbers)

    numbers.sort(reverse=True)
    print(numbers)

play_with_lists([10101023943,8,2,1,6,4,5,6,7,3,9],7)

# Exercise 3: Comparing list elements
def compare_lists(list1: list, list2: list):
    common = []

    for i in list1:
        if i in list2:
            common.append(i)
    return common

print(compare_lists([1,2,3,4,5,6,7,8,9,10],[0]))

# Exercise 4: No duplicates!
def remove_duplicates(items: list):
    items = set(items)
    return list(items)


print(remove_duplicates(["oliver", "Hooman", "Hooman", "oliver", "item","item","item"]))

def remove_duplicates_my_way(items: list):
    common = []
    for j in items:
        for i in items:
            if i != j:
                common.append(j) if j not in common else None
    return common


print(remove_duplicates_my_way(["oliver", "Hooman", "Hooman", "oliver", "item","item","item"]))

# Exercise 5: Computer description
def describe_computer(computer= {"Type":"Unkonwn", "Brand":"Unkonwn", "Price":"Unkonwn"}):
    print(f"You Have a {computer["Type"]} from {computer["Brand"]} that costs {computer["Price"]}€.")
    computer["OS"] = "Linux"
    

my_PC = {"Type":"PC", "Brand":"HP", "Price":2000}
describe_computer(my_PC)


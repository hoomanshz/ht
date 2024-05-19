
# Exercise 1: Famous Quote
def famous_quote():
    aothor = "Mahatma Gandhi"
    quote = "Live as if you were to die tomorrow. Learn as if you were to live forever."
    print(f"{aothor} once said, '{quote}'") 

# Exercise 2: Number Eight
def number_eight():
    print(6 + 2)
    print(10 - 2)
    print(2 * 4)
    print(16 / 2)
    print(24 // 3)
    print(2 ** 3)

# Exercise 3: Formatting
def name_age ():
    name = input("What is your first name? ")
    age = input("What is your age? ")
    print("Hi {}, you are {} years old.".format(name, age))
    print(f"Hi {name}, you are {age} years old.")
    print("Hi " + name + ", you are",age, " years old.")

# Exercise 4: Swap
def swap_integers():
    x = input("Please enter x: ")
    y = input("Please enter y: ")
    print(f"x = {x}, y = {y}")

    c = x
    x =y
    y = c
    print(f"\nx after swap = {x}, y after swap = {y}")

# Exercise 5: Modulo check
def check_numbers(num_1, num_2):

    print(f"\nNumber 1: {num_1}\nNumber 2: {num_2}\n")
    devisible_by_six = num_1 % 6 == 0 or num_2 % 6 == 0
    devisible_by_ten = num_1 % 10 == 0 and num_2 % 10 == 0
    
    if devisible_by_six:
        print("Atleast one number is divisible by 6.")
    else:
        print("No number is divisible by 6.")
    
    if devisible_by_ten:
        print("Both numbers are divisible by 10.")
    else:
        print("max. one number is not divisible by 10.")    
    
    if devisible_by_ten and devisible_by_six:
        return True 

# Exercise 6: Summarizer
def sum_up(num_1, num_2):
    if num_1 > num_2:
        print("Second number should be greater than the first number!!!")
    else:
        num_list = list(range(num_1, num_2 + 1))
        print(f"\n {str(num_list)[1:-1].replace(", ", " + ")} = {sum(num_list)} \n")
    
# Exercise 7: Sequencer
def sequence(number):
    if number >= 0 and number <= 9:
        for i in range(10):
            if i != number:
                print(i, end=" ")
    else:
        print("Number should be between 0 and 9.")

# Exercise 8: String check
def check_string(text):
    if text.lower().startswith("a") or text.lower().endswith("a", "A"):
        print(True)

# Exercise 9: ASCII Art
def triangle(rows):
    for i in range(1, rows + 1):
        print("* " * i)



# Exercise 1
#famous_quote()

# Exercise 2
#number_eight()

# Exercise 3
#name_age()

# Exercise 4
#swap_integers()

# Exercise 5
#check_numbers(6, 120)

# Exercise 6
#sum_up(1, 10)

# Exercise 7
#sequence(5)

# Exercise 8
#check_string("a BananA")

# Exercise 9
triangle(4)





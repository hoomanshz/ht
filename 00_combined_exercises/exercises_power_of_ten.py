"""
Write a program that asks the user for an at max three-digit integer.
The program then shows the decomposition of the number into powers of ten.  
If the number provided is negative, print "number cannot be negative",
if the number has more than three digits, print "number has more than 3 digits". 
Hint: Use floor division (//) and modulo (%) to decompose the numbers.
E.g.: 25//10 = 2; 25%10 = 5
"""

number = int(input("Enter a number: "))

if number < 0:
    print("Number cannot be negative")
elif abs(number) > 999:
    print("Number has more than 3 digits")
else:
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    print(f"The number {number} is composed of:")
    if thousands:
        print(f"{thousands} thousands")
    if hundreds:
        print(f"{hundreds} hundreds")
    if tens:
        print(f"{tens} tens")
    if ones:
        print(f"{ones} ones")


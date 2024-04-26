
"""
def print_range(n1, n2):

    
        if n1 <= 0 or n2 <= 0:
            print("Please enter numbers greater than 0.")
            
        
        elif n2 < n1:
            print("Second number should be greater than or equal to the first number.")
            

        else:
            for i in range(n1, n2+1):
                print(i)
        
        

n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))


print_range(n1, n2)
"""



while True:
    
    n1 = int(input("Enter the first integer: "))
    n2 = int(input("Enter the second integer: "))

    if n1 <= 0 or n2 <= 0:
        print("Please enter numbers greater than 0.")
        continue
                
            
    elif n2 < n1:
        print("Second number should be greater than or equal to the first number.")
        continue       

    else:
        for i in range(n1, n2+1):
            print(i, end=" ")
        print("\n")
    
    if input("continue? (y/n): ") == "n":
        break
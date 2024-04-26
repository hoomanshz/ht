while True:

    to_be_paid = int(input("Enter the amount to be paid: "))
    if to_be_paid <= 0:
        print("Invalid input. Amounts cannot be negative or zero.")
    
    amount_received = int(input("Enter the amount received: "))
    if amount_received <= 0:
        print("Invalid input. Amounts cannot be negative or zero.")
    
    elif amount_received < to_be_paid:
        print("Amount received is too small.")
    
    else:
        change = amount_received - to_be_paid
        #print("Change:", change)
        print(f"Change: {change}")
        break

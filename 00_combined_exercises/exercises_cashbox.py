while True:
    amount_to_be_paid = int(input("Enter the amount to be paid: "))
    amount_received = int(input("Enter the amount received: "))

    if amount_to_be_paid < 0 or amount_received < 0:
        print("Invalid input. Amounts cannot be negative.")
    elif amount_received < amount_to_be_paid:
        print("Amount received is too small.")
    else:
        change = amount_received - amount_to_be_paid
        print("Change:", change)
        break
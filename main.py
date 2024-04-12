def deposit():
    while True:
        amount = input("Enter the amount to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Amount should be valid number.")
    return amount

def main():
    balance = deposit()

main()
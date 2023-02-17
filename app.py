MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input ("What would you like to deposit? :$ ")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print("Please enter a valid number!")
    return amount

def line():
    while True:
        line = input ("What line would you like to bet? : ( 1-"+ str(MAX_LINE)+ ")?")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print("Please enter a valid number!")
        else:
            print("Please enter a valid number!")
    return line 

def bet():
    while True:
        amount = input("What would you like to bet?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number!")


def main():
    balance = deposit()
    lines = line()
    bet = bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} line. Total bet is equal to: ${total_bet}")
    print(balance, lines)


main()
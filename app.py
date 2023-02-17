import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

# Dari sini harus dipelajarin lebih lanjut karena logic nya sangat kompleks dan harus paham
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.item():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# sampai sini

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
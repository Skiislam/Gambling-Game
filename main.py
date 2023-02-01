import random as rand

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.item():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = [[], [], []]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = rand.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

def deposit():
    while True:
        amount = input("Please Enter the amount you want to deposit? $")
        if amount.isdigit(): #making sure they entered a valid number
            amount = int(amount) #changing the string into amount.
            if amount > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("Please enter a numner")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #making sure they entered a valid number
            lines = int(lines) #changing the string into amount.
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a numner")
    return lines

def get_bet():
    while True:
        betAmount = input("Please enter how much you want to bet on each line? $")
        if betAmount.isdigit(): #making sure they entered a valid number
            betAmount = int(betAmount) #changing the string into amount.
            if MIN_BET <= betAmount <= MAX_BET:
                break
            else:
                print("Bet is to large! Please enter a valid amount")
        else:
            print("Please enter a number")
    return betAmount

def main():
    userBalance = deposit()
    lines = get_number_of_lines()
    while True:
        userBet = get_bet()
        total_bet = lines * userBet
        if(total_bet > userBalance):
            print("You dont have enough to bet that amount")
            print("Please Enter a valid bet amount!")
        else:
            break
    print('You are betting ' + str(userBet) + ' on ' + str(lines) + ' lines. Total bet is equal to: $' + str(total_bet))

main()

    

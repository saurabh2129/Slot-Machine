import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLUMNS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(cols, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = cols[0][line]
        for column in cols:
            symbol_to_check = cols[line]
            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    cols = []
    for col in range(columns):
        colm = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            colm.append(value)
        
        cols.append(colm)

    return cols

def print_slot_mahine(cols):
    for row in range(len(cols[0])):
        for i, colm in enumerate(cols):
            if i != len(cols) -1:
                print(colm[row], end= "|")
            else:
                print(colm[row], end="")

        print()  


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 $.")
        else:
            print("Please enter a valid amount")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print("Lines must be in between 1 to 3.")
        else:
            print("Please enter a valid number of lines")

    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet must be in between 1 to 100 $.")
        else:
            print("Please enter a valid bet amount")

    return bet


def spin(balance):
    line = get_number_of_lines()
    while True:
        bets = get_bet()
        total_bet = bets * line

        if total_bet > balance:
            print(f'You do not have enough money to bet that amount, your current balance is {balance}$')
        else:
            break

    print(f'You are betting ${bets} on {line} lines. Total bet is equal to: ${total_bet}')
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_mahine(slots)
    winnings, winning_lines = check_winnings(slots, line, bets, symbol_value)
    print(f'You won ${winnings}')
    print(f'You won on lines: ', *winning_lines)
    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answers = input("Press enter to play (q to quit):  ").lower()
        if answers == 'q':
            break
        balance += spin(balance)

    print(f'You left with ${balance}')
    

main()
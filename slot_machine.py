MAX_LINES = 3 #constant value
MAX_BET = 100 #establishes max number of plays
MIN_BET = 1 #establishes min number of plays

def deposit(): #user input
    while True:
        amount = input('What is your deposit? $') #input deposit to play
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.') #error if entered 0
        else:
            print('Please enter a number.') #error if input is not a number
    return amount

def get_lines(): 
    while True:
        lines = input('Enter lines to bet on (1-' + str(MAX_LINES) + '? $') #enter number of lines 1-3
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.') #error if entered 0
        else:
            print('Please enter a number.') #error if input is not a number
    return lines

def main():
    balance = deposit() #runs deposit function
    lines = get_lines()
    print(balance, lines)
main()

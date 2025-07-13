from handler import round_handler
from globals import *

def main_menu():
    while True:
        global HIGH_SCORE
        global GUESS_LIMIT
        global WORD_LIST
        global ENDLESS_ON
        HIGH_SCORE = 0
        print('>Main Menu:')
        print('1. One Run')
        print('2. Endless Mode (No Lose)')
        print('3. Settings')
        print('4. Quit')
        choice = input("Command: ")
        valid_choices = ['1', '2', '3', '4']
        if choice in valid_choices:
            if choice == '1':
                round_handler(False)
            elif choice == '2':
                round_handler(True)
            elif choice == '3':
                settings_menu()
            elif choice == '4':
                print('Thank you for playing!')
                return           
        else:
            print('ERROR: Invalid Choice')
            continue

def settings_menu():
    while True:
        global GUESS_LIMIT
        global WORD_LIST
        global HIGH_SCORE
        global ENDLESS_ON
        print('>Settings Menu:')
        print('1. Add Words')
        print('2. Guess Limit')
        print('3. Return')
        choice = input("Command: ")
        valid_choices = ['1', '2', '3']
        if choice in valid_choices:
            if choice == '1':
                player_word = input("Word to add: ")
                WORD_LIST.append(player_word.upper())
                print(f"DEBUG: {WORD_LIST}")
                continue
            elif choice == '2':
                player_guess = input("Guess Limit: ")
                try:
                    int(player_guess)
                except ValueError:
                    print("ERROR: Needs Integer")
                    continue
                if int(player_guess) < 1:
                    print('ERROR: Invalid Choice')
                    continue
                else:
                    GUESS_LIMIT = int(player_guess)
                    print(f"DEBUG: {GUESS_LIMIT}")
                    continue
            elif choice == '3':
                return
        else:
            print('ERROR: Invalid Choice')
            continue

## >Settings Menu: <--- Menu Loop
## 1. Add Words <--- Add to list? Dictionary? Function call for this. Global Variable.
## 2. Guess Limit <--- Global Variable
## 3. Return <--- Self Explanatory
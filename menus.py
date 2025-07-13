from handler import round_handler

def main_menu():

    SETTINGS = {
        'GUESS_LIMIT': 3,
        'WORD_LIST': ['BIKE', 'MISCHIEF', 'LUNATIC', 'GOOFBALL'],
        'HIGH_SCORE': 0
    }
    
    while True:
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
                round_handler(False, SETTINGS)
            elif choice == '2':
                SETTINGS['HIGH_SCORE'] = 0
                round_handler(True, SETTINGS)
            elif choice == '3':
                settings_menu(SETTINGS)
            elif choice == '4':
                print('Thank you for playing!')
                return           
        else:
            print('ERROR: Invalid Choice')
            continue

def settings_menu(SETTINGS):
    while True:
        print('>Settings Menu:')
        print('1. Add Words')
        print('2. Guess Limit')
        print('3. Return')
        choice = input("Command: ")
        valid_choices = ['1', '2', '3']
        if choice in valid_choices:
            if choice == '1':
                player_word = input("Word to add: ")
                SETTINGS['WORD_LIST'].append(player_word.upper())
                print(f"DEBUG: {SETTINGS['WORD_LIST']}")
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
                    SETTINGS['GUESS_LIMIT'] = int(player_guess)
                    print(f"DEBUG: {SETTINGS['GUESS_LIMIT']}")
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
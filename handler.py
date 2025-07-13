import random
from menus import *


def round_handler(is_endless, SETTINGS):
    
    GUESS_LIMIT = SETTINGS['GUESS_LIMIT']
    WORD_LIST = SETTINGS['WORD_LIST']
    HIGH_SCORE = SETTINGS['HIGH_SCORE']

    STORED_VARIABLES = {
        'ENDLESS_ON': False,
    }



    if is_endless == True:
        STORED_VARIABLES['ENDLESS_ON'] = True
    random_word = WORD_LIST[random.randint(0,(len(WORD_LIST) - 1))]
    split_word = list(random_word)
    asterisks = ""
    round_count = 0
    for i in range(len(random_word)):
        asterisks += "*"
    split_asterisks = list(asterisks)
    while True:
        if round_count >= GUESS_LIMIT:
            print(f"You lose. The word was: {random_word}")
            STORED_VARIABLES['ENDLESS_ON'] == False
            break
        round_count += 1
        print(f"Your word is: {"".join(split_asterisks)}")
        print(f"You are on: {round_count} of {GUESS_LIMIT} guesses.")
        player_input = input("Guess: ")
        split_input = list(player_input.upper())[:len(random_word)]
        for i in range(0, (len(split_input))):
            if split_input[i] == split_word[i]:
                split_asterisks[i] = split_word[i]
        if split_asterisks == split_word:
            print(f"You win! The word was: {random_word}")
            if STORED_VARIABLES['ENDLESS_ON'] == True:
                SETTINGS['HIGH_SCORE'] += 1
                print(f"You have won: {SETTINGS['HIGH_SCORE']} games in a row.")
                print("===========================================")
                round_handler(True, SETTINGS)
            break
        elif round_count <= GUESS_LIMIT:
            continue
        else:
            break
    return          

    ### Reasoning Model ###
    ## [W|O|R|D]
    ## [*|*|*|*]
    ## [0|1|2|3]
    ## Comparison happens here...
    ## Player Input: .upper() -> .split() -> comparison

    # Produce Random Word
    # Produce * = Length Word
    # Loop # of Guesses, Replacing *'s with correct positional letters.
    # Return True or False, store value in Endless Mode.
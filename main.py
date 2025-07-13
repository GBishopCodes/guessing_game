##
## Game Idea: [Dictionary Guesser]
## Word of any length: dispalyed as ******
## Guess the word in so many guesses
## ----
## Settings Explained:
## Guess Limit: Any
## Guess word: Any characters that match, replace ******s with character
## ====
## Features Explained:
## One Run: Do a single game, win or lose.
## Endless Mode (No Lose): Play until you lose a round.
## Settings: Opens settings, returns to menu with return.
## ----
## UI:
## ----
## >Settings Menu: <--- Menu Loop
## 1. Add Words <--- Add to list? Dictionary? Function call for this. Global Variable.
## 2. Guess Limit <--- Global Variable
## 3. Return <--- Self Explanatory
## ----
## >Main Menu: <--- Menu Loop
## 1. One Run <--- Round Handler Function
## 2. Endless Mode (No Lose) <--- Round Hanlder Function Looped Until Failure, Return Score
## 3. Settings <--- Starts Settings Loop
## 4. Quit <-- Exits Program
##
import random
from globals import *
from menus import main_menu

main_menu()

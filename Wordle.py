########################################
# Name: Sage Soto
# Collaborators (if any): N/A
# GenAI Transcript (if any):
# Estimated time spent (hr): 
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")
        word_to_row("flame", 0)
        word_from_row(1)
       # if_word_in_list()

    def if_word_in_list(word:str):
        if word in ENGLISH_WORDS and len(word) == 5:
            gw.show_message("Word is in the list")
        else:
            gw.show_message("Not in list")
        
    def word_to_row(word:str,row:int):
        col = 0
        for index in range(0, len(word)):
            gw.set_square_letter(row,col,word[index])
            col += 1
        gw.show_message("The word is flame")
        
    def word_from_row(row:int)-> str:
        col = 0
        word = ""
        for index in range(5):
            word += str(gw.get_square_letter(row,col))
            col += 1
        return row
        gw.show_message("placeholder")
            
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    Guess = "Flame"
    guess = Guess.lower()
    GUESS = Guess.upper()
    print(Guess, Guess in ENGLISH_WORDS) # Hello False
    print(guess, guess in ENGLISH_WORDS) # hello True
    print(GUESS, GUESS in ENGLISH_WORDS) # HELLO False
    
    #gw.set_square_letter(0,0,GUESS[0])
    #gw.set_square_letter(0,1,GUESS[1])
    #gw.set_square_letter(0,2,GUESS[2])
    #gw.set_square_letter(0,3,GUESS[3])
    #gw.set_square_letter(0,4,GUESS[4])


# Startup boilerplate
if __name__ == "__main__":
    wordle()

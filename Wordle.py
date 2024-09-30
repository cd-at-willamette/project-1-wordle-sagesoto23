########################################
# Name: Sage Soto
# Collaborators (if any): N/A
# GenAI Transcript (if any): What function is used to create a list for a string?
# Estimated time spent (hr): About 6 hours (total combined time of this project)
# Description of any added extensions: Will look into more extensions if time available
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():                                               
    # The main function to play the Wordle game.
    gw = WordleGWindow()                                    # Defines the graphics window for Wordle 
    correct_word = random.choice(ENGLISH_WORDS)             # A word is randomly chosen from ENGLISH_WORDS for each game
    while len(correct_word) != 5:                           # While loop that makes sure the word chosen
        correct_word = random.choice(ENGLISH_WORDS)         # is 5 letters long
    print(correct_word)                                     # Prints out the random word
    word_list = str(correct_word.upper())                   # Makes all words in ENGLISH_WORDS capitalized
    not_in_list = list(word_list.upper())                   # The correct order of indexes in the correct word
    
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        row = gw.get_current_row()                                  # Defining the current row the player is on
        guess = ""                                                  # Player's guess is initially an empty string
        for index in range(N_COLS):                                 # For an index in each column
            letter = gw.get_square_letter(row,index)                # Defines each letter in each square
            guess += letter                                         # Letters are added to the guess
        if is_english_word(guess) and len(guess) == 5:              # If the player guesses an english word that is five letters long
            for index in range(N_COLS):                             
                if guess[index] == word_list[index]:                # If a guess has the correct letter(s) and correct spot(s)
                    gw.set_square_color(row,index,CORRECT_COLOR)    # Color the square(s) green
                    not_in_list[index] = "0"                        # Makes letters in the word list a 0 to replace the found letter(s) 
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),index),CORRECT_COLOR)            # Also colors the letter key(s)
            for index in range(N_COLS):                                                                         
                if guess[index] != word_list[index]:                                                            # If a guess doesn't have correct letters
                    letter_key = gw.get_key_color(gw.get_square_letter(gw.get_current_row(),index))             # Defines each letter key as a variable 
                    if guess[index] in word_list and guess[index] in not_in_list:                               # If the guess has the correct letter(s) but not correct spot(s)
                        gw.set_square_color(gw.get_current_row(),index,PRESENT_COLOR)                           # Color the sqaures yellow
                        if letter_key != CORRECT_COLOR:                                                         # If the letter keys are not green
                            gw.set_key_color(gw.get_square_letter(gw.get_current_row(),index),PRESENT_COLOR)    # Change their color to yellow
                        not_in_list[not_in_list.index(guess[index])] = "0"                                      # Identifies correct letter(s) and turns into 0
                    else:                                                                                       # If the guess doesn't have correct letters
                        gw.set_square_color(row,index,MISSING_COLOR)                                            # Color the squares grey
                        if letter_key != CORRECT_COLOR and PRESENT_COLOR:                                       # If the letter keys aren't green or yellow
                            gw.set_key_color(gw.get_square_letter(gw.get_current_row(),index),MISSING_COLOR)    # Change their color to grey
            if guess == word_list:                                                            # If the guess equals the correct word
                gw.show_message("Congrats! You guessed the correct word!")                    # The player wins the game
                gw.set_current_row(N_ROWS)                                                    # Player can no longer enter letters
            elif gw.get_current_row() == 5:                                                   # If the player guesses five times
                gw.show_message(f"Out of tries! The correct word was {correct_word}")         # The player loses the game and are told the correct word
            elif gw.get_current_row() < 5:                                                    # If the player has under 5 guesses
                next_row = row + 1                                                            # Variable that defines moving rows
                gw.set_current_row(next_row)                                                  # They move to the next row and their next guess                           
        else:                                                                                 # If the player guesses a word not in english or in gibberish
            gw.show_message("Not a word in the list")                                         # The game tells them it is not a word
    gw.add_enter_listener(enter_action)                                                       # Pressing enter will tell Wordle what to do next
                    

    # Below is testing for capitalized and lowercase letters in a word
    Guess = "Tests"
    guess = Guess.lower()
    GUESS = Guess.upper()
    print(Guess, Guess in ENGLISH_WORDS) # Prints False
    print(guess, guess in ENGLISH_WORDS) # Prints True
    print(GUESS, GUESS in ENGLISH_WORDS) # Prints False

# Startup boilerplate
if __name__ == "__main__":
    wordle()

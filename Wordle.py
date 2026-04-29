# AT3 - Wordle
#
# Author: Vincent La Mela-Ryoo
# Student ID: 20169610
#
# Course: ICTPRG302
# Lecturer: Maryam Shahabi

# TODO: Add Import statements (if needed)

# Variables and Constants
# TODO: Define Constants

# TODO: Define Variables
DEBUG = True

# Application Functions
# TODO: Score Guess Function
def score_guess(guess_word, target_word):
    score = []
    for letter in target_word:
        score.append(0)
    return(score)

# TODO: Read File Into Word List Function

# TODO: Display Greeting Function
def show_greeting():
    print("Welcome")

# TODO: Display Instructions Function
def show_instructions():
    print("Instructions")

# TODO: Any Optional Additional Functions 

# TODO: Play Game Function
def play_game():
    print('Playing the game')

#TODO: Testing Function
def test_game():
    print('Testing the game')
    # Test Case 1
    ## Arrange
    guess_word = 'hello'
    target_word = 'train'
    
    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print('Score:', score, 'Expected:', [0, 0, 0, 0, 0])

#TODO: Main Program
if DEBUG == True:
    test_game()
else:
    play_game()

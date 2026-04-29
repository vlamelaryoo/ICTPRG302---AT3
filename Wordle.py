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
# Score Guess Function
def score_guess(guess_word, target_word):
    score = []
    for letter in target_word:
        score.append(0)
    if guess_word == target_word:
        score = [2, 2, 2, 2, 2]
    else:
        for letter in range(len(target_word)):
            if guess_word[letter] == target_word[letter]:
                score[letter] = 2
            elif guess_word[letter] in target_word:
                score[letter] = 1
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

    #Test Case 2
    ## Arrange
    guess_word = 'hello'
    target_word = 'hello'

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print('Score:', score, 'Expected:', [2, 2, 2, 2, 2])

    #Test Case 3
    ## Arrange
    guess_word = 'world'
    target_word = 'hello'

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print('Score:', score, 'Expected:', [0, 1, 0, 2, 0])

#TODO: Main Program
if DEBUG == True:
    test_game()
else:
    play_game()


# AT3 - Wordle
#
# Author: Vincent La Mela-Ryoo
# Student ID: 20169610
#
# Course: ICTPRG302
# Lecturer: Maryam Shahabi

# Import Statements
import random

# Variables and Constants
# Constants

# Variables
DEBUG = False

# Application Functions

# Greeting Function
def show_greeting():
    user_name = input(str('Enter your name: '))
    print('\nHello', user_name + '. Welcome to Wordle!')

# Rules Function
def show_instructions():
    print('\nThe game rules are:')
    print('Guess the randomly chosen 5 letter word.')
    print('You will have 6 attempts.')
    print('Your guesses must be a valid 5 letter word.')
    print('Invalid guesses will not consume a guess attempt.')
    print('After a guess, your word and each letter in it will scored:')
    print(' - If a letter is in the word and in the correct posotion, a O will be displayed.')
    print(' - If a letter is in the word but is in the incorrect position, a ? will be displayed.')
    print(' - If a letter is not in the word, a - will be displayed.')
    print('If you guess the chosen word, you win!')
    print('If you run out of guesses, you lose.')


# Read File Into Word List Function
def read_words_from_file(filename):
    word_list = []
    word_list = open(filename).read().splitlines()
    return(word_list)

"""Reads a file and creates a list of lines in it without newline characters.

Arguments
---------
filename (file): The file to be converted into a list

Returns
-------
word_list: A list of lines in the file without newline characters

Examples
--------
>>> all_words_list = read_words_from_file('all_word.txt')
>>> print(all_word_list[:5])
>>> ['aahed', 'aalii', 'aargh', 'aarti', 'abaca']

>>> target_words_list = read_words_from_file('target_words.txt')
>>> print(target_words_list[-5:])
>>> ['young', 'youth', 'zebra', 'zesty', 'zonal']
"""

# Select Random Word From List Function
def random_word(word_list):
    chosen_word = random.choice(word_list)
    return(chosen_word)

"""Chooses a random item from a list.

Arguments
---------
word_list: A list from which the random item will be chosen (in this case a list of words)

Returns
-------
chosen_word: The randomly chosen word

Examples
--------
>>> chosen_word = random_word(target_words_list)
>>> print(chosen_word)
>>> shear

>>> chosen_word = random_word(target_words_list)
>>> print(chosen_word)
>>> salsa
"""

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
            else:
                continue
    return(score)

"""Scores the user's guess against the target word

Arguments
---------
guess_word (str): The word the user has guessed.
target_word (str): The word the guess is being checked against

Returns
-------
score: List representing the score assigned to each letter in guess_word
0 if letter is not present in target_word
1 if letter is present in target_word in a different position
2 if letter is present in target_word in the same position

Examples
--------
>>> score = score_guess('world', 'hello')
>>> print(score)
>>> [0, 1, 0, 2, 0]

>>> score = score_guess('blank', 'blind')
>>> print(score)
>>> [2, 2, 0, 2, 0]
"""

# Readable Score Display Function
def display_score(score, guess_word):
    score_output = []
    guess_output = []
    for symbol in score:
        if symbol == 0:
            score_output.append('-')
        elif symbol == 1:
            score_output.append('?')
        elif symbol == 2:
            score_output.append('O')
    for letter in guess_word:
        guess_output.append(letter.upper())
    print('')
    print(' '.join(score_output))
    print(' '.join(guess_output))

"""Displays the user's guess and its assigned score in a more readable manner.

Arguments
---------
score: the score that was assigned to the user's guess
guess_word: the word that the user guessed

Returns
-------
print function of score_output above guess_output

Examples
--------
>>> display_score([0, 1, 0, 2, 0], 'world')
>>> - ? - O -
>>> W O R L D

>>> display_score([2, 2, 2, 0, 0], 'helps')
>>> O O O - -
>>> H E L P S
"""

# Post-Win Replay Function
def replay():
    replay_question = input('\nWould you like to play again? (yes/no): ').lower()
    while True:
        if replay_question == 'yes':
            print('\nOkay! New word selected!')
            play_game()
        elif replay_question == 'no':
            print('\nOkay! Goodbye!')
            break
        else:
            print('\nSorry, I did not understand that.')
            replay()

"""Allows the user to restart the game after winning or end the program.

The function has no arguments and does not return anything.
It either runs the play_game() function again, or it stops.
"""

# Play Game Function
def play_game():

    # Create lists of all words and target words
    all_words_list = read_words_from_file('all_words.txt')
    target_words_list = read_words_from_file('target_words.txt')

    # Randomly choose a target word
    target_word = random_word(target_words_list)

    # Set number of attempts taken to 0
    attempts_remaining = 6

    # Ask user to guess target word, then validate it, score it and respond
    while attempts_remaining > 0:
        guess_word = str(input('\nGuess the word (type "help" to view the rules or "restart" to restart): ')).lower()
        if guess_word == 'help':
            show_instructions()
        elif guess_word == 'restart':
            print('\nOkay! New word selected.')
            play_game()
        elif guess_word in all_words_list:
            score = score_guess(guess_word, target_word)
            display_score(score, guess_word)
            if score == [2, 2, 2, 2, 2]:
                print('\nWell done! You got it!')
                replay()
                break
            else:
                attempts_remaining = attempts_remaining - 1
                print('\nYou have', str(attempts_remaining), 'guesses left.')
        else:
            print('\nThat word is not valid, try again.')
            continue

    # End game if no attempts remaining and offer user to replay
    print('\nMaximum number of guesses reached. The word was:', target_word)
    replay()

"""The main game function.

This function incorporates and uses the following other functions:
read_words_from_file()
random_word()
score_guess()
display_score()
replay()

The function does not return anything.
It results in the user winning or losing the game and being offered to replay.
"""

# Testing Function
def test_game():
    print('\nTesting the game')
    # Test Case 1
    ## Arrange
    guess_word = 'hello'
    target_word = 'train'
    #  
    ## Act
    score = score_guess(guess_word, target_word)
    #
    ## Assert
    #print('Score:', score, 'Expected:', [0, 0, 0, 0, 0])

    #Test Case 2
    ## Arrange
    guess_word = 'hello'
    target_word = 'hello'
    #
    ## Act
    score = score_guess(guess_word, target_word)
    #
    ## Assert
    #print('Score:', score, 'Expected:', [2, 2, 2, 2, 2])

    #Test Case 3
    ## Arrange
    guess_word = 'world'
    target_word = 'hello'
    #
    ## Act
    score = score_guess(guess_word, target_word)
    #
    ## Assert
    #print('Score:', score, 'Expected:', [0, 1, 0, 2, 0])

    #Test Case 4
    ## Arrange
    all_words_filename = 'all_words.txt'
    #
    ## Act
    all_words_list = read_words_from_file(all_words_filename)
    #
    ## Assert
    #print('Got:', all_words_list[:5], 'Expected:', ['aahed', 'aalii', 'aargh', 'aarti', 'abaca'])
    
    #Test Case 5
    ## Arrange
    target_words_filename = 'target_words.txt'
    #
    ## Act
    target_words_list = read_words_from_file(target_words_filename)
    #
    ## Assert
    #print('Got:', target_words_list[-5:], 'Expected:', ['young', 'youth', 'zebra', 'zesty', 'zonal'])

    #Test Case 6
    for count in range(3):
        chosen_word = random_word(target_words_list)
        print(chosen_word)

    #Test Case 7
    ## Arrange
    guess_word = 'world'
    target_word = 'hello'
    #
    ## Act
    score = score_guess(guess_word, target_word)
    display_score(score, guess_word)

# Main Program
# Enter debug mode if enabled
if DEBUG == True:
    test_game()
else:
    # Display greetings and welcome user
    show_greeting()

    #Ask user if they would like to see the rules before starting the game
    while True:
        ask_for_instructions = input('\nWould you like to see the rules before playing? (yes/no) ')
        if ask_for_instructions == 'yes':
            show_instructions()
            play_game()
        elif ask_for_instructions == 'no':
            print('\nOkay, good luck!')
            play_game()
        else:
            print('\nSorry, I did not understand that')
            continue

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

"""Scores the user's guess against the target word.

Arguments
---------
guess_word (str): The word the user has guessed.
target_word (str): The word the guess is being checked against.

Returns
-------
score: List representing the score assigned to each letter in guess_word.
0 if letter is not present in target_word
1 if letter is present in target_word in a different position.
2 if letter is present in target_word in the same position.

Examples
--------
>>> score = score_guess('world', 'hello')
>>> print(score)
>>> [0, 1, 0, 2, 0]

>>> score = score_guess('blank', 'blind')
>>> print(score)
>>> [2, 2, 0, 2, 0]
"""

# TODO: Read File Into Word List Function
def read_words_from_file(filename):
    word_list = []
    word_list = open(filename).read().splitlines()
    return(word_list)

"""Reads a file and creates a list of lines in it without newline characters.

Arguments
---------
filename (file): The file to be converted into a list.

Returns
-------
word_list = A list of lines in the file without newline characters.

Examples
--------
>>> all_word_list = read_words_from_file('all_word.txt')
>>> print(all_word_list[:5])
>>> ['aahed', 'aalii', 'aargh', 'aarti', 'abaca']

>>> target_words_list = read_words_from_file('target_words.txt')
>>> print(target_words_list[-5:])
>>> ['young', 'youth', 'zebra', 'zesty', 'zonal']
"""

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
    #  
    ## Act
    score = score_guess(guess_word, target_word)
    #
    ## Assert
    print('Score:', score, 'Expected:', [0, 0, 0, 0, 0])

    #Test Case 2
    ## Arrange
    guess_word = 'hello'
    target_word = 'hello'
    #
    ## Act
    score = score_guess(guess_word, target_word)
    #
    ## Assert
    print('Score:', score, 'Expected:', [2, 2, 2, 2, 2])

    #Test Case 3
    ## Arrange
    guess_word = 'world'
    target_word = 'hello'
    #
    ## Act
    score = score_guess(guess_word, target_word)
    #
    ## Assert
    print('Score:', score, 'Expected:', [0, 1, 0, 2, 0])

    #Test Case 4
    ## Arrange
    all_word_filename = 'all_words.txt'
    #
    ## Act
    all_word_list = read_words_from_file(all_word_filename)
    #
    ## Assert
    print('Got:', all_word_list[:5], 'Expected:', ['aahed', 'aalii', 'aargh', 'aarti', 'abaca'])
    
    #Test Case 5
    #
    #TODO: Set up your arrange-act-assert test case
    #Create the statement to show the last 5 words and check that they are correct
    ## Arrange
    target_words_filename = 'target_words.txt'
    #
    ## Act
    target_words_list = read_words_from_file(target_words_filename)
    #
    ## Assert
    print('Got:', target_words_list[-5:], 'Expected:', ['young', 'youth', 'zebra', 'zesty', 'zonal'])

#TODO: Main Program
if DEBUG == True:
    test_game()
else:
    play_game()

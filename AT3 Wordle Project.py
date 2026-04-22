#Vincent La Mela-Ryoo - 20169610
#ICTPRG302 - AT3 Project - Wordle Game

#Welcom the user
print('Welcome to Wordle!\n')

#Define rules to be called and displayed when needed
def rules():
    print('The game rules are:')
    print('Guess the randomly chosen 5 letter word.')
    print('You will have 6 attempts.')
    print('Your guesses must be 5 letters long and must be a valid word.')
    print('Invalid guesses will not consume a guess attempt.')
    print('After a guess, your word and each letter in it will scored:')
    print(' - If a letter is in the word and in the correct posotion, a * will be displayed.')
    print(' - If a letter is in the word but is in the incorrect position, a + will be displayed.')
    print(' - If a letter is not in the word, a - will be displayed.')
    print('If you guess the chosen word, you win!')
    print('If you run out of guesses, you lose.\n')

#Show rules before starting game
rules()

This is a case-study emulating a project requested by a client.  
The client and a senior developer provide initial instruction and answer questions as needed.  
  
The goal of the project is a create a simple, text-only clone of the game Wordle in Python to be able to better understand its logic and how it works.  

The rules for the game are:  
  * Random 5 letter long target word for each iteration of the game  
  * Users have to guess the word  
  * Six guess attempts allowed  
  * Guesses must be 5 letters long and must be a valid word  
  * After a guess, the game will score the word and its individual letters and communicate the following:  
    * If a letter is in the word and is in the correct position  
    * If a letter is in the word but is in an incorrect position  
    * If a letter is not in the word  
  * If all letters are correct after a guess, the guess is correct and the user wins  
  * If user does not win in six guesses, they lose and can no longer play and the game tells them what the word was
  
The game should have go through the following steps:  
  * When user begins, show a help message – explaining syntax and input options, help message should also be displayed if user inputs ‘help’ (case insensitive) at any time  
  * Get random target word  
  * Prompt for guess (case insensitive)  
  * Validate guess (length, in valid words), if invalid – loop back to prompt with explanation message, if valid – score the guess (assigning correct letters and letter positions)  
  * If word was completely correct, show winning message  
  * If word is not completely correct, increment guesses and loop back to prompt for guess  
  
The project should follow PEP8 standard, as should be clearly legible to anyone reading the code

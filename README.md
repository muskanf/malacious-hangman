# malacious-hangman
### My Malicious Hangman Project
In my malicious hangman project, the computer doesn’t pick a word. Instead, it eliminates all words containing the guessed letter at each step until it’s forced to pick a word and switches to regular hangman game.

### Part 1: Regular Hangman
Player agrees to a word length and number of guesses allowed.
Computer picks a secret word and writes out a dash for each letter.
Player starts guessing letters and every time they guess one letter correctly, the letter is placed on the dash or dashes where the letter should be.
Game ends when player figures out the word or runs out of guesses.
After game ends, user can choose to play again.
### Part 2: Malicious Hangman
Steps 1, 3, 4, and 5 remain the same as regular hangman.
The malicious part comes from the fact that the computer doesn’t honestly choose the word.
Instead, it eliminates all words containing the letters chosen by the player unless all remaining words contain that letter are eliminated.
In that case, computer is forced to make a choice and game resumes as in normal hangman.
### What I did
I read the file containing all words and stored them in an appropriate data structure.
I prompted the user for a number of letters and a number of guesses for the game.
I played a game of Malicious Hangman as follows:
Constructed a data structure with all the words.
Displayed dashes for all unknown letters.
Player made a guess.
Computer checked if removing all words with guessed letter will eliminate all words and had two cases:
### Case 1: Removing all words containing guessed letter will NOT eliminate all words. Computer eliminates all words containing guessed letter and informs player they guessed incorrectly.
### Case 2: Removing all words with guessed letter will eliminate all remaining words. Computer chooses a word at random and displays letter on correct dash. Game continues like normal hangman.
Repeated until player’s guesses exceed allowed guesses or player guesses all letters correctly.

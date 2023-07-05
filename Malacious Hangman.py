
import random
from collections import defaultdict
import dudraw

dudraw.set_canvas_size(400, 400)

class GenerateWord:
    def __init__(self, filename):
        self.words_by_length = defaultdict(list)
        with open(filename, 'r') as f:
            for line in f:
                word = line.strip()
                self.words_by_length[len(word)].append(word.lower())

    def choose_random_word(self, length):
        return random.choice(self.words_by_length[length])

    def get_words(self, length):
        return self.words_by_length[length]

def draw_hangman(guesses):
    
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(0.01)
    
    # draw base
    dudraw.line(0.2, 0.8, 0.2, 0.2)
    dudraw.line(0.2, 0.8, 0.5, 0.8)
    dudraw.line(0.5, 0.8, 0.5, 0.7)
    
    if guesses > 0:
        # draw head
        dudraw.circle(0.5, 0.65, 0.05)
    
    if guesses > 1:
        # draw body
        dudraw.line(0.5, 0.6, 0.5, 0.4)
    
    if guesses > 2:
        # draw left arm
        dudraw.line(0.5, 0.55, 0.45, 0.5)
    
    if guesses > 3:
        # draw right arm
        dudraw.line(0.5, 0.55, 0.55, 0.5)
    
    if guesses > 4:
        # draw left leg
        dudraw.line(0.5, 0.4, 0.45, 0.35)
    
    if guesses > 5:
        # draw right leg
        dudraw.line(0.5, 0.4, 0.55, 0.35)

def main():
    # Create a generator object using the dictionary file
    generator = GenerateWord('dictionary.txt')
    while True:
        # Get the desired word length from the user
        word_length = int(input("Please enter the number of letters: "))
        # Check if the word length is greater than the longest word in the dictionary
        if word_length > 24: # this is the longest length of the word
            # Ask the user to enter a smaller word length
            word_length = int(input("You want a really big word. Please enter the number of letters again: "))
        # Get the maximum number of guesses from the user
        max_guesses = int(input("Please enter the number of guesses: "))
        # Initialize the current word with underscores
        current_word = ['_'] * word_length
        print(' '.join(current_word))
        # Initialize the number of guesses and set of guessed letters
        guesses = 0
        guessed_letters = set()
        # Get all words of the desired length from the generator
        words = generator.get_words(word_length)

        # Keep looping until all letters are guessed or maximum number of guesses is reached
        while '_' in current_word and guesses < max_guesses:
            # Get a letter guess from the user
            user_guess = input('Please enter a letter for a guess: ').lower()
            # Check if the letter has already been guessed
            while user_guess in guessed_letters:
                print("You have already guesses that letter so Try again.")
                user_guess = input('Please enter a letter for a guess: ').lower()
            # Add the letter to the set of guessed letters
            guessed_letters.add(user_guess)

            # Get all words that contain and do not contain the guessed letter
            words_with_letter = set(word for word in words if user_guess in word)
            words_without_letter = set(word for word in words if all(letter not in word for letter in guessed_letters))
            
            
            # testing hangman
            # print(f"Words with letter: {words_with_letter}")
            # print(f"Words without letter: {words_without_letter}")

            # Check if there are no words left without the guessed letter
            if not words_without_letter:
                # Check if there are any words left with the guessed letter
                if words_with_letter:
                    print(f"Your guess is correct!")
                    # Update the current word with the correct guess
                    for i, letter in enumerate(random.choice(list(words_with_letter))):
                        if letter == user_guess:
                            current_word[i] = letter
                    print(' '.join(current_word))
                else:
                    print(f"Sorry, there are no words left that match your guesses.")
                    break
            else:
                temp_words_without_letter = set(word for word in words if all(letter not in word for letter in guessed_letters | {user_guess}))
                if not temp_words_without_letter:
                    print(f"Cannot remove any more letters without making the set empty.")
                else:
                    words = words_without_letter
                    print(f"Sorry, your guess is incorrect. You have {max_guesses - guesses} guesses left.")
                    guesses += 1 
                    print(' '.join(current_word))
                    draw_hangman(guesses)
                    dudraw.show()

        # Check if all letters have been guessed correctly
        if '_' not in current_word:
            print(f"Congratulations! You won. The word was {''.join(current_word)}.")
        elif guesses >= max_guesses:
            correct_word = random.choice(list(words))
            print(f"Sorry, you lost. The correct word was {correct_word}.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    main()





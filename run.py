import random
import os


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def rules():
    print("Welcome to Hangman!")
    print("Game rules:")
    print("1. You must guess the hidden word before you run out of tries.")
    print("2. You have 6 attempts.")
    print("3. Each incorrect letter results in the removal of one attempt.")
    print("4. Good luck!")


def get_player_name():
    player = input("What is your name? ")
    print(f"\nHello, {player}! Let's start the game!\n")


def main():
    words = [
        {'word': 'pineapple', 'hint': "It's a tropical fruit."},
        {'word': 'strawberry', 'hint': "It's a small, red fruit."},
        {'word': 'kiwi', 'hint': "It's a small, brown, and fuzzy fruit."},
        {'word': 'watermelon', 'hint': "It's a large fruit, green on the outside and red on the inside."},
        {'word': 'grape', 'hint': "It's a small, round fruit, often found in clusters."},
        {'word': 'peach', 'hint': "It's a soft fruit with a velvety skin."},
        {'word': 'avocado', 'hint': "It's a fruit with a large pit in the center."},
        {'word': 'mango', 'hint': "It's a juicy fruit with a large seed in the middle."}
    ]
    word_info = random.choice(words)
    secret_word = word_info['word'].lower()
    hint = word_info['hint']
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman 5.0!")
    print("Try to guess the hidden word. You have 6 attempts.")
    print(f"\nHint: {hint}")

    while True:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        if display_word == secret_word:
            print("Congratulations! You guessed the word correctly.")
            break

        if attempts == 0:
            print("Game over! The secret word was '{secret_word}'.")
            break

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")
            continue

        clean_screen()
        print("Welcome to Hangman 5.0!")
        print("Try to guess the hidden word. You have 6 attempts.")
        print(f"\nHint: {hint}")


# Display rules and get player name
rules()
get_player_name()

# Start the game (call the main function)
main()
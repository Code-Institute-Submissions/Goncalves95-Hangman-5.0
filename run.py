import random
import os


# Function to clean the console screen when the next atempt
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function for display a big name from the game
def display_title():
    print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░██░█░▄▄▀██░▀██░██░▄▄░██░▄▀▄░█░▄▄▀██░▀██░███░▄▄████░▄▄░██
██░▄▄░█░▀▀░██░█░█░██░█▀▀██░█░█░█░▀▀░██░█░█░███▄▄▀█▀▀█░▀▄░██
██░██░█░██░██░██▄░██░▀▀▄██░███░█░██░██░██▄░███▀▀▄█▄▄█░▀▀░██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """)


# Function for the rules presentation
def rules():
    print("Welcome to Hangman 5.0!")
    print("Game rules:")
    print("1. You must guess the hidden word before you run out of tries.")
    print("2. You have 6 attempts.")
    print("3. Each incorrect letter results in the removal of one attempt.")
    print("4. Good luck!")


# Function for get the player name
def get_player_name():
    player = input("What is your name? ")
    print(f"\nHello, {player}! Let's start the game!\n")
    return player


# Main function for the game
def main():
    # All the words the game gone display random
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
    # This status gone appear wuhen the player fail on the guess
    hangman_status = [
        """
           _____
          |     |
                |
                |
                |
                |
        """,
        """
           _____
          |     |
          O     |
                |
                |
                |
        """,
        """
           _____
          |     |
          O     |
          |     |
                |
                |
        """,
        """
           _____
          |     |
          O     |
         /|     |
                |
                |
        """,
        """
           _____
          |     |
          O     |
         /|\\    |
                |
                |
        """,
        """
           _____
          |     |
          O     |
         /|\\    |
         /      |
                |
        """,
        """
           _____
          |     |
          O     |
         /|\\    |
         / \\    |
                |
        """
    ]

    # First's prinst for appear on game menu
    display_title()
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
        # Display the Hangman status
        print(hangman_status[6 - attempts])

        if display_word == secret_word:
            print(f"Congratulations! You guessed the word correctly.")
            break

        if attempts == 0:
            print(f"Game over! The secret word was '{secret_word}'.")
            break

        # Input for the palyer put the guess letter
        guess = input("Guess a letter: ").lower()

        # IF/ELSE to check the right letter or wrong letter and a valid input
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")
            continue

        # Clean the screen dor dont appear all the diferent attempts
        clean_screen()
        display_title()
        print("Welcome to Hangman 5.0!")
        print("Try to guess the hidden word. You have 6 attempts.")
        print(f"\nHint: {hint}")

    # Play again if/else
    play_again = input("Do you want play again? (yes/no): ")

    if play_again.lower() == "yes":
        clean_screen()
        main()
    else:
        print("Thank you for playng Hangman 5.0!")


# Display rules and get player name
display_title()
rules()
get_player_name()

# Start the game (call the main function)
main()

import gspread
from google.oauth2.service_account import Credentials
from colorama import init, Fore, Back
import random
import time
import os

# Scope variabel
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman5.0')

words = SHEET.worksheet('words')

data = words.get_all_values()


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
    while True:
        player = input("What is your name?\n ")
        if player.isalpha():
            print(f"Hello, {player}! Let's start the game!\n")
            return player
        else:
            print("Please only enter letters in your name.\n")


def random_words():
    word_sheet = data[1:]
    random_word = random.choice(word_sheet)
    return random_word


# Main function for the game
def main():
    # All the words the game gone display random come from google sheet
    word_info = random_words()
    secret_word = word_info[0].lower()
    hint = word_info[1]
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

    # First's print's for appear on game menu
    display_title()
    print(f"Welcome to Hangman 5.0! {player_name}")
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

        str1 = f"Congratulations {player_name}! You guessed correctly."
        if display_word == secret_word:
            print(Back.GREEN + str1 + Back.RESET)
            break

        str2 = f"Game over {player_name}! The secret word was '{secret_word}'."
        if attempts == 0:
            print(Back.RED + str2 + Back.RESET)
            break

        # Input for the palyer put the guess letter
        guess = input("Guess a letter: ").lower()

        # IF/ELSE to check the right letter or wrong letter and a valid input
        str3 = f"You already guessed '{guess}'. Try again."
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(Fore.YELLOW + str3 + Fore.RESET)
            elif guess in secret_word:
                print(Fore.GREEN + "Correct guess!" + Fore.RESET)
                guessed_letters.append(guess)
            else:
                print(Fore.RED + "Wrong guess!" + Fore.RESET)
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")
            continue

         # Adicionar um atraso de 3 segundos antes de limpar a tela
        time.sleep(2)

        # Clean the screen dor dont appear all the diferent attempts
        clean_screen()
        display_title()
        print(f"Welcome to Hangman 5.0 {player_name}!")
        print("Try to guess the hidden word. You have 6 attempts.")
        print(f"\nHint: {hint}")

    # Play again if/else
    play_again = input("Do you want play again? (yes/no): ")

    if play_again.lower() == "yes":
        clean_screen()
        main()
    else:
        print(f"Thank you {player_name} for playng Hangman 5.0!")


# Display rules and get player name
display_title()
rules()
player_name = get_player_name()

# Start the game (call the main function)
main()

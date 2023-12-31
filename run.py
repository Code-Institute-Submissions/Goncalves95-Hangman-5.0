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
    time.sleep(0.7)
    print("Game rules:")
    time.sleep(0.7)
    print("1. You must guess the hidden word before you run out of tries.")
    time.sleep(0.5)
    print("2. You have 6 attempts.")
    time.sleep(0.5)
    print("3. Each incorrect letter results in the removal of one attempt.")
    time.sleep(0.5)
    print("4. Good luck!")


# Function for give a thanks menssage on the end
def thanks_animation():
    print(f"Thank you {player} for playing Hangman 5.0!")
    time.sleep(0.5)
    print("Come back soon!")
    time.sleep(0.5)
    print("Goodbye!")
    time.sleep(1)


# Function for get the player name
def get_player_name():
    while True:
        player = input("What is your name?\n ")
        if player.isalpha():
            print(f"Hello, {player}! Let's start the game!\n")
            return player
        else:
            print("Please only enter letters in your name.\n")


# Function to the game pick up random words on sheets
def random_words():
    word_sheet = data[1:]
    random_word = random.choice(word_sheet)
    return random_word


# Error tratment in case he can not access to sheets
word_info = random_words()
if word_info:
    secret_word = word_info[0].lower()
    hint = word_info[1]
else:
    print("Error: Unable to fetch word and hint.")
    exit()


# Function for the play again the player just can answer 'yes' or 'no'
def play_again_prompt():
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Main function for the game
def main():
    # All the words the game gone display random come from google sheet
    word_info = random_words()
    secret_word = word_info[0].lower()
    hint = word_info[1]
    guessed_letters = []
    attempts = 6
    # This status gone appear when the player fail on the guess
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
    print(f"Welcome to Hangman 5.0! {player}")
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

        str1 = f"Congratulations {player}! You guessed correctly."
        if display_word == secret_word:
            print(Back.GREEN + str1 + Back.RESET)
            break

        str2 = f"Game over {player}! The secret word was '{secret_word}'."
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
        # player guess word in one time
        elif guess.isalpha() and len(guess) > 1:
            str4 = f"Congratulations {player}! You guessed the word correctly."
            if guess == secret_word:
                print(Back.GREEN + str4 + Back.RESET)
                break
            else:
                str5 = "Wrong guess! The word is not correct."
                print(Fore.RED + str5 + Fore.RESET)
                attempts -= 1
        else:
            print("Invalid input. Please enter a single letter.")
            continue
        # Adicionar um atraso de 3 segundos antes de limpar a tela
        time.sleep(1)

        # Clean the screen dor dont appear all the diferent attempts
        clean_screen()
        display_title()
        print(f"Welcome to Hangman 5.0 {player}!")
        print("Try to guess the hidden word. You have 6 attempts.")
        print(f"\nHint: {hint}")

    # Play again if/else
    play_again = play_again_prompt()

    if play_again:
        clean_screen()
        main()
    else:
        thanks_animation()


# Display rules and get player name
display_title()
rules()
player = get_player_name()

# Start the game (call the main function)
main()

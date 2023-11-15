import random
import os


def main():
    words = [
        {'word': 'pineapple', "hint': 'It's a tropical fruit."},
        {'word': 'strawberry', "hint': 'It's a small, red fruit."},
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

    print("Welcome to Hangman!")
    print("Try to guess the hidden word. You have 6 attempts.")
    print(f"\nHint: {hint}")

    while True:
        display_word = ""
        for letter in scret_word:
            if letter in guessed_letter:
                display_word += letter
            else:
                display_word += "_"

        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        if display_word = secret_word:
            print("Congratulations! You guessed the word correctly.")
            break
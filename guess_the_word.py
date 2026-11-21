# Alandus James
# CIS256 Fall 2026
# Programming Assignment 4

import random


WORDS = [
    "engine", "garage", "piston", "wrench", "clutch",
    "brakes", "tire", "axle", "spark", "battery",
]
MAX_MISTAKES = 6


# Keep word selection separate so tests can call it without playing.
def select_word():
    return random.choice(WORDS)


# Reveal every occurrence of a guessed letter while hiding other letters.
def display_word(word, guesses):
    letters = []
    for letter in word:
        if letter in guesses:
            letters.append(letter)
        else:
            letters.append("_")
    return " ".join(letters)


# Normalize input and reject entries that should not use a turn.
def validate_guess(guess, guesses):
    guess = guess.strip().lower()
    if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
        raise ValueError("Enter one letter from A to Z.")
    if guess in guesses:
        raise ValueError("You already tried that letter.")
    return guess


# Only accepted letters missing from the word count toward the limit.
def count_wrong_guesses(word, guesses):
    wrong = 0
    for guess in guesses:
        if guess not in word:
            wrong += 1
    return wrong


# Importing this file for tests does not start the input loop.
if __name__ == "__main__":
    secret_word = select_word()
    guessed_letters = []
    mistakes = 0
    print("Garage Word Guess")
    print("Guess the car-related word. Every word has 7 letters or fewer.")
    print("You have 6 wrong guesses. Enter 'quit' to leave.")

    while mistakes < MAX_MISTAKES:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses remaining: {MAX_MISTAKES - mistakes}")
        print("Letters tried:", " ".join(guessed_letters))
        entry = input("Guess a letter: ")
        if entry.strip().lower() == "quit":
            print(f"Game ended. The word was {secret_word}.")
            break

        try:
            letter = validate_guess(entry, guessed_letters)
        except ValueError as error:
            print(error)
            continue

        guessed_letters.append(letter)
        mistakes = count_wrong_guesses(secret_word, guessed_letters)
        if letter in secret_word:
            print(f"Good guess! {display_word(secret_word, guessed_letters)}")
        else:
            print("That letter is not in the word.")

        if "_" not in display_word(secret_word, guessed_letters):
            print(f"You won! The word was {secret_word}.")
            break
    else:
        # This runs only when the loop reaches the wrong-guess limit.
        print(f"Out of guesses! The word was {secret_word}.")

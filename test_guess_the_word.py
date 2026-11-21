# Alandus James
# CIS256 Fall 2026
# Programming Assignment 4

import pytest

from guess_the_word import (
    WORDS,
    count_wrong_guesses,
    display_word,
    select_word,
    validate_guess,
)


# Check membership rather than expecting a particular random result.
def test_selected_word():
    assert select_word() in WORDS
    assert all(1 <= len(word) <= 7 for word in WORDS)


    # A correct letter is revealed without spending a wrong guess.
def test_correct_guess():
    letter = validate_guess(" A ", [])
    assert display_word("axle", [letter]) == "a _ _ _"
    assert count_wrong_guesses("axle", [letter]) == 0


# A valid but incorrect letter stays hidden and counts as one mistake.
def test_incorrect_guess():
    letter = validate_guess("z", [])
    assert display_word("axle", [letter]) == "_ _ _ _"
    assert count_wrong_guesses("axle", [letter]) == 1


    # One guess must reveal both occurrences of the same letter.
def test_repeated_letters():
    assert display_word("garage", ["a"]) == "_ a _ a _ _"


# The display follows word order, even when guesses arrive backward.
def test_letters_in_any_order():
    assert display_word("tire", ["e", "r"]) == "_ _ r e"
    assert display_word("tire", ["e", "r", "i", "t"]) == "t i r e"
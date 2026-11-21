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
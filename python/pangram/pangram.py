#!/usr/bin/python3

def is_pangram(sentence):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True

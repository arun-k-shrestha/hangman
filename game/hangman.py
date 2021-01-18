import random
from words import words
import string

def validwords(words):
    word= random.choice(words)
    while '_' in word or ' ' in word:
        word= random.choice(words)
    return word.upper()

def hangman():
    word = validwords(words)
    word_letter = set(word) # alphabet in the word
    alpha = set(string.ascii_uppercase)
    used_letter= set() # guessed alphabet

    while len(word_letter) >0:
        print("You have used these alphabets so far: ", ' '.join(used_letter))
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("Guessed letters: ", ' '.join(word_list))
        user_input = input("Guess an alphabet: ").upper()
        if user_input in alpha - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
        elif user_input in used_letter:
            print("You have used it already. Guess a different alphabet")
        else:
            print("Invalid Character. Try Again.")
    print("You guessed the word: ", word)
hangman()
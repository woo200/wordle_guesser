import random

with open("words.txt") as f:
    wordle_words = [line.rstrip().lower() for line in f]

used_letters = []
letters_in_word = []
correct_idx = []
bad_idx = []
last_guess = "crane"

print("Initial Guess: CRANE")

def in_deny(word):
    for c in used_letters:
        if c in word:
            return True
    return False

def cidx(word):
    for c in correct_idx:
        idx, cc = c
        if word[idx] != cc:
            return False
    return True

def bidx(word): # False = BAD WORD
    for c in bad_idx:
        idx, cc = c
        if word[idx] == cc:
            return False
    return True

def word_contains_letters(word):
    for c in letters_in_word:
        if c not in word:
            return False
    return True

def filter_words():
    global wordle_words
    filtered = []
    for word in wordle_words:
        if in_deny(word):
            continue
        if not cidx(word):
            continue
        if not bidx(word):
            continue
        if not word_contains_letters(word):
            continue
        filtered.append(word)
    wordle_words = filtered

def pretty_print_wordle_words(words):
    print("Available Words:")
    for word in words:
        print(f"{word.upper()}, ", end='')
    print()

def doround():
    global last_guess
    print("Use - for black, + for green and * for yellow")
    used = input("Enter Response: ")
    for i, c in enumerate(used):
        if c == "-":
            if last_guess[i] not in used_letters and last_guess[i] not in letters_in_word:
                used_letters.append(last_guess[i])
            if [i, last_guess[i]] not in bad_idx:
                bad_idx.append([i, last_guess[i]])
        if c == "+":
            if [i, last_guess[i]] not in correct_idx:
                correct_idx.append([i, last_guess[i]])
            if last_guess[i] not in letters_in_word:
                letters_in_word.append(last_guess[i])
        if c == "*":
            if last_guess[i] not in letters_in_word:
                letters_in_word.append(last_guess[i])
            if [i, last_guess[i]] not in bad_idx:
                bad_idx.append([i, last_guess[i]])
    filter_words()
    pretty_print_wordle_words(wordle_words)
    last_guess = input("Guess: ")
    print(f"NEXT GUESS: {last_guess}")
    doround()

doround()

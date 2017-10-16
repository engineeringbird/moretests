import random
import math

# make a list of words

words = [
    'lotus',
    'birdie',
    'peace',
    'bliss',
    'stars',
    'magical',
    'sparkles',
    'heart',
    'flower',
    'evergreen',
    'mountain',
    'sunshine'
]

while True:
    start = input("Would you like to play hangman? Y/n  ")
    if start.lower() == "n" or start.lower() == "no":
        break
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print('')
        # print('Strikes: {}/7').format(len(str((bad_guesses))))
        guess = input('Guess a letter:  ').lower()

        if len(guess) != 1:
            print('Please enter a single letter  ')
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print('That letter has been guessed already  ')
            continue
        elif not guess.isalpha():
            print('Letters only please  ')
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print('Great job! {} is the word!  ').format(secret_word)
                break
        else:
            bad_guesses.append(guess)
else:
    print('Too bad... The secret word was {}..').format(secret_word)





# pick a random word

# draw spaces

#take guess

# draw guessed letters and strikes

#print out win/lose

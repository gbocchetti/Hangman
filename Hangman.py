#Created by George Bocchetti on 12/03/2020
#TODO: random word from dictionary
#TODO: get a splitscreen setup with interactive console/bash on one side and file being edited on other

import requests
from random import choice

def find_all(a_str, sub):
    start = 0
    start = a_str.find(sub, start)
    occurences = []
    while start != -1:
        occurences.append(start)
        start = a_str.find(sub, start+1)
    return occurences

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = response.content.splitlines()
word = choice(words)
word = str(word, 'utf-8')

#word = list('antenna')
#print("Here's a peek: " + str(word))
word = list(word)
init_tries = 6
tries = init_tries
word_len = len(word)
word_guess = list('_' * word_len)
while(tries > 0):
    print('Word so far: ' + "".join(word_guess) + '\n')
    print('strikes remaining: ' + str(tries) + '\n')
    char_guess = input('Guess a letter: ')
    while(len(char_guess) != 1):
        char_guess = input('Guess again; must be a single letter: ')
    #print(word)
    #print(char_guess)
    if(char_guess not in word):
        tries = tries - 1
        print('Nope, better luck next time!\n')
    elif (char_guess in word_guess):
        print('Already guessed that letter!\n')
    elif (char_guess in word):
        print("Guessed a letter correctly!\n")
        instances = [i for i, x in enumerate(word) if x == char_guess]
        assert(instances),"Broke!" #instances should not be empty
        for i in instances: word_guess[i] = char_guess
        assert(char_guess in word_guess),"Didn't substitute guessed character correctly\n"
        if("_" not in word_guess):
            print("You guessed the word correctly: " + "".join(word) + "\n")
            break;
    else: assert(0), 'Huh?\n'

if(tries == 0): print("You hung the hangman! The word was: " + str(word)+ "\n")


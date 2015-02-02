# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            pass
#        else:
#                secretLetters.append(letter)
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
                return False

    return True

def getGuessedWord(secretWord, lettersGuessed):

     guessed = ''

     for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

     return guessed

def getAvailableLetters(lettersGuessed):
    import string
#    available = 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    return available

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'
        print 'Available letters', getAvailableLetters(lettersGuessed)
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:
            print 'Oops! You have already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print 'Good Guess: ', getGuessedWord(secretWord, lettersGuessed)
        else:
            guesses -=1
            lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word: ',  getGuessedWord(secretWord, lettersGuessed)
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

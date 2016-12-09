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
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret = secretWord
    missCounter = 0
    if lettersGuessed == []:
        return False
    
    elif len(secretWord) == 1:
        if secret in lettersGuessed:
            return True
        else:
            return False
    else:
        for char in lettersGuessed:
            if char in secretWord:
                secret = secret.replace(char,'')
                return isWordGuessed(secret, lettersGuessed)
            else:
                missCounter += 1
                if missCounter == len(lettersGuessed):
                    return False
                



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secret = secretWord
    missCounter = 0
    string = ''
    if lettersGuessed == []:
        for char in secretWord:
            string += ' _'
        return string
    elif len(secretWord) == 1:
        if secret in lettersGuessed:
            return secret
        else:
            return '_'
    else:
        if secret[0] in lettersGuessed:
            string = secret[0]+''
            secret = secret[1:len(secret)+1]
            return string + getGuessedWord(secret, lettersGuessed)
        else:
            secret = secret[1:len(secret)+1]
            return '_ '+getGuessedWord(secret,lettersGuessed)

#print getGuessedWord('abacaxi',['a','b','c','x','i'])

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    all_letters = string.ascii_lowercase
    if lettersGuessed == []:
        return all_letters
    for char in lettersGuessed:
        all_letters = all_letters.replace(char,'')
    return all_letters

#print getAvailableLetters(['a','e','i','o','u'])

def endGameVictory(won,secretWord):
    '''
    Given won boolen, print victory message if Won = True or Prints Failure
message and the word if win = False
'''
    if won:
        stringPrinted = 'Congratulations, you won!'
        print(stringPrinted)
    else:
        print('Sorry, you ran out of guesses. The word was '+secretWord)
        



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

            
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(len(secretWord))+' letters long')
    print('-----------')
    lettersGuessed = []
    mistakesMade = 0
    avaiableLetters = ''
    
    while True:
        print('You have '+str(  8-mistakesMade  )+' guesses left.')
        print('Available letters: '+ getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter:')
        guess = guess.lower()
        if guess in lettersGuessed:
            printedString = 'Oops! You\'ve already guessed that letter: '
            print(printedString + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        elif guess in secretWord:
            lettersGuessed.append(guess)
            printedString = 'Good guess: '
           
            print(printedString + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
            if isWordGuessed(secretWord, lettersGuessed):
                return endGameVictory(True,secretWord)
            
        else:
            lettersGuessed.append(guess)
            printedString = 'Oops! That letter is not in my word: '
            print(printedString  + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
            mistakesMade+=1
            
            if mistakesMade == 8:
                return endGameVictory(False,secretWord) 
       
 





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

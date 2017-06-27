# Problem 1
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    match = False
    for char in secretWord:
        for letter in lettersGuessed:
            if char == letter:
                match=True
                break
            else:
                match=False
        if match == False:
            return False

    return match

# result = isWordGuessed('apple',['e', 'i', 'k', 'p', 'r', 's'])
# print(result)

# Problem 2
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    result = ''
    for char in secretWord:
        if char in lettersGuessed:
            result += char
        else:
            result+='_ '
    return result

# result = getGuessedWord('apple',['e', 'i', 'k', 'p', 'r', 's'])
# print(result)

# Problem 3
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    set_from_list = set(lettersGuessed)
    no_duplicate = list(set_from_list)
    az = string.ascii_lowercase
    azList = [char for char in az]

    for letter in no_duplicate:
        azList.remove(letter)

    return ''.join(azList)

#print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

# Problem 4
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
    # Available helper function: isWordGuessed, getGuessedWord, getAvailableLetters


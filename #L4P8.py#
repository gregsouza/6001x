def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return (aStr == char)
    elif len(aStr) == 2:
        return (aStr[0] == char) or (aStr[1] == char)
    else:
        guess = int(len(aStr)/2)
        if aStr[guess] == char:
            return True
        elif aStr[guess] > char:
            return isIn(char, aStr[0:guess])
        else:
            return isIn(char, aStr[guess: len(aStr)-1])

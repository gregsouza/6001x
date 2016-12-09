def ndigits(integer):
    '''
    Given an integer, it calculates finds out how many digits
the integer have.
'''
    assert integer%1 == 0 #Confirms it is integer
    integer = abs(integer) #sign is not relevant
    if int(integer/10) == 0: #if it is a single number
        return 1
    else:
        reducedInteger = int(integer/10)
        return 1 + ndigits(reducedInteger)
        #Makes recursive call do ndigits adding the one digit removed
         
        
    

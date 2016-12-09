def nfruits(fruitDictonary, fruitStr):
    '''
    Given fruitDiconary on the form: {'A':1, 'B':2, 'C':3}, anda a string 
fruitStr of the form 'AC', updates the dictonary to {'A':0, 'B':2, 'C':3},
couting the 'fruits eaten'. Then, for each value bigger than 0, it uptadates
+1, so it becomes {'A':0, 'B':3, 'C':4}, and finally it consumes 'C':
{'A':0, 'B':3, 'C':4}

    Assumes:
    fruitsDictonary: is a Dictonary str --> int
    fruitStr: is a String

    '''
    
    stringLen = len(fruitStr)
    strCounter = 0
    #Passing through every fruit in string
    while strCounter < stringLen:
        fruit = fruitStr[strCounter]
        fruitDictonary[fruit] -= 1
        strCounter+=1
        #if he hasn't arrived in college
        if strCounter < stringLen:
            for otherFruit in fruitDictonary:
                if otherFruit != fruit:
                    fruitDictonary[otherFruit]+=1



    #search for max:
    maxFruit = 0 
    for fruit in fruitDictonary:
        if fruitDictonary[fruit]>maxFruit: #If bigger than maximum
            maxFruit = fruitDictonary[fruit] #It is new Maximum

    return maxFruit

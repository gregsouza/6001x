def flatten(aList):
    isThereList = False
    newList = []
    comparison = type(aList)
    for element in aList:
        if type(element) == comparison:
            elementSize = len(element)
            newList[len(newList):] = element
            for thing in element:
                if type(thing) == comparison:
                    isThereList = True
                    
        else:
            
            
            newList[len(newList):] = [element]
            

    if isThereList == True:
        return flatten(newList)
    else:
        return newList


aList = [[['a',['c']]],['b']]
newList = flatten(aList)
print(str(newList))

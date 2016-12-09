def f(a):
    return False

def satisfiesF(L):
    copiedL = L
    L = []
    toRemove = []
    print copiedL
    if copiedL == []:
        return 0
    for aString in copiedL:
        #print aString

        if f(aString):
            L.append(aString)
        print toRemove
            
        #print L

        
    if L == []:
        return 0
    else:
        return len(L)



L = ['b','d']

print satisfiesF(L)
print L
    

def f(a,b):
    return (a+b)

def dict_interdiff(d1,d2):
    inter = {}
    diff = {}



    for aInt in d1:
        if aInt in d2:
            elem1 = d1[aInt]
            elem2 = d2[aInt]
            result = f(elem1,elem2)
            inter[aInt] = result
        else:
            diff[aInt]= d1[aInt]

    for otherInt in d2:
        if not (otherInt in d1 or otherInt in diff):
            diff[otherInt] = d2[otherInt]
                   
    return (inter, diff)


d1 = {1: 1, 2: 2, 3: 3, 4: 4}
d2 = {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}
print(str(dict_interdiff(d1,d2)))
   

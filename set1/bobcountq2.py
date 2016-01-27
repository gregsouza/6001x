s='BOBOBOBOBOBOBOBO***'

low_string = s.lower()
bob_count = 0
counter = 0
size = len(low_string)
for char in low_string:
    if counter >= (size-2):
        break
    if char == 'b':
        compar_str = low_string[counter:counter+3]
        if compar_str == 'bob':
            bob_count+=1
    counter+=1

print('Number of times bob occurs is: '+str(bob_count))

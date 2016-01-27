s= 'AdddEdddIdddOdddU'
vowel = 'aeiou'
vowel_count = 0
low_string = s.lower()

for char in low_string:
    if char in vowel:
        vowel_count+=1
print('Number of vowels: '+str(vowel_count))

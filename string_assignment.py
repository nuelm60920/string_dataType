assignment = """
define variable and assign a string value to it.
get the last 3 letters, get first 3 alphabets. 
combine them, transform it to capital letters and reverse afterwards and
print it out without the last element.

"""


#st 1, a v, l-3 ng ind, f 3 l, l + f, r, p -1

club_name = "real madrid"

print(club_name)
last_3 = club_name[-3:]
print(last_3)

first_3 = club_name[:3]
print(first_3)

combine_both = last_3 + first_3
print(combine_both)

upper_case = combine_both.upper()
print(upper_case)
reversed_word = upper_case[::-1]
print(reversed_word)

print('.......')
without_last_letter = reversed_word[0:-1]
print(without_last_letter)

first_4 = club_name[1:4]
print('line 33:', first_4)
print(len(first_4))
print(club_name[::-1])

num = '54666'

print(num[::-1])

#range(0,5)


s = 'python'

rev =""
for i in s:
    rev = i + rev

print(rev)







'''


#hospital management
hospital = "Nuel hospital"

bed = "20 beds"

doctors = "10 doctors"

p =hospital.replace('Nuel','Chinasa')
print(p)
print(hospital.split())
'''



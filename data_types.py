animal  = 'monkey'



book_title = "dont let him"
published_date = 'Jan 03,2022'
author = "Jewell"
currency = '$'
price = 20
color = "blue"
publisher = "Michael"
pages = "he's my friend"


#print(book_title + ","+ published_date)
print(currency,price)

print(type(book_title))

upper = book_title.upper()
print(upper)
capitalize = book_title.capitalize()
#print("capitalize method:",capitalize)
print(capitalize)
username ="nuel4u"
password = "Nuel22....000"
password.lower()
book_title.center


number ='300'
print(number)
name = 'John'

number = number.replace('300','500')
print(number)
print(number.replace('300','Mary'))
print(type(number))

number = 300
print(type(number))



name = 'emmanuel\nedward'
print(len(name))

word = 'ha'
print(word*4)
print(name + word)

print(name.split(','))

print('-'.join(name))

print("first character:",name[0])

fullname = name[7]

print(name[:])
print(fullname)

#[start:end: jump]

print(name[0:14:2])
print(name[::2])
print(name[-15])

print('xap' in name)
print(name)

text = """ 
today is friDAY\n and TOMORROW \ni am going to \nvisit a friend.
hello people \nhow are YOU
"""
print(text)

print(text.swapcase())

news = "today is good {a} - and tomorrow is  {b}".format(a='easter',b='friday')
print(news)

full_name = "neul edward" 
print("-".join(full_name))

name = "-".join(full_name)
print(name)

print(len(full_name))

print(full_name.rjust(20,"-"))
print(full_name.ljust(20, "*"))

print(full_name.partition(" "))
print(full_name.partition(","))
print(full_name.split(" "))
print(full_name.partition(" "))

first_name = "mIchAeL"

print(first_name.swapcase())

text = ''' hello Nuel how are you today?
will like to come for a visit today?
tell me the time convenient for you.
hope to see you later.'''

text_1 ="""
 hello Nuel how are you today?
will like to come for a visit today?
tell me the time convenient for you.
hope to see you later.''
"""
print(text)

word ="today is a good day\n to start learning python. \ni hope you learn and \nunderstand very well."
print(word)

username ="nuel"
password ="edward"

user_info =f"my username {password} and my password is {username}"
print(user_info)

user_details = "my name is {a} and i am a software {b} and AI {c}".format(b="Nuel Edward",a="Engineer", c="Professional")
print(user_details)



greeting = "hello world"
print(len(greeting))
greeting[0]
#[start:end:step]
first = greeting[0]
print(first)
print(greeting[0:])
print(greeting[:])
print(greeting[0:7])
print(greeting[1:7])
word_split =greeting[0:8:2]
print(word_split)
print(greeting[::2])
print(greeting[-5:])

print(greeting[::-1])
print(greeting[1:-1])

email,phone_no = "nuel4xelence@gmail.com","084884984994"
print(email)
print(phone_no)
smile = "ha"

print(smile * 5)

number = "5"
print(number.zfill(5))

word = "Code"
print(word[1:5])

print("ha"*0)

h ="hello"
print("slice:",h[::-2])


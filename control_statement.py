'''
presenter = 'Nuel'
name = input('Enter your name:')

if name == presenter:
    print(f"{name} is currently presenting")

else:
    print("Incorrect name")


password = ''
if password:
    print("correct")

else:
    print("nothing")


num1 = 30
num2 = 30

if num1 != num2:
    print("they are not the same value ")

else:
    print("they have same value" )


voting_age = 18
voter_name = input("enter your name:")
age = int(input("enter your age:"))

if age >= voting_age:
    print('polling unit')
    
    print(f"{voter_name} - {age}, please proceed to vote:")

else:
    print("you are not eligible to vote")
'''

'''
teacher = input("enter your name:")
if teacher == "Nuel":
    print(f"Hello, {teacher} you are taking python programming students")

elif teacher == "Esther":
    print(f"Hello, {teacher} you are taking English students")

elif teacher == "Jerry":
    print(f"Hello, {teacher} you are taking Maths students")

elif teacher == "Mary":
    print(f"Hello, {teacher} you are taking History students")

elif teacher == "Jack":
    print(f"Hello, {teacher} you are taking javascript students")

else:
    print(f"Hello, {teacher} you are not recognized yet.\nContact the admin")
'''

"""
username ="nuel04"
password = "nuel23"

user_input = input("enter your username:")
user_password = input("enter your password:")

if not user_input:
    print("your username must not be empty!")

elif user_input == username and user_password == password:
    print(f"welcome, {user_input}")


else:
    print('everything is not correct.')
"""

number = int(input("enter a number"))
if number % 2 == 0:
    print("even number")
    
else:
    print("odd number")

num1 =100

num1 = 28
num2 = 20
if num1 > num2: print(f"{num1} is bigger than {num2}")

bigger_value = num1 if num1 > num2 else num2
print(f"{bigger_value} is bigger")
print(num1)
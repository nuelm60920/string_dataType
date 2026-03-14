
full_name = 'nuEl edwarD'


print("-".join(full_name))


print(full_name.rjust(20,'-'))
print(full_name.ljust(20, '.'))
print(full_name.partition(" "))
print(full_name.split())

number = '5'
print(number.zfill(10))

print(full_name.swapcase())

word = "today is {a} and tomorrow is {b}".format(a ='Firday',b ="Sunday")
print(word)
age = 25

print(f"my name is {full_name} and my age is {age}")


first = full_name[:]
print(first)

name = "emmanuel chukwuokolo"
print(name.rfind('e'))

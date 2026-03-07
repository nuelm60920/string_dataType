fullName = "01.presentation.pdf"
edited_name = fullName[:-4]
print(edited_name)

file_name = edited_name.split('.')
print(file_name)

file_no, file = file_name

print("file number:",file_no)

print("file name:", file)
print("..........information......")

print(type(file))

print(type(file_no)) # string value

print(type(int(file_no))) #integer value
str()

first, last = "Omo", 'Lola'

print(first)
print(last)
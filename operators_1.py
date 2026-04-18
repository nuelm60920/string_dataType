num = 4
print(num % 2) # modulus operator

print(5 >= 5) #greater than or equal to 

print(5 != 5) # not equal to

n =10

n << 2 #bitwise operator - left shit bitwise operator
bin_no= bin(n)
first_name = input('enter your first name')
email = input('enter your email')

email_slice = email[-4:]
username = bin_no+first_name+email_slice

n = 10
n >> 2
#0101

print(int('10100',2))
email ='nuelueujdnhdnndndbdvsvvs@gmail.com'

n= email.find('@') # position where @ is found
print(n)
email_slice2 = email[:n] # get from beginning to the value of n
print('email without @gmail.com:',email_slice2)

print('@' in email) #check if email contains @
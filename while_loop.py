n=0

'''
while n < 10:
    if n % 2 == 0:
        print(n)
    #n += 1
    n = n + 1

while n <= 10:
    print(n)
    if n == 7:
        break
    #print(n)
    n = n + 1
  
print("...................")

'''




while n < 10:
    n += 1
    if n == 7: # not execution until 7
        continue
    print(n)

fruits = ['mango','apple','orange','grape']
n = 0

while n < len(fruits):
    print(fruits[n])
    n += 1

    

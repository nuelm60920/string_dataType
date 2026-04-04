friends = ['john','Mary','Kemi',' Nuel', 30, 4.5, [5,2,5],'phone'] #list
numbers = list([4,5,6])  #list
cars = []  #empty list
print(type(friends))
print(type(numbers))
print(type(cars))

[], list()


first_item =friends[3]
print(first_item)

list_items = friends[:3]
print(list_items)
last =friends[-1]
print(last)
length = len(friends)
print(length)
list_2= friends[6][1]
print(list_2)

last_2= friends[-2:]
print(last_2)

friends.append('apple')
print(friends)
cars.append('nissan')
cars.append('toyota')
print(len(cars))


cars.insert(0,'Jeep')
cars.insert(2, 20)
print(cars)

print(cars[1:3])

friends.extend(cars)
print(friends)
number_set = [2,4,5] * 3
print(number_set)

steps = friends[::2]
print(steps)

friends[0] = "James"
print(friends)
friends[3] = "Esther"
print(friends)

friends[1:3] = ['Mango', 'Cashew']

print(friends)

phones =['iphone','samsung','redmi']
laptop = ['mac','hp', 'dell']
print(phones + laptop)

print(len(friends))
friends.pop()
print(len(friends))
print(friends)
friends.remove('James')

print(friends)
print(friends[0])
friends.pop(1)
print(friends)

del friends[3]
print(friends)
#del friends
print(friends)

#friends.clear()
print(len(friends))

#del, pop, remove, clear
#friends.pop() #removees the last item
#friends.pop(2) #removes the item at the position mentioned
#friends.clear() # removes everything inside the list
#friends.remove('Jeep') #removes the item specified
#del friends[3]

print('mango' in friends) # check an item in a list
print(friends)
print(friends.index('Esther')) # checks in position of the item

friends.append('Esther') # adds to the last of a lst
count = friends.count('Esther') #counts how many times this item appeared
print(friends)
print(count)

nums =[4,2,1,9,30,5,7,20]
nums.sort() # sorts the items in ascending order

nums.sort(reverse=True) # reverse order
print(nums)
phones.sort() # sorts the items in ascending order
print(phones)
phones.sort(reverse=True)
print(phones)

family = ['Tina','John','Abraham']
family_2= sorted(family)  # creates a new list that can be asinged to new a variable
print(family_2)
family.reverse() # reverses the items
print(family)

f = family
print('f values:',f)
values = family[:]
print(values)
f_2= family.copy()
print(f_2)

nums =[4,2,1,9,30,5,7,20]
total = sum(nums)
print(total)
mx = max(nums)
print(mx)
mn = min(nums)
print(mn)
print(len(nums))
avg = total / len(nums)
print(avg)

rg = list(range(10))
print(rg)
print(range(10))

first, second, third = ['Tina','John','Abraham']

print(first)
print(second)

jn = " ".join(family)
print(jn)

laptop = ['mac','hp', 'dell']

join_string = " ".join(laptop)
print(join_string)
first, *rest = [20,50,70,10]
print(first)
print(rest)
*mylist,last = [90,50,20,100]
print(mylist)
print(last)
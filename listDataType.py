items = [2,10,30,60,'goat','sheep','line', ['james','king', 'queen','mary'], ['rita','john','erica'], 8,4,4.5,(7,4,6,8), 90,10,70 ]

list_f = list([3,6,78, [3,6,7]])

empty = []




friends = "Nuel Amos"

print(type(items))
print(len(items))
print(type(list_f))
print(type(empty))

print(f"number of items: {len(items)}")
first_item = items[2:7]
print(first_item)
last_item  = items[:-3]
print(last_item)

nest_list_1 = items[7][-1]


print(nest_list_1)

n = items[12]
print(n[2])
print(n)
n_1 = items[-4][-2]
print(n_1)
print(len(empty))

items[1] = 100
print(items)
items[0] = "mac laptop"
print(items)

empty.append('mac laptop')
empty.append('dell laptop')
empty.append('dell laptop')
print(empty)
print(f"items in empty variable {empty}")
items.append(200)
print(items)

print(items)

print(f"when to use it {items} the output")

items.insert(4, "monkey")
print(items)

list_1 = ['iphone 16', 'samsung', 'redemi']
list__2 = ['book', 'pen', 'pencil']
list_1.extend(list__2)
print(list_1)

list_3 = list_1 + list__2
print(list_3)

list_1.sort(reverse=True)
print(list_1)
list_1.sort()
print(list_1)

items[1:6] = ['Jack', 'john','james']
print(items)
spain, england, nigeria = ['Real Madrid', 'Man United', 'Enyimba']
print(f"the biggest club in Spain is {spain}")


items_2 = ['Jack', 'john','james', 'Jack']
fullname = " ".join(items_2)

print(fullname)
print(type(fullname))

n = items_2 * 3
print(n)
nums= [3,5,6,7] *3
print(nums)

print(nums.count(3))
print(items_2.count('Jack'))

#items_2.pop(1)
items_2.remove('james')
print(items_2)

del nums[2]
print(nums)

nums.clear()


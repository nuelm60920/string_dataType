print('#'.center(50, 'W'))
friends = ['Nuel','Mary','John','James','Samson']


count = 1
number_of_friends = len(friends)

while count < number_of_friends:
    print(friends[count])
    count += 1

print("*" * 50)
for x in friends:
    print(x)


print('*' * 50)
for x in friends:
    print(x)
    if x == "John":
        break


print('*' * 50)

for x in friends:
    
    if x == "John":
        continue
    else:
        print(x)


j_names = []
for y in friends:
    if y.startswith('J'):
        j_names.append(y)
print(j_names)


print('*'*50)
colors = ['green','blue', 'yellow','white']
cars =  ['toyota','nissan','benz','jeep']

for col in colors:
    for ca in cars:
        print(col, ca)

print('*'* 50)
for c1, c2 in zip(colors, cars):
    print(c1, c2)

print("*" *50)
for i in range(1,20,2):
    print(i)



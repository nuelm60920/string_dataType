
mylist = [1,3,5,6]
print(type(mylist))
friends = ['james','michael', 'peter', 20, 4,30, 20.5, ['nissan','toyota',True, False],50]
print(friends)
no= len(friends)
print(no)
first= friends[0]
print(first)
slice_1 = friends[:3]
print(slice_1)
second_list= friends[7]
print(second_list)
slice_inner_list=friends[7][1]
print(slice_inner_list)

slice__2 = friends[7][2]
print(slice__2)


friends[0] = "Mary"
print(friends)
friends[7][2] = 'Jeep'
print(friends)

friends[1:2] = ['King', 'Queen']
print(friends)
lst= list(range(5))
print(lst)
name_list= list(['vivian','moses','nuel','john'])
print(name_list)
print(friends[::-1])
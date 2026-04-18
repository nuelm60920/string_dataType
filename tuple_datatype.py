myvalue = (300, 59, 70 ,[3,6,7], (9,6,7), 9, 9, "goat","sheep")
print(type(myvalue)) 

first = myvalue[2]
print(first)

second = myvalue[3][1]
print(second)
item = myvalue[3]
print(item)
sliced = item[1]
print(sliced)

third = myvalue[4][0]
print(third)
print(myvalue[-1])
length = len(myvalue)
print(length)

mylist = list(myvalue)
print(myvalue)
print(mylist)
mylist[0] =200
print(mylist)
my_numbers = 20,30,50 
print(my_numbers)
print(type(my_numbers))

first_3 =myvalue[:3]
print(first_3)
print(myvalue.count(9))
print("index position of 9:",myvalue.index(9))

my_t = (4,5,7,8,9,2,1)
print(my_t[::-1])


numbers = [6,7,8,10]
print(numbers.index(10))
print(10 in numbers)
numbers[3] = 100
print(numbers)
#print(numbers.find(5))

first_num, *rest = my_t
print(first_num)
print(rest)

*all_values, last = my_t
print(all_values)
print(type(all_values))

colors = ('green',"white","blue","black","yellow")
*all_colors, one_color = colors
print(all_colors)
print(one_color)
first_3 = colors[:3]
last_2 = colors[-2:]
print(first_3)
print(last_2)

*a, b = colors


*c,d = colors

#b,a = a,b
#print(b)
d,c = c,d

numbers = (10,20,50) * 3
print(numbers)
n = (4,2,7,9,3)
print(n)
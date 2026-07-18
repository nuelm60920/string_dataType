st={3,5,3,7,1,3,1,5,'nuel'}

print(type(st))
print(len(st))
print(st)
set()
{1:10}
#st['nuel']

mylist = [3,5,6,7,3,6,7]
new_st = set(mylist)
print(new_st)

#print(list(range(10)))
print(list(range(10,-1,-2)))

print(list(range(20,-1,-2)))


StopAsyncIteration                                    
print(set_values)


set_values.add(20)
set_values.add("Laptop")
print(set_values)

fruits = {'mango','cashew','apple', 5,7,9}
cars = {'toyota','tesla','nissian',5,7,9}
a =fruits.update(cars) # update does not create a new set of values but updates fruits



print("a:", a)
print("updates:",fruits)

b = fruits.union(cars) # creates a new set of values
print('b:', b)

new_set = {'Nuel','Ben','Esther','joy',('John','James')}
print(new_set)

new_set.remove('Ben')
new_set.discard('Edward')

print(new_set)

d=set("hello")
print(d)
#print('new values:',fruits)
#print(combined_values)

#product  ={'laptop':20}
#print(product)
f=new_set.pop()
print(f)

new_set.clear()


print(fruits | cars)

print('and:', fruits & cars)

fruits.intersection(cars)
print(fruits)


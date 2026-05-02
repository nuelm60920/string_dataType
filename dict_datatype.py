my_dict = {'name':'Nuel', 'surname':'Edward','age':30, 'phone No': [68934983,9864778483]}
print(type(my_dict))
print(my_dict)

friends = {'John':'080757578588','Mike':83664477848, 'Mary':8949494994}
print(friends)

phone = my_dict['phone No'][1]
print('phone number:',phone)

name = my_dict['name']
print(name)
key_items = my_dict.keys()
print(key_items)
values = my_dict.values()
print(values)
items = my_dict.items()
print(items)

age=my_dict['age']

my_dict['name'] = "Michael"
print(my_dict)
my_dict['height'] = 5.7
print(my_dict)

#del my_dict
del my_dict['name']

print('name' not in my_dict)
#address = my_dict['address']
address = my_dict.get('address','No valid address')
print(address)

print(len(my_dict))



print(age)
dict_function = dict(name = "James", phone_no =980938833,country='Nigeria')
print(type(dict_function))
print(dict_function)


phones = {'samsung':"$2000", 'Iphone 14': '$25000','Readmi' :'$1500'}
print(phones)
print(phones.keys())
key_list = list(phones.keys())
print(key_list)
key_values = list(phones.values())
print(key_values)

items = list(phones.items())
print('items: ',items)


university = {
    'English Language': {
        'teacher':'Nuel',
        "stundents":30, 
        "time": '9:30am',
        'Phone_no':[9899938783, 98465662]},

    'Programming': {
        'teacher':'Mr John', 
        "students":45, 
        "time":"10:30am", 
        "Phone_no": 977585773733},

    "Maths":{
        "teacher":"Mrs Mary", 
        "students": 50, 
        "time":'12:00pm', 
        "phone_no": 574878484}
}
print(university)

print('teacher' in university)
print('English Language' in university)
print('teacher' in university['English Language'])

phone_no = university['Maths']['phone_no']
d ={'laptop':'mac pro 16'}
e = dict(laptop ='mac pro 16')

fruits = ['banana', 'orange','grape','apple']
fruit_items = dict.fromkeys(fruits,50)
print(fruit_items)

d.update(fruit_items)
print(d)

d.update({'cashew':30, "mango":20,"strawberry":30})
print(d)


copy = d.copy()
print(copy)
#d.clear()
print(d)

d.pop('cashew')
print(d)
d.popitem()
print(d)

no_students = university['Programming']['students']
print(no_students)


n={'name':'nuel','age':20,'height':5.7}
m={'name':'mary','address':'30 tinubu way','phone':98484874}

print(n|m)

students = { "Alice": 90, "Bob": 95, "Carol": 72, "David": 95, "Eve": 97, 'Daniel':101 }
best= max(students, key=students.get)
print(best)

best = students['Alice']
best_score = students['Alice']
print('first scores:',best_score)
for i in students.values():
    if i > best_score:
        best_score = i
print('best score:', best_score)

print(set(('appple','mango','orange')))
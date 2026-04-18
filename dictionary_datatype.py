dict_1 ={'name': 'Nuel', 'country': 'Ghana','height':5.7, 'age':25, 'phone no': [89699943,894636636]}
print(dict_1)
keys_items = dict_1.keys()

print(keys_items)
values = dict_1.values()
print(values)

friends = {'Mike':'089484423', 'John':'089298927', 'Mary':'08773733'}
print(friends)



dict_2 = dict(ipone='iphone',price='$2500', location='Lagos',manager='Nuel')
print(dict_2)

name = dict_1['name']
print(name)
dict_1['sister'] ="Tina"
print(dict_1)
dict_1['name'] = "Mercy"
print(dict_1)

#dict_1['address']
addresss = dict_1.get('address','no valid address')
print(addresss)
club = {}
print(len(club))
club['ManU'] = '60 million fans'
club['Real Madrid'] = '100 million fans'
print(club)
items = dict_1.items()
print(items)
list_items = list(dict_1.keys())
print(list_items)

friends ={'name':'Esther', 'surname':'Jerry'}
family ={'father':'Edward',"mother":'Blessing'}
friends.update(family)
print(friends)

friends['name'] ='Nana'
print(friends)

unversity ={
    'English Language':{'teacher':'Rita','students':30,'means of teaching':'online'},
    'Maths' :{'teacher': 'John', 'Students': 50, 'means of teaching': 'offline'},
    'Programming': {'teacher':'Nuel', 'students':30, 'means of teaching': 'Online'}
    
}
print(unversity)
course = unversity['English Language']
print('course details:',course)
teacher = unversity['English Language']['teacher']
print(teacher)

#unversity.clear()
print(unversity)
#del unversity
#print(unversity)

print('........................testing...............................')

print('teacher' in unversity['English Language'])
print('country' in dict_1)
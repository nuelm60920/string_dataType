myset ={"Mango",'Apple',"Orange","Cashew","Mango","Apple",(3,5,7)}
myset_1 = {}
myset_2 = set(("hello","world"))
print(type(myset))
print(myset)
print(myset_2)
print(type(myset_2))

new_set = set(["Nuel","Esther","Joy","John"])
print(new_set)

new_set.add("Jerry")
new_set.update(['King','Queen'])
print(new_set)

leaders = {"Trump","Buhari","Mercy","Mike"}
new_set.update(leaders)
print(new_set)

personal_properties = {"car","bike","phone","sonny"}
tv_sets = {"lg","samsung","sonny"}

belongings = personal_properties | tv_sets
print(belongings)
#belongings.discard("sonny")
#print(belongings)

belongings.pop()
print(belongings)

#belongings.clear()
bel = belongings.copy()
print(bel)

items = {"pen","pencil","ruler","chalk", "python"}
courses = {'python','java','javascript','.Net',"pen"}

studies = items.union(courses) # union creat while new a set while update adds to the existing values
print(items)
print(studies)

commom_values =items & courses # common values
print(commom_values)
common = items.intersection(courses) #common values
print(common)

diff  = items - courses # what is not in course
print(diff)
diff_2 = items.difference(courses) ## what is not in course
print(diff_2)

print("Pen" in items)

print(set(range(5,(10 + 1),2)))
#range(start:stop:step)

set_values = {3,True,1, 6,3,False, 0}
print(set_values)
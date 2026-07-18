def teacher(name,ph):
    print('hello world')

    #print(n)
    age = int(input('enter teacher age:'))
    email = input('enter email:')
    print(name)
    print(age)
    print(email)
    print(ph)




name = input('enter teacher name:')
ph = input('enter phone:')

teacher(name,ph)



def schoolTeacher(teachers, name):
    for x in teachers:
        if x == name:
            print('promotion is due')


teachers = ['rita','mike','john','james','jenny']
name = "jenny"
schoolTeacher(teachers, name)




def family(name, location="Lagos"):
    print(f"family name:{name}")
    print(F"location:{location}")


family('Enugu', 'Nuel')

family(location="Abuja", name="Mike")



def reverse_string(s):
    rev = ""
    for x in s:
        rev = x +rev
    
    return rev


print(reverse_string("Michael"))


def reverse_string1(s):
    st = "".join(reversed(s))
    return st



print(reverse_string1("emmanuel"))

nums=[1,2,3,2,4,1]

for a in nums:
    pass
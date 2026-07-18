def multiplication_numbers():
    num1 = int(input('enter first number:'))
    num2 = int(input('enter second number:'))
    num3 = num1 * num2
    print(num3)


multiplication_numbers()


def multiplication(num1, num2):
    num3 = num1 * num2
    print(num3)



n1 = int(input('enter your own number:'))
n2 = int(input('enter your own number:'))
multiplication(n1,n2)


def addition(n1,n2,n3):
    if n1 < 1 or n2 < 1 or n3 < 1:
        return "Only numbers above 1 are accepted"
    

    c = n1 + n2 + n3
    return c 

print(addition(2,4,6))
res = addition(0,10,20)
print(f"total value of our addition is:{res}")
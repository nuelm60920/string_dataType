customer = input('enter customers name:')
number_of_items = int(input('enter number of items purchased:'))
items = {}
total = 0

count = 1
while count <= number_of_items:
    product = input('enter the name of product:')
    price = int(input('enter price'))

    items[product] = price
    total += price



    count += 1


print(f"Hi, {customer}, total amount is ${total}\nthe items purchased is below:\n")
for x in items.items():
    print(x)

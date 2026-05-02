items = [2,4,5,7,10]
for i in items:
    items.remove(i)

print(items)






def average_number(numbers):
    total =0
    for i in numbers:
        total += numbers[i]
        average = total / len(numbers - 1)

        return average
    
res = [8,5,7,8,]
num = average_number(res)
print(f"average of the numbers is {num}")
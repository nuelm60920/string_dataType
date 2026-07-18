def palindrome(word):
    return True if word[::-1] == word else False


print(palindrome('madam'))



def factoria(num):
    if num < 0:
        return "incorrect number"
    
    result = 1

    for x in range(2, num + 1):
        result = result * x

    return result

res = factoria(5)
print(res)


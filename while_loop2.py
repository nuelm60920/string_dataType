n = 10
while n >= 0:
    if n % 2 == 0:
        print(n)
    #print(n % 2 == 0)
    n -= 1

print("*" * 50 )
username = 'nuel01'
password ="nuel123"


max_attempt = 3
start = 0

while start <= max_attempt:
    user_name = input("Enter your username: ")
    password_input = input("Enter your password: ")


    if user_name == username and password_input == password:
        print(f"Hello, {user_name}, Access granted!")

        break

    else:
        start += 1
        remaining = max_attempt - start

        if remaining > 0:
            print("Access Denied!")
            print(f"Invalid credential.{remaining} attempts remaining.")

        else:
            print('Time elapsed. Account locked!')
            break



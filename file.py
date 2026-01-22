filename = 'file.txt'
with open(filename,'r+') as file:
    content = file.read()
    print(content)
with open(filename,'r+') as file:
    for line in file:
        print(line.strip())
with open(filename,'r+') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
print(content.replace('fg', '12'))

while True:
    with open(filename, 'a') as file:
        username = input("Enter your name (or 'exit' to quit): ")
        if username.lower() == 'exit':
            break
        file.write(username + '\n')
        print(f"Hello, {username}!")

while True:
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        result = number1 + number2
        print(f"The sum is: {result}")
        break

try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    pass

import json
def get_stored_numbers():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            numbers = json.load(f)
            return numbers if isinstance(numbers, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def favorite_number():
    numbers = get_stored_numbers()
    user_number = input("Enter your favorite number: ")
    
    if user_number in numbers:
        print(f"Welcome! {user_number} is already in your favorites!")
    else:
        numbers.append(user_number)
        with open('favorite_number.json', 'w') as f:
            json.dump(numbers, f)
        print(f"Added {user_number} to your favorites!")
    
    print(f"Your favorite numbers: {numbers}")

favorite_number()

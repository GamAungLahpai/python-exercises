#While Loop
# Module 4
#No.1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

# No.2
inches_to_cm = 2.54

while True:
    inches = float(input("Enter a value in inches (negative to quit): "))
    if inches < 0:
        print("Negative value entered. Program ending.")
        break
    centimeters = inches * inches_to_cm
    print(f"{inches} inches is equal to {centimeters} centimeters")

# N0.3
numbers = []

while True:
    user_input = input("Enter a number (empty string to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")

# No.4
import random

secret_number = random.randint(1, 20)

while True:
    guess = int(input("Guess the number between 1 and 20: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You've guessed the number.")
        break
#No.5
correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Incorrect username or password.")

if attempts == max_attempts:
    print("Access denied.")

#No.6
import random
import math
random_points = int(input("How many points to be generated? "))
inside_points = 0
i=0
while i< random_points:
    x = random.uniform(-1, 1.)
    y = random.uniform(-1, 1.)
    if x**2 + y**2 <= 1:
        inside_points += 1

    i += 1
pi = 4 * inside_points/ random_points
print(f"Pi estimation is {pi}, the difference with math pi is: {math.pi - pi}")
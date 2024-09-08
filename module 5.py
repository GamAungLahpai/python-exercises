#Module 5 (for Loop)
#1
import random
num_dice = int(input("How many dice would you like to roll! "))
total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"The total sum is: {total_sum}")

#2
numbers = []
num = input("Enter the first number or quit by pressing Enter: ")

while num != "":
    numbers.append(float(num))  # Convert input to float and add to list
    num = input("Enter the next number or quit by pressing Enter: ")
if len(numbers) < 5:
    print("Please enter at least 5 numbers.")
else:
    numbers.sort(reverse=True)
    print("The five greatest numbers are:", numbers[:5])

#3
num = int(input("Type an integer! "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number.")


#4
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)
print("\nThe cities you entered are:")
for city in cities:
    print(city)



# Module 6
# Ex.1
import random
def dice_roll():
    return random.randint(1, 6)
while True:
    dice = dice_roll()
    print(f"Dice's eyes are: {dice}")
    if dice == 6:
        break
# Ex 2
def dice_roll_side (num):
    return random.randint(1, num)
num = int(input("How many sides in your dice? "))
while True:
    dice = dice_roll_side(num)
    print(f"Dice's eyes are: {dice}")
    if dice == num:
        break

# 3
def gallons_to_liters(gallons):
    return 3.78541 * gallons

while True:
    user_gallon = float(input("How many gallons would you like to convert? "))
    if user_gallon < 0:
        break
    print(f"{user_gallon} gallons are {gallons_to_liters(user_gallon):.2f} liters.")

# 4

def sum_of_list(numbers):
    return sum(numbers)

def main():
    numbers = [10, 20, 30, 40, 50]
    total = sum_of_list(numbers)
    print(f"The sum of the list {numbers} is {total}.")
main()

#5
import random

def make_even(num_list):
    result = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            result.append(num_list[i])
    return result

def print_list(message, num_list):
    print(message, end=": ")
    for i in range(len(num_list)):
        print(num_list[i], end=", ")
    print()

example_list = []
for n in range(10):
    example_list.append(random.randint(1, 99))

print_list("Original list", example_list)
new_list = make_even(example_list)
print_list("Only even number list", new_list)

#6

import math

def pizza_efficiency(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius / 100) ** 2
    return price / area

p1_diameter = float(input("What is the diameter of the 1st pizza (in cm)? "))
p1_price = float(input("What is the price of the 1st pizza (in euros)? "))
p2_diameter = float(input("What is the diameter of the 2nd pizza (in cm)? "))
p2_price = float(input("What is the price of the 2nd pizza (in euros)? "))

if pizza_efficiency(p1_diameter, p1_price) < pizza_efficiency(p2_diameter, p2_price):
    print("The first pizza is a better choice! Grab it.")
else:
    print("The second pizza is a better choice! Grab it.")






















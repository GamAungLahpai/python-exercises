#Exercise 1
name = input("what is your name? ")
print(f"Hello, {name}! ")

#Exercise 2
import math
radius = float(input('What is the radius of the circle? '))
area = math.pi * radius **2
print(f'The area is  {area}' )

#Exercise 3
import math
Length = int(input('What is the length of a rectangle? '))
width = int(input('What is the width of a rectangle? '))
perimeter = 2 * (Length + width)
area = (Length * width)
print(f'The perimeter of the rectangle is {perimeter}')
print(f'The area of the rectangle is {area}')

#Exercise 4
import math
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
num_3 = float(input("Enter a third number: "))

sum = num_1 + num_2 + num_3
product = num_1 * num_2 * num_3
average = sum/3

print(f"The sum of the numbers is {sum}")
print(f"The product of the number is {product}")
print(f"The average of the numbers is {average}")

#Exercise 5
print("Enter talents: ")
talents = float(input())

print("Enter pounds: ")
pounds = float(input())

print("Enter lots: ")
lots= float(input())

kg_weight = ((talents*20 + pounds)*32 + lots)* 0.0133
gr_weight = 1000.0* (kg_weight - int(kg_weight))

print(f"The weight in modern units:\n {int(kg_weight)} kilograms and {gr_weight:.2f} grams")


#Exercise 6
import random
three_digit_code = f"{random.randint(0, 999):03d}"
print(f"First combination of lock number: {three_digit_code}")

four_digit_code = "".join(str(random.randint(1, 6)) for _ in range(4))
print(f"Second combination of lock number: {four_digit_code}")
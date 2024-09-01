#module 3
# No1
size_limit = 42
zander_length = float(input("What is the length of the fish in centimeters? "))

if zander_length >= size_limit:
    print("The fish meets the size limit. You can keep it.")
else:
    difference = size_limit - zander_length
    print(f"The zander is below the size limit by {difference:.1f} centimeters. You must release it back into the lake.")

# No2

cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#No3

gender = input("Please enter your biological gender (male/female): ")
hemoglobin = float(input("Please enter your hemoglobin value (g/l): "))

if gender.lower() == 'female':
    if hemoglobin < 117:
        print("Your hemoglobin is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

if gender.lower() == 'male':
    if hemoglobin < 134:
        print("Your hemoglobin is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

#No 4
year = int(input("Please enter a year: "))

if (year % 4 == 0 or year % 100 == 0 and year % 400 == 0):
    print (f"{year} is a leap year.")
else:
    print (f"{year} is not a leap year.")




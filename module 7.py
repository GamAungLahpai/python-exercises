# Module 7
# Ex 1

def get_season(month):
    seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
    if month in [12, 1, 2]:
        return seasons[0]
    elif month in [3, 4, 5]:
        return seasons[1]
    elif month in [6, 7, 8]:
        return seasons[2]
    elif month in [9, 10, 11]:
        return seasons[3]
    else:
        return "Invalid month"

month = int(input("Enter the number of a month (1-12): "))
season = get_season(month)
print(f"The season is: {season}")

# Ex 2
name_set = set()

while True:
    name = input("Enter a name (or press Enter to stop): ")
    if name == "":
        break
    if name in name_set:
        print("Existing name")
    else:
        print(f"New name")
        name_set.add(name)
print(*name_set, sep= "\n")

# Ex 3
airport_data = {}


def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ").upper().strip()
    if icao_code in airport_data:
        print("This airport already exists.")
    else:
        airport_name = input("Enter the name of the airport: ").strip()
        airport_data[icao_code] = airport_name
        print("Airport added successfully.")


def fetch_airport():
    while True:
        icao_code = input("Enter the ICAO code of the airport to fetch: ").upper().strip()
        if icao_code in airport_data:
            print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
        else:
            print("Airport not found.")
            choice = input(
                "Choose an option:\n1. Add airport\n2. Fetch another airport\n3. Exit\nYour choice: ").strip()

            if choice == "1":
                add_airport()
            elif choice == "2":
                continue
            elif choice == "3":
                break
            else:
                print("Invalid option.")


fetch_airport()




























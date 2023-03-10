#Rashelle Ward
#CIS261
#Country Codes
def display_menu():
    print("Command Menu")
    print("view -   View country name")
    print("add  -   Add a country")
    print("del  -   Delete a country")
    print("exit -   Exit program")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    listofcodes = "Country codes: "
    for code in codes:
        listofcodes += code + " "
    print(listofcodes)

def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")

def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")

def main():
    countries = {"AR": "Argentina", "US": "United States", "NO": "Norway"}

    display_menu()
    while True:
        command = input("Command: ")
        if command.lower() == "view":
            view(countries)
        elif command.lower() == "add":
            add(countries)
        elif command.lower() == "del":
            delete(countries)
        elif command.lower() == "exit":
            print("Good Bye!")
            break
        else:
            print("This is not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
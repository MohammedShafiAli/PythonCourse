FILE_PATH = "C:/Users/User/Desktop/PythonCourse/6_Files/acronyms.txt"
FILE_PATH = "6_Files/acronyms.txt"

def print_all_acronyms():
    try:
        with open(FILE_PATH) as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print("File not found")

def find_acronym():
    look_up = input("What acronym do you want to look up?: ")

    found = False
    try:
        with open(FILE_PATH) as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
    
    if not found:
        print("The acronym does not exist")

def add_acronym():
    acronym = input("What acronym would you like to add?: ")
    definition = input("What is the definition?: ")
    with open(FILE_PATH, "a") as file:
        file.write(acronym + " - " + definition + "\n")

def main():
    print("Welcome to Acroyms")
    while True:
        print("\n1. Print all acronyms")
        print("2. Find acronym")
        print("3. Add acronym")
        print("4. Exit")

        try:
            menu_choice = int(input("Enter menu choice: "))
        except:
            print("Invalid input")
            continue

        if menu_choice == 1:
            print_all_acronyms()
        elif menu_choice == 2:
            find_acronym()
        elif menu_choice == 3:
            add_acronym()
        elif menu_choice == 4:
            print("Program terminated")
            break
        else:
            print("Invalid input")

main()
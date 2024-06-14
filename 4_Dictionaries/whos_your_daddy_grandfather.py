pairs = {"Soliman(as)": ["Dauod(as)","Eisha(as)"],
         "Yusuf(as)": ["Yaqub(as)","Isaac(as)"],
         "Ismail(as)": ["Ibrahim(as)","Azar"],
         "Abel(as)": ["Adam(as)","Don't have one"],
         "Muhammed(as)": ["Abdullah(as)", "Hashim(as)"]
        }
print("Welcome to Who's Your Daddy")
while True:
    print("\n1. Print all son's")
    print("2. Find father")
    print("3. Find grandfather")
    print("4. Add")
    print("5. Remove")
    print("6. Replace father")
    print("7. Exit")

    menu_choice = int(input("\nEnter menu choice: "))

    if menu_choice == 1:
        for son in pairs:
            print(son)
    elif menu_choice == 2:
        son_name = input("Enter son's name: ")
        print("The father is", pairs.get(son_name)[0])
    elif menu_choice == 3:
        son_name = input("Enter son's name: ")
        print("The grandfather is", pairs.get(son_name)[1])
    elif menu_choice == 4:
        son_name = input("Enter son's name: ")
        father_name = input("Enter father's name: ")
        grandfather_name = input("Enter grandfather's name: ")
        pairs[son_name] = [father_name, grandfather_name]
    elif menu_choice == 5:
        son_name = input("Enter son's name: ")
        if son_name not in pairs:
            print("Invalid entry")
            continue
        del pairs[son_name]
    elif menu_choice == 6:
        son_name = input("Enter son's name: ")
        if son_name not in pairs:
            print("Invalid entry")
            continue
        father_name = input("Enter updated father's name: ")
        pairs[son_name][0] = father_name
    elif menu_choice == 7:
        print("Thanks for playing")
        break
    else:
        print("Invalid menu choice")
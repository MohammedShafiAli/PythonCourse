pairs = {"Soliman(as)":"Dauod(as)",
         "Yusuf(as)":"Yaqub(as)",
         "Ismail(as)":"Ibrahim(as)",
         "Abel(as)":"Adam(as)",
         "Muhammed(as)":"Abdullah(as)"
        }
print("Welcome to Who's Your Daddy")
while True:
    print("\n1. Print all son's")
    print("2. Find father")
    print("3. Add pair")
    print("4. Remove pair")
    print("5. Replace father")
    print("6. Exit")

    menu_choice = int(input("\nEnter menu choice: "))

    if menu_choice == 1:
        for son in pairs:
            print(son)
    elif menu_choice == 2:
        son_name = input("Enter son's name: ")
        print("The father is", pairs.get(son_name))
    elif menu_choice == 3:
        son_name = input("Enter son's name: ")
        father_name = input("Enter father's name: ")
        pairs[son_name] = father_name
    elif menu_choice == 4:
        son_name = input("Enter son's name: ")
        if son_name not in pairs:
            print("Invalid entry")
            continue
        del pairs[son_name]
    elif menu_choice == 5:
        son_name = input("Enter son's name: ")
        if son_name not in pairs:
            print("Invalid entry")
            continue
        father_name = input("Enter updated father's name: ")
        pairs[son_name] = father_name
    elif menu_choice == 6:
        print("Thanks for playing")
        break
    else:
        print("Invalid menu choice")

character = {"pool": 30,
             "strength": 0,
             "health": 0,
             "wisdom": 0,
             "dexterity": 0}

print("Create your character")
while True:
    print("\n1. View you character")
    print("2. Add points")
    print("3. Remove points")
    print("4. Exit game")

    choice = int(input("\nEnter menu choice: "))

    if choice == 1:
        print(character)
    elif choice == 2:
        print("You have", character["pool"], "points available")
        print("1. Strength")
        print("2. Health")
        print("3. Wisdom")
        print("4. Dexterity")

        attr_choice = int(input("Which attribute would you like to assign points to?: "))
        points_to_add = int(input("How many points would you like to assign?: "))
        
        if points_to_add > character["pool"]:
            print("Invalid number of points")
            continue

        if attr_choice == 1:
            character["strength"] = character["strength"] + points_to_add 
        elif attr_choice == 2:
            character["health"] = character["health"] + points_to_add 
        elif attr_choice == 3:
            character["wisdom"] = character["wisdom"] + points_to_add 
        elif attr_choice == 3:
            character["dexterity"] = character["dexterity"] + points_to_add 
        else:
            print("Invalid entry choice")
            continue

        character["pool"] = character["pool"] - points_to_add

    elif choice == 3:
        print("You have", character["pool"], "points available")
        print("1. Strength")
        print("2. Health")
        print("3. Wisdom")
        print("4. Dexterity")

        attr_choice = int(input("Which attribute would you like to remove points from?: "))
        points_to_remove = int(input("How many points would you like to remove?: "))
        
        if points_to_remove > list(character.values())[attr_choice]:
            print("Invalid number of points")
            continue

        if attr_choice == 1:
            character["strength"] = character["strength"] - points_to_remove 
        elif attr_choice == 2:
            character["health"] = character["health"] - points_to_remove 
        elif attr_choice == 3:
            character["wisdom"] = character["wisdom"] - points_to_remove 
        elif attr_choice == 3:
            character["dexterity"] = character["dexterity"] - points_to_remove 
        else:
            print("Invalid attribute choice")
            continue

        character["pool"] = character["pool"] + points_to_remove
    elif choice == 4:
        break
    else:
        print("Invalid menu choice")
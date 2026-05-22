inventory = []

while True:
    print("Weapon Inventory")
    print("1 . Add Weapon")
    print("2 . Show Weapon")
    print("3 . Remove Weapon")
    print("4 . Exit...")

    choice = input("Enter Choice (1 - 4) : ")

    if choice == "1":
        add_weapon = input("Enter The Weapon Name : ")
        inventory.append(add_weapon)
        print("Weapon Added Successfully")

    elif choice == "2":
        if len(inventory) == 0:
            print("No Weapons Found")
        else:
            for i in range(len(inventory)):
                print(i , ":" , inventory[i])

    elif choice == "3":
        if len(inventory) == 0:
            print("Inventory is Empty")
        else:
            remove_weapon = int(input("Enter the Weapon : "))
            removed_weapon = inventory.pop(remove_weapon)
            print("Weapon Removed Succesfully")
            print("Removed Weapon is : " , removed_weapon)
        
    elif choice == "4":
        print("Exit...")
        break

    else:
        print("Invalid Move")

import random 

while True:
    print("Dice Roller Game")
    print("1 . Roll Dice")
    print("2 . Exit...")
    
    choice = input("Enter Choice (1 - 2) : ")

    if choice == "1":
        dice = random.randint(1 , 6)
        print(dice)
    
    elif choice == "2":
        print("Exit...")
        break
    
    else:
        print("Invalid Move")

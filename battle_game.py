import random

player_hp = 100

enemy_hp = 100

while True:
    print("Mini Battle Game")
    print("1 . Attack")
    print("2 . Heal")
    print("3 . Exit...")

    choice = input("Enter Choice (1 - 3) : ")

    if choice == "1":
        damage = random.randint(10 , 30)

        critcal_hit = random.randint(1 , 5)
        if critcal_hit <= 2:
            damage *= 2
            print("Super Attack You Got Is : " , "Critcal_hit")

        enemy_hp -= damage
        print("You Attacked Enemy For : " , damage , "Damage")

        enemy_damage = random.randint(10 , 30)
        player_hp -= enemy_damage
        print("Enemy Attacked You For : " , enemy_damage , "Damage")

    elif choice == "2":
        healing_potion = random.randint(10 , 40)
        player_hp += healing_potion
        print("You Goat Healing For : " , healing_potion , "Healed")

    elif choice == "3":
        print("Exit...")
        break

    else:
        print("Invalid Move")

    if player_hp <= 0:
        print("Game Over")
        break

    if enemy_hp <= 0:
        print("Game Over")
        break

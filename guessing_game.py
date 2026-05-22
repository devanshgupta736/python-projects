import random

secret = random.randint(1, 10)

while True:
    user = int(input("Guess Number (1 - 10) : "))
    print("Computer Choice : " , secret)

    if user == secret:
        print("You Won")
        break
    else:
        print("Wrong , Try Again")

import random

comp_choice = random.randint(1 , 10)

chances = 5

while chances > 0:
    user_choice = int(input("Guess the Numbers (1 , 10) : "))
    print("Computer Choice : " , comp_choice)

    if user_choice == comp_choice:
        print("Correct Guess , You Won")
        break
    else:
        chances -= 1

    if user_choice > comp_choice:
        print("Too High")
    else:
        print("Too Low")

    print("Chances Remaining : " , chances)

    if chances == 0:
        print("All Chances are Exhausted ! Game Over")
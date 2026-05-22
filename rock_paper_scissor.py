import random

chances = 5

while chances > 0:
    user_choice = input("Guess The Move (Rock , Paper , Scissor) : ")
    comp_choice = random.choice(["Rock" , "Paper" , "Scissor"])
    print("Computer Choice is : " , comp_choice)

    if user_choice == comp_choice:
        print("Match Tie")

    elif user_choice == "Rock":
        if comp_choice == "Scissor":
            print("Rock Smashes Scissor , You Won")
        else:
            print("Paper Covers Rock ! You Lose")

    elif user_choice == "Paper":
        if comp_choice == "Rock":
            print("Paper Covers Rock , You Won")
        else:
            print("Scissor Cuts Papers ! You Lose")

    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissor Cuts Paper , You Won")
        else:
            print("Rock Smashes Scissor ! You Lose")

    else:
        print("Invalid Move")
        continue

    chances -= 1
    print("Total Chances Remaining : " , chances)

    if chances == 0:
        print("Chances are Exhausted ! Game Over")

    play_again = input("Do You want to play again (Yes / No) : ")
    
    if play_again == "No":
        print("Game Over")
        break
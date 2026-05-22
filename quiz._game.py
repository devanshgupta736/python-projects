# Single Question Quiz

while True:
    print("Quiz Game")
    print("Q1 . Who makes Python ?")
    print("1 . James Gosling")
    print("2 . Guido Van Rossum")
    print("3 . Dennis Ritchie")

    answer = input("Enter Your Choice (1 - 3) : ")

    if answer == "2":
        print("Correct Answer")
        break
    else:
        print("Wrong Answer")

# Multiple Questions Quiz

def start_quiz():
    score = 0

    print("Solve Quiz Questions")
    print("Q1 . Who Invent Python ? ")
    print("1 . Hyper Text Mark Up Language")
    print("2 . Guido Van Rossum")
    print("3 . Dennis Ritchie")

    answer = input("Enter Choice (1 - 3) : ")

    if answer == "2":
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
    
    print("Total Score is : " , score)

    print("Q2 . Who Invent C Language ?")
    print("1 . Hyper Text Mark Up Language")
    print("2 . Guido Van Rossum")
    print("3 . Dennis Ritchie")

    answer = input("Enter Choice (1 - 3) : ")

    if answer == "3":
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")

    print("Total Score is : " , score)

    print("Q3 . Full Form of HTML ?")
    print("1 . Hyper Text MArk Up Language")
    print("2 . Guido Van Rossum")
    print("3 . Dennis Ritchie")

    answer = input("Enter Choice (1 - 3) : ")

    if answer == "1":
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
    
    print("Final Score is : " , score)

while True:
    print("1 . Start Quiz")
    print("2 . Exit...")

    choice = input("Enter Choice (1 - 2) : ")

    if choice == "1":
        start_quiz()
    
    elif choice == "2":
        print("Exit...")
        break

    else:
        print("Invalid Choice")


# # Multiple Questions Quiz


import random

def start_quiz():
    score = 0
    
    comp_choice = random.choice(["HTML" , "Python" , "C"])

    print("Computer Choice is : " , comp_choice)

    if comp_choice == "HTML":
        print("Q1 . Full Form of HTML .")
        print("1 . Hyper Text Mark Up Language")
        print("2 . High Text Maching Language")
        print("3 . Hyper Tool Markup Language")
        
        user_choice = input("Enter the Choice (1 - 3) : ")

        if user_choice == "1":
            print("Correct Answwer")
            score += 1
        else:
            print("Wrong Answer")
        
        print("Total Score is : " , score)
    
    elif comp_choice == "Python":
        print("Q1 . Who Invent Python ? ")
        print("1 . Hyper Text Mark Up Language")
        print("2 . Guido Van Rossum")
        print("3 . Dennis Ritchie")
        
        user_choice = input("Enter the Choice (1 - 3) : ")

        if user_choice == "2":
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")

        print("Total Score is : " , score) 

    elif comp_choice == "C":
        print("Q1 . Who Invent C Language ?")
        print("1 . Hyper Text Mark Up Language")
        print("2 . Guido Van Rossum")
        print("3 . Dennis Ritchie")

        user_choice = input("Enter the Choice (1 - 3) : ")

        if user_choice == "3":
            print("Correct Answer")
            score += 1
        else:
            print("Wrong Answer")
        
        print("Total Score is : " , score)

while True:
    print("1 . Start Quiz")
    print("2 . Exit...")

    choice = input("Enter Choice (1 - 2) : ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        print("Exit...")
        break

    else:
        print("Invalid Choice")
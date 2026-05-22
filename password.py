attempts = 5
correct_password = "MrCoder123"         
while attempts > 0:
    user_pass = input("Enter the Password : ")

    if user_pass == correct_password:
        print("Password is Correct Access Granted")
        break
    else:
        print("Wrong attempt")
    
    attempts -= 1
    print("Total Attempts left : " , attempts)

    if attempts == 0:
        print("Attempts are Exhausted Game Over")


import random

attempts = 5

while attempts > 0:
    comp_pass = random.choice(["MrCoder123" , "MrVilen124" , "MrNeon345"])      
    print("Correct Password is : " , comp_pass)

    if user_pass == comp_pass:
        print("Correct Password Access Granted")
        break
    else:
        print("Wrong Attempt")

    attempts -= 1
    print("Total Attempts left : " , attempts)

    if attempts == 0:
        print("Attempts are Exhausted You Locked")
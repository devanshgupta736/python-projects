correct_username = "Mr Devansh 123"

correct_password = "python.py"

chances = 3

while chances > 0:
    user_name = input("Enter The Correct Username : ")
    user_password = input("Enter The Correct Password : ")

    if user_name == correct_username:
        if user_password == correct_password:
            print("Username is Correct")
            print("Password is Correct")
            print("Access Granted")
            break
        else:
            print("Wrong Password")
            chances -= 1
            print("Total Chances Remaining : " , chances)

    else:
        print("Invalid Username")
        chances -= 1
        print("Total Chances Remaining : " , chances)
    
    if chances == 0:
        print("Chances Are Over ! Account Locked")
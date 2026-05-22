while True:
    print("\n 1 . Addition")
    print("2 . Subtraction")
    print("3 . Multiplication")
    print("4 . Division")
    print("5 . Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a + b)

    elif choice == "2":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a - b)

    elif choice == "3":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a * b)

    elif choice == "4":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a / b)

    elif choice == "5":
        print("Exiting...")
        break


while True:
    print("1 . Power")
    print("2 . Modulus")
    print("3 . Exit")

    user_choice = input("Enter Choices : ")

    if user_choice == "1":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a ** b)
    
    elif user_choice == "2":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a % b)
    
    elif user_choice == "3":
        print("Exiting...")
        break


while True:
    print("Addtional Calculator")
    print("1 . Add")
    print("2 . Subtract")
    print("3 . Multiply")
    print("4 . Divide")
    print("5 . Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a + b)

    elif choice == "2":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a - b)
    
    elif choice == "3":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a * b)
    
    elif choice == "4":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a / b)
    
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice , Try Again")


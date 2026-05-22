import math

history = []

while True:
    print("Upgraded Calculator")
    print("1 . Addition")
    print("2 . Power")
    print("3 . Square Root")
    print("4 . Percentage")
    print("5 . History")
    print("6 . Exit...")

    choice = input("Enter Choice (1 - 6) : ")

    if choice == "1":
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        print(a + b)
    
    elif choice == "2":
        num = 5
        
        result = num ** 2

        print(result)

    elif choice == "3":
        num = int(input("Enter a num : "))

        result = math.sqrt(num)

        print(result)
    
    elif choice == "4":
        num = int(input("Enter a num : "))

        result = num / 100

        print(result)
    
    elif choice == "5":
        result = 65

        history.append(result)

        print(history)

    elif choice == "6":
        print("Exit...")
        break

    else:
        print("Invalid Choice")
balance = 1000

while True:
    print("ATM Machine Simulator")
    print("1 . Check Balance")
    print("2 . Deposit Machine")
    print("3 . Withdraw Money")
    print("4 . Exit...")

    choice = input("Enter Choice (1 - 4) : ")

    if choice == "1":
        print("Your Balance is : " , balance)

    elif choice == "2":
        deposit_money = int(input("Enter Money For Deposit : "))

        balance += deposit_money
        print("Money Deposit Successfully")
        print("Total Balance is : " , balance)
    
    elif choice == "3":
        withdraw_money = int(input("Enter Money For Withdrawl : "))

        if withdraw_money <= balance:
            balance -= withdraw_money
            print("Money Successfully Withdrawl")
            print("Your Total Balance is : " , balance)
        else:
            print("Insufficient Balance")
    
    elif choice == "4":
        print("Thank You For Using ATM Machine")
        print("Exit...")
        break

    else:
        print("Invalid Move")
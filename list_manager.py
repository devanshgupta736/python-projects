tasks = []

while True:
    print("To-Do-List Manager")
    print("1 . Add Task")
    print("2 . Show Task")
    print("3 . Delete Task")
    print("4 . Mark Task Done")
    print("5 . Exiting...")

    choice = input("Enter Task Num : ")

    if choice == "1":
        task = input("Enter Task Name : ")
        tasks.append(task)
        print("Task Added")

    elif choice == "2":
        print("Show Task")
        for i in range(len(tasks)):
            print(i , tasks[i])
    
    elif choice == "3":
        dlt_idx = int(input("Enter Delete Task idx : "))
        print("Tast Deleted")
        print("Deleted Task is : " , tasks[dlt_idx])

    elif choice == "4":
        mark_idx = int(input("Enter the Task Mark : "))
        tasks[mark_idx] = tasks[mark_idx] +  "Done"
        print("Task Marked")
        print("Task Marked : " , tasks[mark_idx])

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")


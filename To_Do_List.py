tasks = []
print("Welcome to To-Do List")
while True:
    print("\nChoose:")
    print("1 - Add")
    print("2 - Show")
    print("3 - Remove")
    print("4 - Exit")
    option = input("Enter option: ")
    if option == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task saved")
    elif option == "2":
        print("\nTask List:")
        if tasks == []:
            print("No tasks available")
        else:
            count = 1
            for task in tasks:
                print(count, ":", task)
                count += 1
    elif option == "3":
        remove_task = input("Enter task to remove: ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print("Task removed")
        else:
            print("Task not found")
    elif option == "4":
        print("Thank You")
        break
    else:
        print("Wrong option")
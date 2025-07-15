while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. clear all Task")
    print("4. Exit")

    choice=int(input("Enter your choice(1-4): "))
    if choice ==1:
        task=input("enter task:")
        with open("todo.txt","a") as f:
            f.write(task+"\n")
            print("Task added successfully")
    elif choice==2:
        try:
            with open("todo.txt","r") as f:
                tasks=f.readlines()
                if tasks:
                    for i, task in enumerate(tasks, start=1):  
                        print(f"{i}. {task.strip()}")
                else:
                    print("No tasks found.")
        except FileNotFoundError:
            print("No ftask file found.")  
    elif choice==3:
        open("todo.txt","w").close()
        print("All tasks cleared.")
    elif choice==4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
                  



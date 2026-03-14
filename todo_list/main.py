while True:

    print("\n------ TO DO LIST ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter new task: ")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added successfully!")

    elif choice == "2":

        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if len(tasks) == 0:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i].strip())

        except FileNotFoundError:
            print("No tasks file found.")

    elif choice == "3":

        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if len(tasks) == 0:
                print("No tasks to delete.")
            else:
                for i in range(len(tasks)):
                    print(i + 1, ".", tasks[i].strip())

                num = int(input("Enter task number to delete: "))

                if num <= len(tasks):

                    tasks.pop(num - 1)

                    with open("tasks.txt", "w") as file:
                        for task in tasks:
                            file.write(task)

                    print("Task deleted successfully!")

                else:
                    print("Invalid task number.")

        except:
            print("Error occurred while deleting task.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

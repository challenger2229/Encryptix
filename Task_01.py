# Task : create a to-do list via which user can create, update and track their tasks

# approch : the to-do list is created to keep in mind basic utilities and easiness in use of the user. There are 5 different functions to perform different operations 

# the user can provide input(tasks), update tasks and can also mark them done otherwise they will be in "pending state"


print("------------------TO-DO LIST--------------------")


def todo_list():
    tasks = []

    def add_task(description):#function for adding task
        tasks.append({"description": description, "completed": False})
        print(f"Task '{description}' added.")

    def view_tasks():#function for viewing purpose
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['description']} [{status}]")

    def update_task(index, new_description=None):#function to update the task
        if 0 < index <= len(tasks):
            if new_description:
                tasks[index - 1]["description"] = new_description
                print(f"Task {index} description updated to '{new_description}'.")
            tasks[index - 1]["completed"] = True
            print(f"Task {index} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(index):
        if 0 < index <= len(tasks):
            task = tasks.pop(index - 1)
            print(f"Task '{task['description']}' deleted.")
        else:
            print("Invalid task number.")

    while True:
        print("\nTO-DO List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to update: "))
            new_description = input("Enter new description (leave blank to mark as done): ")
            update_task(index, new_description)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == "5":
            print("Exiting TO-DO List...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list()

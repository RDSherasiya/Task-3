import os
tasks = []

# add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# show all tasks
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# update a task
def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print(f"Task updated to '{new_task}'.")
    else:
        print("Invalid task index.")

# remove a task 
def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' removed.")
    else:
        print("Invalid task index.")


while True:
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        index = int(input("Enter the task number to update: "))
        new_task = input("Enter the new task: ")
        update_task(index, new_task)
    elif choice == '4':
        index = int(input("Enter the task number to remove: "))
        delete_task(index)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
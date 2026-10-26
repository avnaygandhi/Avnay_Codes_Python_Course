FILE_NAME="Tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME) as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "a") as file:
        for task in tasks:
            file.write(f"{task}\n")

def main():
    tasks = load_tasks()
    while True:
        print("\n To do list manager")
        print("1. View tasks\n2. Add Task\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if not tasks:
                print("No tasks added")
            else:
                count=1
                for task in tasks:
                    print(f"{count}. {task}")
                    count += 1
        elif choice == "2":
            new_task = input("Enter new task: ")
            if new_task.strip():
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task is saved")
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
main()
import json

def add_task(tasks, name):
    new = {"name": name, "done": False}
    tasks.append(new)

def show_tasks(tasks):
    for i in tasks:
        print(f'{i["name"]} - Done: {i["done"]}')

def remove_task(tasks, name):
    for i in tasks:
        if i["name"] == name:
            tasks.remove(i)
            return True
    return False

def mark_done(tasks, name):
    for i in tasks:
        if i["name"] == name:
            i["done"] = True
            return True
    return False

try:
    with open("data.txt", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

while True:
    print("1. Add task")
    print("2. Show task")
    print("3. Remove task")
    print("4. Mark task done")
    print("5. Exit")
    option = input("Choose an option: ")

    if option == "1":
        task_name = input("Enter task name: ")
        add_task(tasks, task_name)
    elif option == "2":
        show_tasks(tasks)
    elif option == "3":
        task_name = input("Enter task name: ")
        result = remove_task(tasks, task_name)
        if result == True:
            print("Success")
        else:
            print("Failure")
    elif option == "4":
        task_name = input("Enter task name: ")
        result = mark_done(tasks, task_name)
        if result == True:
            print("Success")
        else:
            print("Failure")
    elif option == "5":
        with open("data.txt", "w") as file:
            json.dump(tasks, file)
        break
    else:
        print("Error")


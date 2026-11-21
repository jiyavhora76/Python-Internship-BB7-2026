tasks = []

def add_task(task):
    tasks.append(task)
    print(task, "added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(task, "removed successfully!")
    else:
        print(task, "not found!")

def show_tasks():
    print("\nCurrent To-Do List:")
    for task in tasks:
        print("-", task)


add_task("Complete homework")
add_task("Study Python")
add_task("Read a book")
add_task("Go shopping")
add_task("Exercise")

remove_task("Read a book")
remove_task("Go shopping")

show_tasks()
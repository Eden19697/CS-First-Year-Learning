"""
OOP + JSON Practice: Todo Manager
=================================

Goal:
Build a small project that combines:

- class
- list of dictionaries
- search by id
- update state
- delete/filter
- JSON read/write


Data format
-----------

Each task is a dictionary:

    {
        "id": 1,
        "title": "Study hash table",
        "completed": False
    }

All tasks are stored in a list:

    [
        {"id": 1, "title": "Study hash table", "completed": False},
        {"id": 2, "title": "Practice CSV", "completed": True}
    ]


Class
-----

Create:

    class TodoManager


Methods
-------

1. add_task(title)

Add a new task.

Example:

    manager.add_task("Study graph")


2. complete_task(task_id)

Mark a task as completed.

Return True if found.
Return False if not found.


3. delete_task(task_id)

Delete a task.

Return True if deleted.
Return False if not found.


4. list_tasks()

Return all tasks.


5. save_to_file(filename)

Save tasks to a JSON file.


6. load_from_file(filename)

Load tasks from a JSON file.


Expected output
---------------

[
    {'id': 1, 'title': 'Study graph', 'completed': False},
    {'id': 2, 'title': 'Practice JSON', 'completed': True}
]
True
False
Wrote todos to todos.json
Loaded todos from todos.json
"""


import json


class TodoManager:
    def __init__(self):
        # TODO: Create an empty tasks list.
        self.tasks = []
        # TODO: Create next_id starting from 1.
        self.next_id = 1

    def add_task(self, title):
        # TODO: Create a new task dictionary.
        task_dict = {
        "id": self.next_id,
        "title": title,
        "completed": False
        }
        # TODO: Append task to self.tasks.
        self.tasks.append(task_dict)
        # TODO: Increase self.next_id.
        self.next_id += 1
        # TODO: Return the new task.
        return task_dict

    def complete_task(self, task_id):
        # TODO: Loop through tasks.
        for obj in self.tasks:
        # TODO: If task id matches, set completed to True and return True.
            if task_id == obj["id"]:
                obj["completed"] = True
                return True
        # TODO: If not found, return False.
        return False

    def delete_task(self, task_id):
        # TODO: Loop through tasks by index.
        for index, task in enumerate(self.tasks):
        # TODO: If task id matches, remove it and return True.
            if task["id"] == task_id:
                del self.tasks[index]
                return True
        # TODO: If not found, return False.
        return False

    def list_tasks(self):
        # TODO: Return all tasks.
        return self.tasks

    def save_to_file(self, filename):
        # TODO: Open filename in write mode.
        with open(filename,"w") as file:
        # TODO: Save self.tasks using json.dump(..., indent=4).
            json.dump(self.tasks, file, indent=4)

    def load_from_file(self, filename):
        # TODO: Open filename in read mode.
        with open(filename, "r") as file:
        # TODO: Load tasks using json.load(file).
            reader = json.load(file)
        # TODO: Update self.tasks.
            self.tasks = reader#理解为 github 里面的 pull
        # TODO: Update self.next_id so new tasks get a fresh id.
            if self.tasks:#判断 self.tasks 是不是为空
                self.next_id = max(task["id"] for task in self.tasks) + 1
            else:
                self.next_id = 1


def main():
    manager = TodoManager()

    manager.add_task("Study graph")
    manager.add_task("Practice JSON")
    manager.complete_task(2)

    print(manager.list_tasks())
    print(manager.delete_task(1))
    print(manager.delete_task(99))

    manager.save_to_file("todos.json")
    print("Wrote todos to todos.json")

    new_manager = TodoManager()
    new_manager.load_from_file("todos.json")
    print("Loaded todos from todos.json")
    print(new_manager.list_tasks())


if __name__ == "__main__":
    main()

# Chapter 08: OOP Mini-Projects

This chapter combines classes, a list of dictionaries as instance state, and JSON persistence into two small
working programs: a to-do list manager and a library manager.

## Core ideas

| Concept | What it means here | Example |
| --- | --- | --- |
| Instance state | Data lives on `self.`, not a local variable, so every method can see and change it | `self.tasks = []` |
| Auto-incrementing id | Track the next id on the object, bump it after every creation | `self.next_id += 1` |
| Linear search by id | Walk the list, compare each item's `"id"` | `for task in self.tasks: if task["id"] == task_id:` |
| Persistence | Dump the whole list to JSON, and reload it back into `self` | `json.dump(self.tasks, file, indent=4)` |

## Practice files

| File | Main pattern |
| --- | --- |
| `todo_manager.py` | `TodoManager` class: add / complete / delete / list tasks, save/load as JSON |
| `library_manager.py` | `LibraryManager` class: add / borrow / return / delete / search books, save/load as JSON |

## A useful problem-solving template

Before writing a method, ask:

1. Does this change stored state? Then it must read or write `self.something`, not a local variable.
2. Does this look something up by id? That's a linear search — loop and compare `item["id"] == target_id`.
3. Does "not found" need a signal? Return `False` (or `None`) instead of raising, unless the exercise asks otherwise.

## Run a practice file

From the repository root:

```bash
python3 08_oop_projects/todo_manager.py
python3 08_oop_projects/library_manager.py
```

## Common reminders

- `==` checks equality; `=` assigns. Writing `book["borrowed"] == True` inside an `if` block silently does nothing —
  the state never actually changes, even though the surrounding logic looks correct.
- If a dictionary's fields are documented (like `{"id": ..., "title": ..., "completed": False}`), create every field
  up front when the record is built. A field that only gets added later (e.g. only when a task is completed) means
  freshly created records are missing it entirely.
- After `load_from_file`, recompute `next_id` from the loaded data (`max(id) + 1`) — don't leave it at its
  `__init__` default, or new items will collide with ids that already exist in the file.

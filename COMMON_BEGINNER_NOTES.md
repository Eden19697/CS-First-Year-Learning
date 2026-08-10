# Common Beginner Notes

Short reminders collected while practicing the early chapters in this repository.

## Hash Tables: `set` and `dict`

### Use the right tool for the question

- Use a `set` when you only need fast membership checks or unique values.
- Use a `dict` when each key needs associated information, such as a count, index, or list of grouped values.

```python
seen = set()
counts = {}
```

### Save an updated count back into the dictionary

This expression calculates a new value but does not store it:

```python
counts.get(char, 0) + 1
```

Store the result instead:

```python
counts[char] = counts.get(char, 0) + 1
```

### Do not rely on a set's order

A set is good for membership and uniqueness, but it is not a tool for preserving an order. If a problem asks for the *first* unique character, first count characters, then loop through the original string again.

```python
for char in text:
    if counts[char] == 1:
        return char
```

### Do not overwrite Python built-in names

Avoid variable names such as `dict`, `list`, `set`, or `int`. They hide Python's built-in tools and make code harder to read.

```python
character_counts = {}
number_set = set()
```

### One-pass lookup pattern

For problems such as Two Sum, check whether the needed value was already seen *before* saving the current value. This prevents using the same element twice.

```python
needed = target - value
if needed in seen:
    return [seen[needed], index]
seen[value] = index
```

## Files: CSV and JSON

### CSV values come back as strings

Even a column that looks numeric, like `"85"`, is read as a string. Convert it before doing math:

```python
score = int(row["score"])
```

### `round()` works on one number, not a whole dictionary

Round each value *as it is stored*, not by calling `round()` on the finished dictionary — a `dict` has no
`__round__` method and raises a `TypeError`.

```python
# Wrong: round(averages) fails, averages is a dict
averages[name] = average
return round(averages)

# Right: round the single number before storing it
averages[name] = round(average, 2)
return averages
```

### "At least one" means `> 0`, not `> 1`

A condition meant to catch "failed at least one subject" must use `> 0` (or just check truthiness). Using `> 1`
silently drops anyone who only failed exactly one thing.

```python
if failed_subject:        # correct: true for 1 or more items
    failed[name] = failed_subject
```

## OOP Mini-Projects

### `==` compares, `=` assigns — mixing them up silently does nothing

Inside an `if` block it's easy to write a comparison by accident when a state update was intended. Python doesn't
error on this; it just quietly evaluates the comparison and throws away the result.

```python
# Wrong: this is a comparison, book["borrowed"] never changes
book["borrowed"] == True

# Right: this is an assignment
book["borrowed"] = True
```

### Create every documented field up front, not only when it changes later

If a record's shape is `{"id": ..., "title": ..., "completed": False}`, build it with all three fields immediately.
Adding a field only inside a later method (like `complete_task`) means freshly created records are silently
missing that key until something else touches them.

```python
# Wrong: "completed" only appears after complete_task() runs
task = {"id": self.next_id, "title": title}

# Right: every field exists from the start
task = {"id": self.next_id, "title": title, "completed": False}
```

### Recompute the id counter after loading from a file

`self.next_id` only knows about ids created during the current run. After `load_from_file`, it must be
recalculated from the loaded data, or a new item can reuse an id that's already on disk.

```python
self.next_id = max(item["id"] for item in self.items) + 1 if self.items else 1
```

## Graphs

### Mutate the dictionary itself, not a same-named local variable

`if node not in graph: a = []` creates a throwaway local variable called `a` — it never gets attached to `graph`.
The fix is to assign directly into the dictionary being built.

```python
# Wrong: graph is never actually populated
if node_a not in graph:
    a = []
a.append(node_b)

# Right: mutate graph[node_a] directly
if node_a not in graph:
    graph[node_a] = []
graph[node_a].append(node_b)
```

### Directed edges only go one way

An undirected edge needs both `graph[a].append(b)` and `graph[b].append(a)`. A directed edge only gets the first
line — adding the reverse turns a one-way graph into a two-way one and breaks reachability checks.

### Remove debug `print()` calls before treating a function as finished

A leftover `print(...)` inside a function still runs every time it's called — it doesn't affect correctness, but
it means the actual output no longer matches what the docstring documents as "expected output."

## Heap / Priority Queue

### A "peek" method must return the same shape as its matching "pop" method

`heapq` stores whatever tuple you pushed — `(priority, task_name)` — not just the value you care about. A `pop`
method that unpacks and returns only `task_name` needs its `peek` counterpart to do the same, or callers get a
raw tuple back instead of the value the docstring promises.

```python
# Wrong: returns the whole (priority, task_name) tuple
def peek_task(self):
    return self.heap[0]

# Right: return just the task name, matching pop_task's contract
def peek_task(self):
    return self.heap[0][1]
```


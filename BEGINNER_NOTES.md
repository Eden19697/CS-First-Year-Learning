# Beginner Notes

## 1. Use `dict` for grouping

When records belong to different people or categories, a dictionary is usually the right tool.

Example:

```python
scores_by_student = {}

for name, subject, score in records:
    if name not in scores_by_student:
        scores_by_student[name] = []

    scores_by_student[name].append(score)
```

Why:

Each student needs their own list of scores.

## 2. Use `dict` for counting

Wrong idea:

```text
Loop again and again to count each user
```

Better:

```python
counts[user] = counts.get(user, 0) + 1
```

Why:

`dict.get(user, 0)` safely gives the old count, or `0` if the user is new.

## 3. Save calculated values back

Wrong:

```python
counts.get(user, 0) + 1
```

Why it is wrong:

This calculates a number but does not store it.

Correct:

```python
counts[user] = counts.get(user, 0) + 1
```

## 4. Use `set` for unique values

Example:

```python
titles = set()

for record in records:
    titles.add(record["title"])
```

Why:

A set automatically removes duplicates.

## 5. Use `sorted` with `key`

Example:

```python
ranking = sorted(averages.items(), key=lambda item: item[1], reverse=True)
```

Meaning:

- `item[0]` is the name
- `item[1]` is the average
- `reverse=True` means high to low

## 6. Common edge cases

Things to check:

- empty records
- a student with only one score
- repeated names
- repeated book titles
- ties in ranking
- filtering when no record matches

## 7. Linked list: check the head first

In a linked list, `self.head` is special because it is the only direct entry point.

For deletion, check these cases in order:

```python
if self.head is None:
    return False

if self.head.value == value:
    self.head = self.head.next
    return True
```

Why:

- an empty list has no node to inspect
- deleting the head does not have a previous node to reconnect

## 8. Save `next` before reversing a node

During linked-list reversal, changing `current.next` too early can lose the rest of the list.

Wrong idea:

```python
current.next = prev
current = current.next
```

Why it is wrong:

After the first line, `current.next` points backward, so the original next node is lost.

Correct pattern:

```python
next_node = current.next
current.next = prev
prev = current
current = next_node
```

## 9. Traversal always moves the current node

Most linked-list operations use this structure:

```python
current = self.head

while current is not None:
    # use current.value
    current = current.next
```

If `current = current.next` is forgotten, the loop never moves forward.

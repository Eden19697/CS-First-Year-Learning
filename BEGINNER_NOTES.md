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

## 10. Every recursive function needs a base case

A recursive function that never stops calling itself will crash with a `RecursionError`.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Why:

- the base case (`n == 0`) stops the recursion
- the recursive case (`n * factorial(n - 1)`) must move toward the base case, not away from it

## 11. Binary search only works on a sorted list

```python
left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

Why:

- binary search decides which half to keep by comparing to the middle value
- that comparison only makes sense if the list is already sorted

## 12. O(n²) vs O(n log n) is about how work grows

Selection sort and insertion sort compare pairs of elements over and over, so the work grows roughly with `n * n`.

Merge sort splits the list in half at each level of recursion, so it only does about `log n` levels of work, each level touching all `n` elements: `n * log n`.

Why it matters:

- for small lists the difference barely shows
- for large lists, O(n log n) finishes far sooner than O(n²)

## 13. Tree recursion checks `root is None` first

Every recursive tree function needs an answer for an empty subtree.

```python
if root is None:
    return ...
```

The return value depends on the question:

```python
# traversal
return []

# node count or tree height
return 0

# search
return False

# balance check
return True
```

Without this base case, recursion eventually tries to access `root.value` when `root` is `None`.

## 14. Match the recursive operator to the question

```text
How many nodes?        Use +
Does a target exist?   Use or
How tall is the tree?  Use max
```

Examples:

```python
count = 1 + count_nodes(root.left) + count_nodes(root.right)
found = search_tree(root.left, target) or search_tree(root.right, target)
height = 1 + max(tree_height(root.left), tree_height(root.right))
```

## 15. A BST needs lower and upper bounds

Checking only direct children is not enough for BST validation. Every node must satisfy:

```text
lower < node.value < upper
```

When moving left, update `upper` to the current value. When moving right, update `lower` to the current value.

```python
is_valid_bst(root.left, lower, root.value)
is_valid_bst(root.right, root.value, upper)
```

## 16. BST deletion has three cases

After finding the node to delete:

```text
No children: return None
One child: return the existing child
Two children: replace with the minimum value in the right subtree,
              then delete that successor node
```

# Linked List Fundamentals

This chapter implements a basic singly linked list in Python. The goal was to move beyond Python's built-in `list` and practice how a linear data structure can be represented through objects and references.

## Structure

```text
head -> Node(value, next) -> Node(value, next) -> None
```

Each `Node` stores a value and a reference to the next node. `LinkedList.head` is the entry point for every traversal and update.

## Implemented Operations

| Method | Purpose | Time complexity |
| --- | --- | --- |
| `append(value)` | Add a value at the tail | O(n) |
| `prepend(value)` | Add a value at the head | O(1) |
| `display()` | Return values as a Python list | O(n) |
| `length()` | Count nodes | O(n) |
| `contains(value)` | Search for a value | O(n) |
| `delete(value)` | Remove the first matching node | O(n) |
| `reverse()` | Reverse all node links in place | O(n) |

`reverse()` uses O(1) extra space by maintaining three references: `prev`, `current`, and `next_node`.

## Edge Cases Practiced

- an empty linked list
- inserting the first node
- deleting the head node
- deleting a middle or tail node
- searching for a missing value
- reversing an empty or single-node list

## Run

From the repository root:

```bash
python3 03_linked_list/linked_list_basic.py
```

## Learning Reflection

The central challenge was understanding that linked-list operations change references rather than indexes. In particular, deletion requires reconnecting a node around the removed node, while reversal requires saving the original next node before redirecting the current link.

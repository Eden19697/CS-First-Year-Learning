# CS First Year Learning

This repository records my CS self-study with Python, organized chapter by chapter as I build my foundations.

The current chapters focus on basic data structures, data processing, stacks, queues, linked lists, recursion, and searching/sorting algorithms.

## Topics

- `list`
- `tuple`
- `dict`
- `set`
- sorting with `key`
- grouping records
- counting records
- filtering records
- ranking by calculated values
- stack operations
- queue operations
- bracket matching and error location
- singly linked list operations
- recursion (base case and recursive case)
- binary search
- selection sort, insertion sort, merge sort
- time complexity (O(n), O(n²), O(n log n), O(log n))

## Exercises

### Student Grade Analyzer

File:

```text
01_data_structures_basics/student_grade_analyzer.py
```

Practice goals:

- group scores by student
- calculate average scores
- find the best student
- find subject-level highest scores
- filter failed records
- rank students by average score

### Library Borrow Analyzer

File:

```text
01_data_structures_basics/library_borrow_analyzer.py
```

Practice goals:

- count borrow records by user
- calculate total borrowed days
- find the most active user
- count book categories
- filter long borrow records
- collect unique book titles

### Stack and Queue

Files:

```text
02_stack_queue/browser_history_stack.py
02_stack_queue/printer_queue.py
02_stack_queue/bracket_checker.py
02_stack_queue/bracket_error_locator.py
```

Practice goals:

- use a stack for browser back-history behavior
- use a queue to process print jobs in arrival order
- check whether brackets are balanced with a stack
- store bracket positions to report where an error occurs

### Linked List

Files:

```text
03_linked_list/linked_list_basic.py
03_linked_list/README.md
```

Practice goals:

- build a singly linked list with `Node` and `LinkedList` classes
- traverse nodes through `current = current.next`
- append and prepend values
- search for and delete a node safely
- reverse a linked list in place with `prev`, `current`, and `next_node`
- reason about empty-list and head-node edge cases

### Recursion, Searching, and Sorting

Files:

```text
04_recursion_search_sort/recursion_basic.py
04_recursion_search_sort/binary_search.py
04_recursion_search_sort/selection_sort.py
04_recursion_search_sort/insertion_sort.py
04_recursion_search_sort/merge_sort.py
04_recursion_search_sort/README.md
```

Practice goals:

- write recursive functions with a clear base case and recursive case
- search a sorted list with binary search in O(log n)
- sort with selection sort and insertion sort, and recognize their O(n²) behavior
- sort with merge sort by combining recursion and merging, achieving O(n log n)
- compare algorithm efficiency instead of only checking correctness

## How to Run

```bash
git clone https://github.com/Eden19697/CS-First-Year-Learning.git
cd CS-First-Year-Learning
python3 01_data_structures_basics/student_grade_analyzer.py
python3 01_data_structures_basics/library_borrow_analyzer.py
python3 02_stack_queue/browser_history_stack.py
python3 02_stack_queue/printer_queue.py
python3 02_stack_queue/bracket_checker.py
python3 02_stack_queue/bracket_error_locator.py
python3 03_linked_list/linked_list_basic.py
python3 04_recursion_search_sort/recursion_basic.py
python3 04_recursion_search_sort/binary_search.py
python3 04_recursion_search_sort/selection_sort.py
python3 04_recursion_search_sort/insertion_sort.py
python3 04_recursion_search_sort/merge_sort.py
```

## Learning Reflection

At this stage, I practiced moving from basic Python syntax to small data analysis tasks and core linear data structures.

The most important idea was learning to choose the right data structure:

- use `dict` for grouping and counting
- use `set` for uniqueness
- use `list` for ordered records
- use `sorted(..., key=...)` for ranking
- use a stack for last-in, first-out behavior
- use a queue for first-in, first-out behavior
- use node references to build and modify a linked structure
- use a base case and a recursive case to define a recursive function
- use binary search instead of linear search when a list is already sorted
- notice the difference between O(n²) sorting and O(n log n) sorting

This is the first part of a longer CS foundation learning process.

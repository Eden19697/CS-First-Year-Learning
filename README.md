# CS First Year Learning

This repository records my CS self-study with Python, organized chapter by chapter as I build my foundations.

The current chapters focus on basic data structures, data processing, linear data structures, recursion, searching/sorting algorithms, tree-based structures, hash tables, file I/O, object-oriented mini-projects, graphs, heaps/priority queues, and two pointers/sliding window.

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
- binary tree traversals and analysis
- breadth-first traversal with a queue
- binary search tree operations
- hash-table lookup with `dict` and `set`
- duplicate detection, counting, grouping, and set intersection
- reading and writing CSV files with the `csv` module
- reading and writing JSON files with the `json` module
- classes with instance state (`self.`), auto-incrementing ids, and linear search by id
- combining a class with JSON persistence to build a small working program
- graph representation with an adjacency list, DFS, BFS, and a visited set
- directed graphs, connected components, shortest path, and topological sort
- `heapq` min heaps, simulating a max heap with negation, and bounded "top-k" heaps
- Dijkstra's shortest path algorithm
- opposite-direction and slow/fast two-pointer patterns
- fixed-size and variable-size sliding windows

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

### Trees and Binary Search Trees

Files:

```text
05_trees/binary_tree_traversal.py
05_trees/binary_search_tree.py
05_trees/tree_review_drill.py
05_trees/README.md
```

Practice goals:

- implement preorder, inorder, postorder, and level-order traversal
- count nodes, calculate height, search a tree, and check balance
- implement BST insertion, search, minimum, maximum, validation, and deletion
- use lower and upper bounds to validate the full BST property
- distinguish recursive aggregation with `+`, `or`, and `max`

### Hash Tables

Files:

```text
06_hash_table/contains_duplicate.py
06_hash_table/two_sum.py
06_hash_table/valid_anagram.py
06_hash_table/group_anagrams.py
06_hash_table/intersection.py
06_hash_table/first_unique_char.py
06_hash_table/README.md
```

Practice goals:

- use a `set` for fast membership checks and duplicate detection
- use a `dict` to store counts or the index of a previously seen value
- group anagrams by using sorted letters as a shared key
- find common values with set-based lookup
- preserve original order when finding the first unique character

### Files (CSV and JSON)

Files:

```text
07_files_csv_json/csv_score_analyzer.py
07_files_csv_json/json_student_analyzer.py
07_files_csv_json/README.md
```

Practice goals:

- read rows from a CSV file with `csv.DictReader` and convert string values to numbers
- group and average scores by student, then write results back with `csv.writer`
- read nested records from a JSON file with `json.load`
- compute per-student averages and collect students with failing subjects
- write a structured summary back to disk with `json.dump`

### OOP Mini-Projects

Files:

```text
08_oop_projects/todo_manager.py
08_oop_projects/library_manager.py
08_oop_projects/README.md
```

Practice goals:

- store a list of dictionaries as instance state on `self.`
- generate ids automatically and keep them collision-free across saves and loads
- add, update, delete, and search records with a linear scan by id
- persist and reload an object's full state as JSON
- catch the classic `==` vs `=` bug, where a state update is silently skipped

### Graphs

Files:

```text
09_graphs/graph_traversal.py
09_graphs/directed_graph.py
09_graphs/island_count.py
09_graphs/topological_sort.py
09_graphs/README.md
```

Practice goals:

- represent a graph as an adjacency list, and build one from a list of edges
- implement DFS and BFS with a visited set to handle cycles
- check path existence, count connected components, and find shortest path with BFS
- build a directed graph, adding an edge in only one direction
- apply graph traversal to a 2D grid (island counting)
- implement topological sort with Kahn's algorithm (indegree counting + a queue)

### Heap / Priority Queue

Files:

```text
10_heap_priority_queue/heap_basic.py
10_heap_priority_queue/heapify_basic.py
10_heap_priority_queue/max_heap_basic.py
10_heap_priority_queue/k_largest.py
10_heap_priority_queue/kth_largest.py
10_heap_priority_queue/k_closest_points.py
10_heap_priority_queue/top_k_frequent.py
10_heap_priority_queue/priority_task_queue.py
10_heap_priority_queue/merge_k_sorted_arrays.py
10_heap_priority_queue/dijkstra_basic.py
10_heap_priority_queue/README.md
```

Practice goals:

- build and peek a min heap with `heapq.heappush`/`heappop`, and heapify an existing list in place
- simulate a max heap by pushing and popping negated values
- keep a bounded heap of size k to find the k largest/most frequent/closest items
- push comparison tuples like `(priority, name)` or `(distance, point)` so the heap orders by the right field
- wrap a heap in a class to build a priority task queue
- merge k sorted arrays and implement Dijkstra's shortest path with a heap

### Two Pointers / Sliding Window

Files:

```text
11_two_pointers_sliding_window/two_sum_sorted.py
11_two_pointers_sliding_window/valid_palindrome.py
11_two_pointers_sliding_window/remove_duplicates.py
11_two_pointers_sliding_window/max_sum_subarray_k.py
11_two_pointers_sliding_window/minimum_size_subarray_sum.py
11_two_pointers_sliding_window/longest_substring_without_repeat.py
11_two_pointers_sliding_window/review_drill.py
11_two_pointers_sliding_window/README.md
```

Practice goals:

- use opposite-direction pointers on a sorted array and for palindrome checks
- use slow/fast pointers to compact a sorted list in place
- use a fixed-size sliding window to find the max sum of any subarray of size k
- use a variable-size sliding window (expand right, shrink left in a `while`) for a minimum-length condition
- track a window's contents with a `set` to find the longest substring without repeats
- rewrite all four core templates from memory in a review drill

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
python3 05_trees/binary_tree_traversal.py
python3 05_trees/binary_search_tree.py
python3 05_trees/tree_review_drill.py
python3 06_hash_table/contains_duplicate.py
python3 06_hash_table/two_sum.py
python3 06_hash_table/valid_anagram.py
python3 06_hash_table/group_anagrams.py
python3 06_hash_table/intersection.py
python3 06_hash_table/first_unique_char.py
python3 08_oop_projects/todo_manager.py
python3 08_oop_projects/library_manager.py
python3 09_graphs/graph_traversal.py
python3 09_graphs/directed_graph.py
python3 09_graphs/island_count.py
python3 09_graphs/topological_sort.py
python3 10_heap_priority_queue/heap_basic.py
python3 10_heap_priority_queue/heapify_basic.py
python3 10_heap_priority_queue/max_heap_basic.py
python3 10_heap_priority_queue/k_largest.py
python3 10_heap_priority_queue/kth_largest.py
python3 10_heap_priority_queue/k_closest_points.py
python3 10_heap_priority_queue/top_k_frequent.py
python3 10_heap_priority_queue/priority_task_queue.py
python3 10_heap_priority_queue/merge_k_sorted_arrays.py
python3 10_heap_priority_queue/dijkstra_basic.py
python3 11_two_pointers_sliding_window/two_sum_sorted.py
python3 11_two_pointers_sliding_window/valid_palindrome.py
python3 11_two_pointers_sliding_window/remove_duplicates.py
python3 11_two_pointers_sliding_window/max_sum_subarray_k.py
python3 11_two_pointers_sliding_window/minimum_size_subarray_sum.py
python3 11_two_pointers_sliding_window/longest_substring_without_repeat.py
python3 11_two_pointers_sliding_window/review_drill.py
```

Chapter 07 reads and writes files using relative filenames, so it must be run from inside its own folder instead of the repository root:

```bash
cd 07_files_csv_json
python3 csv_score_analyzer.py
python3 json_student_analyzer.py
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
- use recursive structure and invariants to traverse and validate trees
- use a set when the key question is "have I seen this value?"
- use a dictionary when a value needs related information such as a count, index, or group
- read structured data with `csv.DictReader` / `json.load`, and remember CSV values arrive as strings
- round or transform a value before storing it, not by operating on the whole collection afterward
- store an object's state on `self.`, so every method shares the same data
- recompute an id counter after loading saved data, instead of trusting its `__init__` default
- double-check `==` vs `=` inside conditionals — a stray `==` silently does nothing instead of updating state
- mutate a dictionary directly (`graph[node].append(...)`) instead of a same-named local variable that never gets attached to it
- only add a directed edge in one direction; use a visited set whenever a graph or grid can revisit the same node
- reach for a heap instead of re-sorting when only the current min/max matters
- keep a bounded heap of size k when only "the best k so far" is needed
- keep peek/pop methods consistent about what they return — a wrapper method shouldn't leak the heap's raw internal tuple when its docstring promises just one field
- use opposite-direction pointers only on sorted (or symmetric) data; use slow/fast pointers to compact a list in place
- shrink a variable-size window with a `while` loop, not an `if`, since more than one shrink step may be needed

This is the first part of a longer CS foundation learning process.


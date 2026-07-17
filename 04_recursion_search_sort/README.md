# Recursion, Searching, and Sorting

This chapter moves from data structures to algorithms: writing recursive functions, searching a sorted list efficiently, and comparing three classic sorting algorithms by how they scale.

## Recursion Basics

File: `recursion_basic.py`

| Function | Base case | Recursive case |
| --- | --- | --- |
| `factorial(n)` | `n == 0` returns `1` | `n * factorial(n - 1)` |
| `sum_to_n(n)` | `n == 0` returns `0` | `n + sum_to_n(n - 1)` |

Every recursive function needs a base case that stops the recursion and a recursive case that shrinks the problem toward that base case.

## Binary Search

File: `binary_search.py`

`binary_search(numbers, target)` only works on an already-sorted list. It keeps `left` and `right` pointers and repeatedly checks the middle index, discarding half of the remaining search space each time.

| Case | Result |
| --- | --- |
| target found | return its index |
| target not found | return `-1` |

Time complexity: O(log n), since each step halves the search space.

## Sorting Algorithms

Files: `selection_sort.py`, `insertion_sort.py`, `merge_sort.py`

| Algorithm | Idea | Time complexity |
| --- | --- | --- |
| Selection sort | each round, find the smallest remaining value and swap it into place | O(n²) |
| Insertion sort | keep the left side sorted, insert each new value into its correct position | O(n²) |
| Merge sort | split in half recursively, then merge two sorted halves back together | O(n log n) |

Selection sort and insertion sort are simple but quadratic. Merge sort trades a bit of extra space for `O(n log n)` performance by combining recursion with a merge step.

## Edge Cases Practiced

- empty list and single-element list (all sort functions)
- already-sorted and reverse-sorted input
- target at the first index, last index, and not present at all (binary search)
- `n = 0` and `n = 1` base cases (recursion)

## Run

From the repository root:

```bash
python3 04_recursion_search_sort/recursion_basic.py
python3 04_recursion_search_sort/binary_search.py
python3 04_recursion_search_sort/selection_sort.py
python3 04_recursion_search_sort/insertion_sort.py
python3 04_recursion_search_sort/merge_sort.py
```

## Learning Reflection

The key shift in this chapter was thinking in terms of base case and recursive case instead of loops. Merge sort made the tradeoff between simplicity and efficiency concrete: selection sort and insertion sort are easier to write by hand, but they redo comparison work that merge sort avoids by dividing the problem in half at every level of recursion.

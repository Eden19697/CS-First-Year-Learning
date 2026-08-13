# Chapter 11: Two Pointers / Sliding Window

This chapter practices two closely related patterns: moving two indices toward each other (or at different
speeds) through a sequence, and expanding/shrinking a window over a sequence, both without nested loops.

## Core ideas

| Pattern | Best use | Example |
| --- | --- | --- |
| Opposite-direction pointers | Sorted data, or comparing from both ends | `left = 0; right = len(nums) - 1` |
| Slow/fast pointers | Compacting a list in place (e.g. removing duplicates) | `slow` marks the unique boundary, `fast` scans ahead |
| Fixed-size sliding window | "Every subarray of exactly size k" | add `nums[right]`, then drop `nums[right - k + 1]` once the window reaches size k |
| Variable-size sliding window | "Shortest/longest subarray satisfying a condition" | expand `right`, shrink `left` while the condition holds |

The shared idea: instead of re-scanning from scratch for every position (`O(n²)`), reuse the work already done by
sliding pointers forward, bringing most of these problems down to `O(n)`.

## Practice files

| File | Main pattern |
| --- | --- |
| `two_sum_sorted.py` | Opposite-direction pointers on a sorted array |
| `valid_palindrome.py` | Opposite-direction pointers comparing characters from both ends |
| `remove_duplicates.py` | Slow/fast pointers to compact a sorted list in place |
| `max_sum_subarray_k.py` | Fixed-size sliding window (size exactly k) |
| `minimum_size_subarray_sum.py` | Variable-size sliding window, shrink while a sum condition still holds |
| `longest_substring_without_repeat.py` | Variable-size sliding window with a `set` tracking the window's contents |
| `review_drill.py` | Rewrites the four core templates above from memory |

## A useful problem-solving template

Before writing code, ask:

1. Is the data sorted, or am I comparing from both ends? Reach for opposite-direction pointers.
2. Am I compacting/filtering a list in place? Reach for slow/fast pointers.
3. Does the window size stay fixed (exactly k)? Add the new right edge, drop the old left edge once size k is reached.
4. Does the window size change (shortest/longest satisfying a condition)? Expand `right` every step; shrink `left`
   in a `while` loop as long as the condition still holds.

## Run a practice file

From the repository root:

```bash
python3 11_two_pointers_sliding_window/two_sum_sorted.py
python3 11_two_pointers_sliding_window/valid_palindrome.py
python3 11_two_pointers_sliding_window/remove_duplicates.py
python3 11_two_pointers_sliding_window/max_sum_subarray_k.py
python3 11_two_pointers_sliding_window/minimum_size_subarray_sum.py
python3 11_two_pointers_sliding_window/longest_substring_without_repeat.py
python3 11_two_pointers_sliding_window/review_drill.py
```

## Common reminders

- Opposite-direction pointers only make sense on **sorted** data (or when comparing symmetric ends like a
  palindrome) — on unsorted data, moving `left`/`right` based on a sum comparison doesn't mean anything.
- For a fixed-size window, do the "add new / update result / remove old" three steps in that exact order, and only
  once the window has actually reached size k (`right >= k - 1`).
- For a variable-size window, the shrink step is a `while` loop, not an `if` — you may need to shrink several
  times in a row before the window is valid again.
- A window's length is `right - left + 1`, not `right - left` — it's easy to be off by one.

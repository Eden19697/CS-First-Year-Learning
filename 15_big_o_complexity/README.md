# 15. Big-O Complexity

This chapter connects code structure to worst-case time complexity and extra
space complexity. The goal is to identify *why* an operation costs what it does,
not only to memorize labels such as O(n) or O(n log n).

## Files

| File | Focus |
| --- | --- |
| `big_o_examples.py` | Worked examples for one-pass scans, set-based duplicate checks, sorting, binary search, nested loops, and repeated binary searches. |
| `big_o_review_drill.py` | A practice drill for predicting complexity, then rebuilding the core patterns from memory. |

## Key patterns

| Code structure | Typical time | Typical extra space |
| --- | --- | --- |
| One pass through a list | O(n) | O(1) when only a few variables are kept |
| One pass plus a set | O(n) average | O(n) |
| Sorting a copied list | O(n log n) | O(n) with `sorted(...)` |
| Binary search on sorted data | O(log n) | O(1) |
| A nested pair loop | O(n²) | O(1) |
| A binary search inside an n-item loop | O(n log n) | O(1) |

## Run the chapter

From the repository root:

```bash
python3 15_big_o_complexity/big_o_examples.py
python3 15_big_o_complexity/big_o_review_drill.py
```

## Review checklist

1. State whether the question asks for time, extra space, or both.
2. Identify whether operations are sequential (add) or nested (multiply).
3. Check for sorting, hashing, or a repeatedly halved search range.
4. Keep the dominant term for Big-O, but retain the reason that creates it.

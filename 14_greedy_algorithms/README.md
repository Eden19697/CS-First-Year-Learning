# 14. Greedy Algorithms

This chapter introduces greedy algorithms: make the best local choice that can
be proven to lead to a correct global result. Greedy algorithms are often
short, but the important question is always **why the choice is safe**.

## Files

| File | Problem | Greedy choice |
| --- | --- | --- |
| `interval_scheduling.py` | Select the most non-overlapping intervals | Choose the available interval that ends first. |
| `greedy_coin_change.py` | Produce a greedy coin choice | Take the largest usable coin first. This is not always optimal. |
| `assign_cookies.py` | Satisfy the maximum number of children | Give the smallest suitable cookie to the least demanding child. |
| `jump_game.py` | Decide whether the final index is reachable | Track the furthest reachable index. |
| `min_arrows_balloons.py` | Burst every balloon interval with fewest arrows | Shoot at the earliest possible ending position. |
| `partition_labels.py` | Split a string into maximum valid partitions | Extend the partition to the last occurrence of every included character. |
| `best_time_stock.py` | Maximize one buy/sell stock transaction | Track the lowest earlier price and best profit. |
| `greedy_review_drill.py` | Rewrite the core patterns from memory | Explain the greedy invariant before coding. |

## Run the chapter

Run any example from the repository root:

```bash
python3 14_greedy_algorithms/interval_scheduling.py
python3 14_greedy_algorithms/greedy_review_drill.py
```

## Key habits

1. State the local greedy choice in one sentence.
2. Identify the state that proves progress, such as `last_end`, `farthest`, or
   `lowest_price`.
3. Test empty input and boundary-touching intervals.
4. Do not assume every greedy rule is optimal: coin change needs a proof or a
   restricted coin system; otherwise dynamic programming may be required.

# Chapter 12: Dynamic Programming Intro

This chapter practices the core DP habit: define what `dp[i]` means, write the base case(s), write the
transition, then (optionally) compress the table down to a couple of variables once the pattern is clear.

## Core ideas

| Step | Question to ask | Example (`house_robber`) |
| --- | --- | --- |
| Define `dp[i]` | What does one entry in the table represent? | "max money from the first i houses" |
| Base case(s) | What are the smallest inputs I already know the answer to? | `dp[0] = 0`, `dp[1] = nums[0]` |
| Transition | How does `dp[i]` build on smaller subproblems? | `dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])` |
| Space optimization | Do I ever need more than the last 1-2 entries? | keep `prev1`/`prev2` instead of the full list |

The shared idea: a problem has overlapping subproblems and optimal substructure when the brute-force recursive
solution keeps recomputing the same smaller cases. Storing each subproblem's answer once (in a list, or in a
couple of variables) turns exponential recursion into linear time.

## Practice files

| File | Main pattern |
| --- | --- |
| `fibonacci_dp.py` | Plain recursion vs. DP list vs. two-variable DP, side by side |
| `climbing_stairs.py` | Counting paths with a Fibonacci-shaped recurrence |
| `min_cost_climbing_stairs.py` | Minimum-cost variant, `dp[i] = min(...)` instead of `dp[i] = dp[i-1] + dp[i-2]` |
| `house_robber.py` | Choosing "skip" vs. "take" at each step under a non-adjacency constraint |
| `coin_change_intro.py` | Unbounded choice at each step (any coin, reused any number of times), minimizing a count |
| `dp_review_drill.py` | Rewrites all five patterns above from memory in one file |

## A useful problem-solving template

Before writing code, ask:

1. What does `dp[i]` mean, in one sentence? If you can't say it plainly, the recurrence won't make sense either.
2. What are the base case(s) — the smallest `i` where the answer is obvious without any transition?
3. How does `dp[i]` combine smaller subproblems: a sum (`climbing_stairs`), a min/max over choices
   (`house_robber`, `min_cost_climbing_stairs`), or a min/max over every possible coin/item (`coin_change_intro`)?
4. Once the list version is correct, does the transition only ever look back 1-2 steps? If so, replace the list
   with a couple of variables.

## Run a practice file

From the repository root:

```bash
python3 12_dynamic_programming_intro/fibonacci_dp.py
python3 12_dynamic_programming_intro/climbing_stairs.py
python3 12_dynamic_programming_intro/min_cost_climbing_stairs.py
python3 12_dynamic_programming_intro/house_robber.py
python3 12_dynamic_programming_intro/coin_change_intro.py
python3 12_dynamic_programming_intro/dp_review_drill.py
```

## Common reminders

- `dp[i]` almost always means "the answer using the first `i` items/steps," not "the answer at index `i`" — off-by-one
  mistakes usually come from mixing these two up.
- A "skip vs. take" choice (`house_robber`) needs a `max`; a "cheapest way in" choice
  (`min_cost_climbing_stairs`, `coin_change_intro`) needs a `min`.
- For unbounded choice problems like `coin_change_intro`, the inner loop tries *every* coin at each amount — the
  answer isn't decided by a single "best" coin up front.
- Initialize a min-seeking DP table with `float("inf")` (not `0`), so any real transition can only make it
  smaller, and an untouched entry stays recognizably "unreachable."
- Space-optimizing to two variables only works once you've confirmed the transition never looks back more than
  2 steps — check this before deleting the list version.

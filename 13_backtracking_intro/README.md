# Chapter 13: Backtracking Intro

This chapter practices the backtracking shape: explore a choice, recurse, then undo that choice before trying the
next one. Every problem here reduces to answering the same four questions before writing any code.

## Core ideas

| Question | What it means | Example (`combination_sum`) |
| --- | --- | --- |
| What do the recursive parameters mean? | What state does each call carry forward? | `start_index` (where choices may resume), `remaining` (how much target is left) |
| What is the base case? | When is a path complete (or dead)? | `remaining == 0` → save it; `remaining < 0` → dead end |
| What is the choice? | What gets tried at each step? | append one candidate to `path` |
| What must be undone? | What has to be reset before the next branch? | `path.pop()` after the recursive call returns |

The shared idea: a backtracking function tries a choice, recurses one level deeper, and then **undoes** that exact
choice (`path.pop()`, `used[i] = False`, `visited.remove(...)`) so the next branch starts from a clean slate. This
"choose → explore → un-choose" pattern is what makes it possible to enumerate every valid path with one function.

## Practice files

| File | Main pattern |
| --- | --- |
| `subsets.py` | Every element has two choices: skip it or include it |
| `subsets_practice.py` | Rewrite of `subsets.py` from memory |
| `permutations.py` | Every element must be used exactly once, in every order, tracked with a `used` list |
| `combination_sum.py` | Candidates may be reused — recurse with the *same* index |
| `combination_sum_once.py` | Each candidate position used at most once — recurse with `index + 1` |
| `generate_parentheses.py` | Two constrained choices (`(` and `)`) instead of one binary choice per element |
| `phone_letter_combinations.py` | Choices come from a lookup table (`phone[digit]`) instead of a fixed list |
| `word_search.py` | Backtracking over a 2D grid with a `visited` set instead of a 1D `path` |
| `backtracking_review_drill.py` | Rewrites all seven patterns above from memory in one file |

## A useful problem-solving template

Before writing code, ask:

1. What does each recursive parameter mean, in one sentence?
2. What is the base case — when is `path` a complete (or invalid) answer?
3. Can each item be reused (`combination_sum`, same index) or used at most once (`combination_sum_once`,
   `permutations`, index + 1 / a `used` list)?
4. Does every mutation before the recursive call (`path.append`, `used[i] = True`, `visited.add(...)`) have a
   matching undo line after it?

## Run a practice file

From the repository root:

```bash
python3 13_backtracking_intro/subsets.py
python3 13_backtracking_intro/subsets_practice.py
python3 13_backtracking_intro/permutations.py
python3 13_backtracking_intro/combination_sum.py
python3 13_backtracking_intro/combination_sum_once.py
python3 13_backtracking_intro/generate_parentheses.py
python3 13_backtracking_intro/phone_letter_combinations.py
python3 13_backtracking_intro/word_search.py
python3 13_backtracking_intro/backtracking_review_drill.py
```

## Common reminders

- Every `append`/`add`/`mark used` before a recursive call needs a matching `pop`/`remove`/`unmark` after it — a
  missing undo silently leaks state into sibling branches.
- "May be reused" (`combination_sum`) recurses with the *same* `start_index`; "used at most once"
  (`combination_sum_once`, `permutations`) recurses with `index + 1` or a `used` list — mixing these up either
  drops valid answers or creates duplicates.
- `word_search`'s `visited` set is scoped to the *current path only* — it gets a cell added right before exploring
  and removed right after, so the same cell can be reused by a different, later path.
- A base case that saves a result doesn't always need to `return` immediately afterward if the rest of the
  function independently guarantees no further real work happens (see `combination_sum`, where any deeper call
  after `remaining == 0` hits `remaining < 0` on its very next step) — but it's worth tracing through why that's
  safe rather than assuming it.

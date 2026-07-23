# Chapter 06: Hash Tables

This chapter practices Python hash-table tools: dictionaries (`dict`) and sets (`set`).
They are useful when we need a fast lookup, a count, or a way to group related values.

## Core ideas

| Tool | Best use | Example |
| --- | --- | --- |
| `set` | Membership checks and removing duplicates | `if number in seen:` |
| `dict` | Store a value by a key | `counts[char] = counts.get(char, 0) + 1` |
| sorted-string key | Group anagrams | `"".join(sorted(word))` |

Both `set` and `dict` usually support lookup in **O(1)** average time. This is why they are often faster than scanning a list repeatedly.

## Practice files

| File | Main pattern |
| --- | --- |
| `contains_duplicate.py` | Track seen numbers with a `set` |
| `two_sum.py` | Store each number and its index in a `dict` |
| `valid_anagram.py` | Count characters and compare the counts |
| `group_anagrams.py` | Use the sorted letters as a dictionary key |
| `intersection.py` | Use sets to keep only common values |
| `first_unique_char.py` | Count first, then scan again in original order |

## A useful problem-solving template

Before writing code, ask:

1. Do I need to know whether I have seen an item before? Use a `set`.
2. Do I need to remember extra information for an item, such as its count or index? Use a `dict`.
3. Do several values belong to the same category? Make a dictionary where each value is a list.

## Run a practice file

From the repository root:

```bash
python3 06_hash_table/two_sum.py
```

Or replace `two_sum.py` with any other practice filename in this folder.

## Common reminders

- A set has no fixed order, so do not rely on the order of a converted set.
- `dict.get(key, default)` lets you safely start a new count at zero.
- Do not name a variable `dict`, `list`, or `set`; those names are built-in Python tools.
- For anagrams, characters and their frequencies must both match.

# Common Beginner Notes

Short reminders collected while practicing the early chapters in this repository.

## Hash Tables: `set` and `dict`

### Use the right tool for the question

- Use a `set` when you only need fast membership checks or unique values.
- Use a `dict` when each key needs associated information, such as a count, index, or list of grouped values.

```python
seen = set()
counts = {}
```

### Save an updated count back into the dictionary

This expression calculates a new value but does not store it:

```python
counts.get(char, 0) + 1
```

Store the result instead:

```python
counts[char] = counts.get(char, 0) + 1
```

### Do not rely on a set's order

A set is good for membership and uniqueness, but it is not a tool for preserving an order. If a problem asks for the *first* unique character, first count characters, then loop through the original string again.

```python
for char in text:
    if counts[char] == 1:
        return char
```

### Do not overwrite Python built-in names

Avoid variable names such as `dict`, `list`, `set`, or `int`. They hide Python's built-in tools and make code harder to read.

```python
character_counts = {}
number_set = set()
```

### One-pass lookup pattern

For problems such as Two Sum, check whether the needed value was already seen *before* saving the current value. This prevents using the same element twice.

```python
needed = target - value
if needed in seen:
    return [seen[needed], index]
seen[value] = index
```

## Files: CSV and JSON

### CSV values come back as strings

Even a column that looks numeric, like `"85"`, is read as a string. Convert it before doing math:

```python
score = int(row["score"])
```

### `round()` works on one number, not a whole dictionary

Round each value *as it is stored*, not by calling `round()` on the finished dictionary — a `dict` has no
`__round__` method and raises a `TypeError`.

```python
# Wrong: round(averages) fails, averages is a dict
averages[name] = average
return round(averages)

# Right: round the single number before storing it
averages[name] = round(average, 2)
return averages
```

### "At least one" means `> 0`, not `> 1`

A condition meant to catch "failed at least one subject" must use `> 0` (or just check truthiness). Using `> 1`
silently drops anyone who only failed exactly one thing.

```python
if failed_subject:        # correct: true for 1 or more items
    failed[name] = failed_subject
```


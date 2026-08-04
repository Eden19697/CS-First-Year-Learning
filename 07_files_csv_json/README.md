# Chapter 07: Files (CSV and JSON)

This chapter practices reading and writing two common file formats: CSV (`csv` module) and JSON (`json` module).
They are used for loading real-world data and saving computed results back to disk.

## Core ideas

| Format | Best use | Example |
| --- | --- | --- |
| CSV | Table-like, flat records (rows and columns) | `csv.DictReader(file)` |
| JSON | Nested data (objects inside objects, lists of objects) | `json.load(file)` |

Both formats read values back as **strings or Python-native types straight from the file** — CSV values always come back
as strings and often need converting (`int(...)`, `float(...)`), while JSON preserves types (numbers stay numbers,
`true`/`false`/`null` map to `True`/`False`/`None`).

| JSON | Python |
| --- | --- |
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

## Practice files

| File | Main pattern |
| --- | --- |
| `csv_score_analyzer.py` | Read rows with `csv.DictReader`, group and average scores, write results back with `csv.writer` |
| `json_student_analyzer.py` | Read nested student records with `json.load`, compute per-student averages and failing subjects, write a summary with `json.dump` |

## A useful problem-solving template

Before writing code, ask:

1. Is the data flat rows-and-columns, or nested with sub-objects? That decides CSV vs JSON.
2. Do values need converting after reading? CSV always hands back strings; JSON usually doesn't.
3. Am I filtering ("who failed"), grouping ("scores per student"), or both?

## Run a practice file

From the repository root:

```bash
python3 07_files_csv_json/csv_score_analyzer.py
python3 07_files_csv_json/json_student_analyzer.py
```

## Common reminders

- CSV values are always read as strings — convert with `int()` or `float()` before doing math on them.
- `round(x, 2)` rounds one number; it cannot be called on a whole `dict`. Round each value *while storing it*,
  not after the dictionary is already built.
- A filter condition like "at least one failed subject" means `len(failed_subject) > 0` (or simply
  `if failed_subject:`) — not `> 1`, which would silently skip anyone who failed exactly one thing.
- Open files with `with open(...) as file:` so they close automatically, and pass `newline=""` when writing CSV
  files to avoid extra blank lines on some platforms.

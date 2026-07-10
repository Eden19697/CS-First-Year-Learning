# CS First Year: Data Structures Basics

This repository records the first stage of my CS self-study with Python.

The focus of this stage is learning how to use basic Python data structures to analyze small records and solve beginner-level data processing problems.

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

## How to Run

```bash
cd "/Users/eden1969/Documents/CS-First-Year-Data-Structures-Basics/01_data_structures_basics"
python3 student_grade_analyzer.py
python3 library_borrow_analyzer.py
```

## Learning Reflection

At this stage, I practiced moving from basic Python syntax to small data analysis tasks.

The most important idea was learning to choose the right data structure:

- use `dict` for grouping and counting
- use `set` for uniqueness
- use `list` for ordered records
- use `sorted(..., key=...)` for ranking

This is the first part of a longer CS foundation learning process.


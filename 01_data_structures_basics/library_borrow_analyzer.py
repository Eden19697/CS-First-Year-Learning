"""
Library Borrow Analyzer
=======================

This is your second data structures practice exercise.

You will practice:
- list
- tuple
- dict
- set
- sorting
- functions
- clean code
- edge cases

Each record has this format:

    (user, book, category, days)

Example:

    ("Alice", "Python Basics", "Programming", 12)

Meaning:
- user: the person who borrowed the book
- book: the book title
- category: the book category
- days: how many days the book was borrowed


Tasks
-----

1. Count how many books each user borrowed.

Expected output example:

    {
        "Alice": 3,
        "Bob": 3,
        "Charlie": 2,
        "David": 2
    }


2. Calculate each user's total borrowed days.

Expected output example:

    {
        "Alice": 38,
        "Bob": 57,
        "Charlie": 35,
        "David": 37
    }


3. Find the user with the highest total borrowed days.

Expected output example:

    Top borrower: Bob, total days: 57

Think about this edge case:
- What if two or more users have the same highest total days?


4. Count how many times each category was borrowed.

Expected output example:

    {
        "Programming": 4,
        "Self-help": 2,
        "AI": 3,
        "Psychology": 1
    }


5. Find all records where borrowed days are more than 20.

Rule:
- days > 20

Expected output example:

    [
        ("Charlie", "Deep Learning", "AI", 25),
        ("David", "Thinking Fast and Slow", "Psychology", 30),
        ("Bob", "Deep Learning", "AI", 22)
    ]


6. Rank users by total borrowed days from highest to lowest.

Expected output example:

    [
        ("Bob", 57),
        ("Alice", 38),
        ("David", 37),
        ("Charlie", 35)
    ]


7. Collect all unique book titles.

Requirement:
- Use a set.

Expected output example:

    {
        "Python Basics",
        "Clean Code",
        "Atomic Habits",
        "Deep Learning",
        "The Pragmatic Programmer",
        "Thinking Fast and Slow",
        "Machine Learning Yearning"
    }


Suggested function structure
----------------------------

def count_books_by_user(records):
    ...

def calculate_total_days_by_user(records):
    ...

def find_top_borrowers(total_days):
    ...

def count_by_category(records):
    ...

def find_long_borrow_records(records, limit=20):
    ...

def rank_users_by_total_days(total_days):
    ...

def collect_unique_books(records):
    ...

def main():
    ...


Edge cases to think about
-------------------------

- What if records is empty?
- What if there is only one user?
- What if multiple users have the same highest total days?
- What if a category appears only once?
- What if no record is longer than 20 days?
- What if every record is longer than 20 days?
- What if the same book appears multiple times?


How to run this file
--------------------

In terminal:

    cd "/Users/eden1969/Documents/CS First yeat/student_grade_analyzer"
    python3 library_borrow_analyzer.py
"""


records = [
    ("Alice", "Python Basics", "Programming", 12),
    ("Bob", "Clean Code", "Programming", 20),
    ("Alice", "Atomic Habits", "Self-help", 8),
    ("Charlie", "Deep Learning", "AI", 25),
    ("Bob", "The Pragmatic Programmer", "Programming", 15),
    ("David", "Thinking Fast and Slow", "Psychology", 30),
    ("Alice", "Machine Learning Yearning", "AI", 18),
    ("Charlie", "Python Basics", "Programming", 10),
    ("David", "Atomic Habits", "Self-help", 7),
    ("Bob", "Deep Learning", "AI", 22),
]


def count_books_by_user(records):
    # TODO: Use a dictionary to count how many records each user has.
    dic_times = {}
 
    for name, book, cata, days in records:
        if name not in dic_times:#先创建
            dic_times[name] = 0

        dic_times[name] += 1#再加和

    return dic_times        


def calculate_total_days_by_user(records):
    # TODO: Use a dictionary to add up borrowed days for each user.
    total_days = {}

    for name, book, cata, days in records:
        if name not in total_days:
            total_days[name] = 0
        
        total_days[name] += days

    return total_days


def find_top_borrowers(total_days):
    # TODO: Find the highest total days.
    # Think about whether you want to return one user or multiple users.
    if not total_days:
        return None
    
    highest = max(total_days.values())
    top_borrowers = []

    for name, days in total_days.items():
        if days == highest:
            top_borrowers.append(name)

    return top_borrowers, highest



def count_by_category(records):
    # TODO: Use a dictionary to count how many times each category appears.
    dic_cata = {}

    for name, book, cata, days in records:
        if cata not in dic_cata:
            dic_cata[cata] = 0
        
        dic_cata[cata] += 1
    
    return dic_cata


def find_long_borrow_records(records, limit=20):
    # TODO: Return all records where days is greater than limit.
    list_long = []
    for name, book, cata, days in records:
        if days > limit:
            tuple_a = (name, book, cata,days)
            list_long.append(tuple_a)
    return list_long



def rank_users_by_total_days(total_days):
    # TODO: Sort users by total borrowed days from high to low.
    ranking = sorted(
        total_days.items(),
        key = lambda item:item[1],
        reverse= True
    )

    return ranking


def collect_unique_books(records):
    # TODO: Use a set to collect all unique book titles.
    s = set()
    for name, book, cata, days in records:
        if book not in s:
            s.add(book)

    return s


def main():
    # TODO: Call your functions here and print the results.
    dic_a = count_books_by_user(records)
    print(dic_a)

    dic_b = calculate_total_days_by_user(records)
    print(dic_b)

    dic_c = count_by_category(records)
    print(dic_c)

    list_a = find_long_borrow_records(records, limit=20)
    print(list_a)

    ranking = rank_users_by_total_days(dic_b)
    print(ranking)

    set = collect_unique_books(records)
    print(set)


    


if __name__ == "__main__":
    main()

"""
Student Grade Analyzer
======================

This is a data structures practice exercise.

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

    (name, subject, score)

Example:

    ("Alice", "Math", 85)

Tasks
-----

1. Calculate each student's average score.

Expected output example:

    {
        "Alice": 85.0,
        "Bob": 71.33,
        "Charlie": 91.5,
        "David": 62.5
    }

The average score should be rounded to 2 decimal places.


2. Find the student with the highest average score.

Expected output example:

    Top student: Charlie, average score: 91.5

Think about this edge case:
- What if two or more students have the same highest average?


3. Calculate the highest score for each subject.

Expected output example:

    {
        "Math": 95,
        "Physics": 91,
        "Chemistry": 79
    }


4. Find all failed records.

Rule:
- A score lower than 70 is failed.

Expected output example:

    [
        ("Bob", "Physics", 68),
        ("David", "Math", 60),
        ("David", "Physics", 65)
    ]


5. Rank students by average score from highest to lowest.

Expected output example:

    [
        ("Charlie", 91.5),
        ("Alice", 85.0),
        ("Bob", 71.33),
        ("David", 62.5)
    ]


Suggested function structure
----------------------------

def calculate_student_averages(records):
    ...

def find_top_student(averages):
    ...

def calculate_subject_highest_scores(records):
    ...

def find_failed_records(records, pass_score=70):
    ...

def rank_students(averages):
    ...

def main():
    ...


Edge cases to think about
-------------------------

- What if records is empty?
- What if there is only one student?
- What if multiple students have the same highest average?
- What if a subject appears only once?
- What if every student passes?
- What if every student fails?


How to run this file
--------------------

In terminal:

    cd "/Users/eden1969/Documents/CS First yeat/student_grade_analyzer"
    python3 student_grade_analyzer.py
"""


records = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 72),
    ("Alice", "Physics", 91),
    ("Charlie", "Math", 95),
    ("Bob", "Physics", 68),
    ("Alice", "Chemistry", 79),
    ("Charlie", "Physics", 88),
    ("Bob", "Chemistry", 74),
    ("David", "Math", 60),
    ("David", "Physics", 65),
]


def calculate_student_averages(records):
    # TODO: Use a dictionary to group scores by student.
    dic_group = {}
    for name, subject, score in records:
        if name not in dic_group:
            dic_group[name] = []
        
        dic_group[name].append(score)
    print(dic_group)
    # Then calculate each student's average score.
    averages = {}
    for name, scores in dic_group.items():
        average = sum(scores)/len(scores)
        averages[name] = round(average,2)
    
    return averages

    


def find_top_student(averages):
    # TODO: Find the highest average score.
    if not averages:
        return None
    
    highest = max(averages.values())
    Top_student = []

    for person in averages:
        if averages[person] == highest:
            Top_student.append(person)
    
    return Top_student,highest
    # Think about whether you want to return one student or multiple students.
    


def calculate_subject_highest_scores(records):
    # TODO: Use a dictionary to store the highest score for each subject.
    dic_sub = {}
    
    for name, subject, score in records:
        if subject not in dic_sub:
            dic_sub[subject] = score
        elif dic_sub[subject] < score:
            dic_sub[subject] = score
    return dic_sub
        


def find_failed_records(records, pass_score=70):
    # TODO: Return all records where score is lower than pass_score.
    fail_list = []
    for name, subject, score in records:
        if score < pass_score:
            fail_list.append((name, subject, score))
    return fail_list


def rank_students(averages):
    # TODO: Sort students by average score from high to low.
    ranking = sorted(
        averages.items(),
        key=lambda item: item[1],
        #排序的时候，对于每一个 student_item，都拿 student_item[1] 作为排序依据。
        reverse=True
    )

    return ranking

def main():
    # TODO: Call your functions here and print the results.
    averages = calculate_student_averages(records)
    print(averages)

    top_student, highest = find_top_student(averages)
    print(f"Top student: {top_student}, average score: {highest}")

    dic_a = calculate_subject_highest_scores(records)
    print(dic_a)

    dic_b = find_failed_records(records, pass_score=70)
    print(dic_b)
    
    rankings = rank_students(averages)
    print(rankings)

if __name__ == "__main__":
    main()

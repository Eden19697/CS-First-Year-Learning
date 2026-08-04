"""
JSON Practice: Student Analyzer
===============================

Goal:
Practice reading and writing JSON files.


CSV vs JSON
-----------

CSV is good for table-like data:

    name,subject,score
    Alice,Math,85

JSON is good for nested data:

    {
        "name": "Alice",
        "scores": {
            "Math": 85,
            "Physics": 91
        }
    }


Python and JSON mapping
-----------------------

JSON object  -> Python dict
JSON array   -> Python list
JSON string  -> Python str
JSON number  -> Python int or float
JSON true    -> Python True
JSON false   -> Python False
JSON null    -> Python None


Files
-----

Read:

    students.json

Write:

    student_summary.json


Tasks
-----

1. read_students_json(filename)

Read students.json and return Python data.


2. calculate_json_averages(students)

Calculate each student's average score.

Expected result:

    {
        "Alice": 85.0,
        "Bob": 71.33,
        "Charlie": 91.5,
        "David": 62.5
    }


3. find_json_failed_students(students, pass_score=70)

Return students who have at least one failed subject.

Expected result:

    {
        "Bob": ["Physics"],
        "David": ["Math", "Physics"]
    }


4. write_summary_json(filename, averages, failed_students)

Write a JSON file like:

    {
        "averages": {
            "Alice": 85.0,
            "Bob": 71.33
        },
        "failed_students": {
            "Bob": ["Physics"]
        }
    }


Expected output
---------------

Loaded students: [...]
{'Alice': 85.0, 'Bob': 71.33, 'Charlie': 91.5, 'David': 62.5}
{'Bob': ['Physics'], 'David': ['Math', 'Physics']}
Wrote summary to student_summary.json
"""


import json


def read_students_json(filename):
    # TODO: Open filename in read mode.
    with open(filename,"r") as file:
    # TODO: Use json.load(file) to read JSON into Python data.
        data = json.load(file)
    # TODO: Return the data.
    return data
    


def calculate_json_averages(students):
    # TODO: Create averages dictionary.
    averages = {}
    # TODO: Loop through each student.
    for student in students:
        # TODO: Get student name.
        name = student["name"]
        # TODO: Get scores dictionary.
        scores = student["scores"]
        # TODO: Calculate average from scores.values().
        average = sum(scores.values())/len(scores)#.values()用来找出字典里所有 values
        # TODO: Store rounded average.
        averages[name] = round(average, 2)
    # TODO: Return averages.
    return averages


def find_json_failed_students(students, pass_score=70):
    # TODO: Create failed_students dictionary.
    failed = {}
    # TODO: Loop through each student.
    for student in students:
        # TODO: Check each subject and score.
        name = student["name"]
        scores = student["scores"]

        failed_subject = []
        # TODO: If score is lower than pass_score, record subject.
        for subject, score in scores.items():
            if score < pass_score:
                failed_subject.append(subject)

        # TODO: Only add student to failed_students if they failed at least one subject.
        if failed_subject:
            failed[name] = failed_subject
    # TODO: Return failed_students.
    return failed


def write_summary_json(filename, averages, failed_students):
    # TODO: Create summary dictionary with averages and failed_students.
    summary = {
        "averages" : averages,
        "failed_students" : failed_students
    }
    # TODO: Open filename in write mode.
    with open(filename,"w", encoding="utf-8") as file:
        
    # TODO: Use json.dump(summary, file, indent=4).
        json.dump(summary, file, indent=4)
    # 是把这个字典写进文件，并且用 4 个空格缩进，让 JSON 文件看起来工整。

def main():
    students = read_students_json("students.json")
    averages = calculate_json_averages(students)
    failed_students = find_json_failed_students(students)

    print("Loaded students:", students)
    print(averages)
    print(failed_students)

    write_summary_json("student_summary.json", averages, failed_students)
    print("Wrote summary to student_summary.json")


if __name__ == "__main__":
    main()

"""
CSV Practice: Student Score Analyzer
====================================

Goal:
Practice reading data from a CSV file and analyzing it with dictionaries.


CSV file
--------

We will read this file:

    student_scores.csv

It contains:

    name,subject,score
    Alice,Math,85
    Bob,Math,72
    ...


Important idea
--------------

When Python reads from a CSV file, values usually start as strings.

For example:

    "85"

You need to convert score to int:

    int(row["score"])


Tasks
-----

1. read_scores(filename)

Read the CSV file and return records in this format:

    [
        ("Alice", "Math", 85),
        ("Bob", "Math", 72),
        ...
    ]


2. calculate_student_averages(records)

Calculate each student's average score.

Expected result:

    {
        "Alice": 85.0,
        "Bob": 71.33,
        "Charlie": 91.5,
        "David": 62.5
    }


3. find_failed_records(records, pass_score=70)

Return all records with score lower than pass_score.


4. write_averages(filename, averages)

Write student averages into a new CSV file.

Expected output file:

    student_averages.csv

Example content:

    name,average
    Alice,85.0
    Bob,71.33
    Charlie,91.5
    David,62.5


5. read_averages(filename)

Read the generated averages CSV file and return a dictionary:

    {
        "Alice": 85.0,
        "Bob": 71.33,
        "Charlie": 91.5,
        "David": 62.5
    }

Important:

CSV values are read as strings, so average should be converted with float().


Expected output
---------------

[('Alice', 'Math', 85), ('Bob', 'Math', 72), ...]
{'Alice': 85.0, 'Bob': 71.33, 'Charlie': 91.5, 'David': 62.5}
[('Bob', 'Physics', 68), ('David', 'Math', 60), ('David', 'Physics', 65)]
Wrote averages to student_averages.csv
{'Alice': 85.0, 'Bob': 71.33, 'Charlie': 91.5, 'David': 62.5}
"""


import csv


def read_scores(filename):
    # TODO: Create an empty records list.
    records = []
    # TODO: Open the CSV file.
    with open(filename,"r") as file:
     #打开文件，并把它临时叫做 file。
     #代码块结束后，Python 自动帮你关闭文件。
     
    # TODO: Use csv.DictReader(file) to read rows as dictionaries.
        reader = csv.DictReader(file)
    # TODO: For each row, get name, subject, and score.
        for row in reader:
            name = row["name"]
            subject = row["subject"]
            
    # TODO: Convert score to int.
            score = int(row["score"])
    # TODO: Append (name, subject, score) to records.
            records.append((name, subject, score))
    # TODO: Return records.
    return records


def calculate_student_averages(records):
    # TODO: Group scores by student using a dictionary.
    grouped = {}
    for obj in records:
        if obj[0] not in grouped:
            grouped[obj[0]] = []

        grouped[obj[0]].append(obj[2])
    # TODO: Calculate average for each student.
    for name, score in grouped.items():
        avg = round(sum(score)/len(score),2)
        grouped[name] = avg
    # TODO: Round average to 2 decimal places.
    return grouped
    
    


def find_failed_records(records, pass_score=70):
    # TODO: Return all records where score is lower than pass_score.
    fail = []
    for name, subject, score in records:
        if score < pass_score:
            fail.append((name, subject, score))
    return fail


def write_averages(filename, averages):
    # TODO: Open filename in write mode.
    with open(filename, "w", newline="" ) as file:#newline avoid csv format problem
    # TODO: Create a csv.writer.
        writer = csv.writer(file)
    # TODO: Write header row: name, average.
        writer.writerow(["name","average"])#writerow stands for write one row
    # TODO: Write each student and average.
        for name, averages in averages.items():
            writer.writerow([name, averages])


def read_averages(filename):
    # TODO: Create an empty dictionary.
    averages = {}

    # TODO: Open filename in read mode.
    with open(filename,"r") as file:
        # TODO: Use csv.DictReader(file).
        reader = csv.DictReader(file)

        # TODO: For each row, read name and average.
        for row in reader:
            name = row["name"]
            average = float(row["average"])

            # TODO: Convert average to float.
            averages[name] = average

            # TODO: Store name -> average in dictionary.
            

    # TODO: Return dictionary.
    return averages


def main():
    records = read_scores("student_scores.csv")
    averages = calculate_student_averages(records)

    print(records)
    print(averages)
    print(find_failed_records(records))

    write_averages("student_averages.csv", averages)
    print("Wrote averages to student_averages.csv")
    print(read_averages("student_averages.csv"))


if __name__ == "__main__":
    main()

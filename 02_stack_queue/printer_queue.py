"""
Queue Practice: Printer Queue
=============================

Goal:
Practice queue using Python list.

A queue follows this rule:

    First In, First Out

That means:
- The first job added to the queue should be printed first.
- New jobs are added to the end of the queue.
- The printer removes jobs from the front of the queue.

You will practice:
- class
- __init__
- list
- append
- pop(0)
- method
- edge cases


Task
----

Create a class called PrinterQueue.

It should support these methods:


1. add_job(job)

Add a print job to the end of the queue.

Example:

    printer.add_job("essay.pdf")
    printer.add_job("homework.docx")
    printer.add_job("photo.png")

The internal queue should become:

    ["essay.pdf", "homework.docx", "photo.png"]


2. print_next()

Print the next job in the queue.

Rules:

- If the queue is not empty:
    remove the first job
    return "Printing: job_name"

- If the queue is empty:
    return "No jobs to print"

Example:

    printer = PrinterQueue()

    printer.add_job("essay.pdf")
    printer.add_job("homework.docx")

    print(printer.print_next())
    # Printing: essay.pdf

    print(printer.print_next())
    # Printing: homework.docx

    print(printer.print_next())
    # No jobs to print


3. current_queue()

Return the current queue.

Example:

    printer.add_job("essay.pdf")
    printer.add_job("homework.docx")

    print(printer.current_queue())
    # ["essay.pdf", "homework.docx"]


Expected behavior
-----------------

printer = PrinterQueue()

print(printer.current_queue())
# []

printer.add_job("essay.pdf")
printer.add_job("homework.docx")
printer.add_job("photo.png")

print(printer.current_queue())
# ["essay.pdf", "homework.docx", "photo.png"]

print(printer.print_next())
# Printing: essay.pdf

print(printer.print_next())
# Printing: homework.docx

print(printer.current_queue())
# ["photo.png"]

print(printer.print_next())
# Printing: photo.png

print(printer.print_next())
# No jobs to print

print(printer.current_queue())
# []


Suggested structure
-------------------

class PrinterQueue:
    def __init__(self):
        # TODO: Create an empty list to store print jobs
        pass

    def add_job(self, job):
        # TODO: Add job to the end of queue
        pass

    def print_next(self):
        # TODO: Print and remove the first job in queue
        pass

    def current_queue(self):
        # TODO: Return current queue
        pass


def main():
    printer = PrinterQueue()

    print(printer.current_queue())

    printer.add_job("essay.pdf")
    printer.add_job("homework.docx")
    printer.add_job("photo.png")

    print(printer.current_queue())

    print(printer.print_next())
    print(printer.print_next())

    print(printer.current_queue())

    print(printer.print_next())
    print(printer.print_next())

    print(printer.current_queue())


if __name__ == "__main__":
    main()
"""


class PrinterQueue:
    def __init__(self):
        # TODO: Create an empty list to store print jobs
        self.jobs = []

    def add_job(self, job):
        # TODO: Add job to the end of queue
        self.jobs.append(job)

    def print_next(self):
        # TODO: Print and remove the first job in queue
        if len(self.jobs) == 0:
            return "No jobs to print"
        first = self.jobs.pop(0)
        return "Printing:" + first

    def current_queue(self):
        # TODO: Return current queue
        return self.jobs


def main():
    printer = PrinterQueue()

    print(printer.current_queue())

    printer.add_job("essay.pdf")
    printer.add_job("homework.docx")
    printer.add_job("photo.png")

    print(printer.current_queue())

    print(printer.print_next())
    print(printer.print_next())

    print(printer.current_queue())

    print(printer.print_next())
    print(printer.print_next())

    print(printer.current_queue())


if __name__ == "__main__":
    main()

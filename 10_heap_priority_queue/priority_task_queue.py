"""
Priority task queue with heapq.

Core idea:
- Use a min heap to store tasks.
- Each item is a tuple: (priority, task_name)
- Smaller priority number means higher priority.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 priority_task_queue.py
"""

import heapq


class PriorityTaskQueue:
    """
    Manage tasks by priority.

    Example:
    queue.add_task("fix bug", 1)
    queue.add_task("write notes", 3)
    queue.pop_task() -> "fix bug"
    """

    def __init__(self):
        # TODO: create an empty heap to store tasks
        self.heap = []

    def add_task(self, task_name, priority):
        """
        Add a task.

        Hint:
        - store (priority, task_name) in the heap
        """
        # TODO: write your code here
        heapq.heappush(self.heap, (priority, task_name))
        return

    def pop_task(self):
        """
        Remove and return the highest priority task name.

        Edge case:
        - if the queue is empty, return None

        Hint:
        - heappop returns (priority, task_name)
        - return only task_name
        """
        # TODO: write your code here
        if not self.heap:
            return None
        info = heapq.heappop(self.heap)
        return info[1]

    def peek_task(self):
        """
        Return the highest priority task name without removing it.

        Edge case:
        - if the queue is empty, return None
        """
        # TODO: write your code here
        if not self.heap:
            return None
        return self.heap[0][1]

    def is_empty(self):
        """
        Return True if there are no tasks.
        Otherwise return False.
        """
        # TODO: write your code here
        if not self.heap:
            return True
        return False


def main():
    queue = PriorityTaskQueue()

    queue.add_task("write notes", 3)
    queue.add_task("fix bug", 1)
    queue.add_task("review code", 2)

    print("Peek:", queue.peek_task())
    print("Pop:", queue.pop_task())
    print("Pop:", queue.pop_task())
    print("Pop:", queue.pop_task())
    print("Pop from empty:", queue.pop_task())
    print("Is empty:", queue.is_empty())

    print("\nExpected:")
    print("Peek: fix bug")
    print("Pop: fix bug")
    print("Pop: review code")
    print("Pop: write notes")
    print("Pop from empty: None")
    print("Is empty: True")


if __name__ == "__main__":
    main()

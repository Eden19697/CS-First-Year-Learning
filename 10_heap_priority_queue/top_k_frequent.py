"""
Find the top k frequent numbers.

Core idea:
- Use a dict to count frequency.
- Use a min heap to keep only the top k frequent numbers.

Run:
cd "/Users/eden1969/Documents/CS First years/10_heap_priority_queue"
python3 top_k_frequent.py
"""

import heapq


def count_numbers(numbers):
    """
    Count how many times each number appears.

    Example:
    [1, 1, 1, 2, 2, 3]

    Return:
    {
        1: 3,
        2: 2,
        3: 1
    }

    Hint:
    - create counts = {}
    - loop through numbers
    - use counts.get(number, 0) + 1
    """
    # TODO: write your code here
    counts = {}
    for number in numbers:
            counts[number] = counts.get(number,0) + 1
            #从字典 counts 里面拿 number 对应的次数；
            #如果 number 还不存在，就当它之前出现了 0 次；
            #然后再 + 1。
    return counts



def top_k_frequent(numbers, k):
    """
    Return the k most frequent numbers.

    Example:
    numbers = [1, 1, 1, 2, 2, 3]
    k = 2
    return [1, 2]

    Edge cases:
    - if k <= 0, return []
    - if numbers is empty, return []

    Hint:
    - first call count_numbers(numbers)
    - create heap = []
    - loop through counts.items()
    - push (count, number) into heap
    - if len(heap) > k, pop one value
    - return the numbers from the heap
    """
    # TODO: write your code here
    if k <= 0:
         return []
    if not numbers:
         return []
    heap = []
    dic = count_numbers(numbers)
    for key,value in dic.items():
        heapq.heappush(heap,(value,key))
        if len(heap) > k:
             heapq.heappop(heap)
    result = []
    for count, number in heap:
         result.append(number)
    return result
        


def main():
    numbers = [1, 1, 1, 2, 2, 3]

    print("Numbers:", numbers)
    print("k = 2:", top_k_frequent(numbers, 2))
    print("k = 1:", top_k_frequent(numbers, 1))
    print("k = 0:", top_k_frequent(numbers, 0))
    print("empty:", top_k_frequent([], 2))

    print("\nExpected:")
    print("k = 2 -> [1, 2] in any order")
    print("k = 1 -> [1]")
    print("k = 0 -> []")
    print("empty -> []")


if __name__ == "__main__":
    main()

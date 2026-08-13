"""
Remove duplicates from a sorted array.

Core idea:
- Use slow and fast pointers.
- fast scans every number.
- slow marks the end of the unique part.

Run:
cd "/Users/eden1969/Documents/CS First years/11_two_pointers_sliding_window"
python3 remove_duplicates.py
"""


def remove_duplicates(nums):
    """
    Remove duplicates in place from a sorted list.

    Return:
    - the length of the unique part

    Example:
    nums = [1, 1, 2, 2, 3]
    return 3
    nums becomes [1, 2, 3, 2, 3]
    The unique part is nums[:3] -> [1, 2, 3]

    Edge cases:
    - if nums is empty, return 0
    - if nums has one number, return 1

    Hint:
    - slow = 0
    - fast starts from 1
    - when nums[fast] != nums[slow]:
        - slow += 1
        - nums[slow] = nums[fast]
    - return slow + 1
    """
    # TODO: write your code here
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    
    slow = 0
    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


def main():
    nums1 = [1, 1, 2, 2, 3]
    length1 = remove_duplicates(nums1)
    print("Length:", length1)
    print("Unique part:", nums1[:length1])

    nums2 = [1, 2, 3]
    length2 = remove_duplicates(nums2)
    print("Length:", length2)
    print("Unique part:", nums2[:length2])

    nums3 = []
    length3 = remove_duplicates(nums3)
    print("Length:", length3)
    print("Unique part:", nums3[:length3])

    print("\nExpected:")
    print("Length: 3, Unique part: [1, 2, 3]")
    print("Length: 3, Unique part: [1, 2, 3]")
    print("Length: 0, Unique part: []")


if __name__ == "__main__":
    main()

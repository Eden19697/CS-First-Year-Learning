"""Greedy practice 6: partition a string into the most valid parts."""


def partition_labels(text):
    """
    Return the size of each partition.

    Each letter may appear in at most one partition.
    Return as many partitions as possible.

    Example:
    partition_labels("ababcbacadefegdehijhklij") returns [9, 7, 8].
    The partitions are: "ababcbaca", "defegde", "hijhklij".

    Greedy idea:
    A partition cannot end before the last occurrence of every letter inside it.
    Keep extending the current partition's ending boundary as needed.
    """
    # TODO: return [] for an empty string.
    if not text:
        return []
    # TODO: build last_index.
    # last_index[character] should store the final index of that character in text.
    last_index = {}
    for index, char in enumerate(text):
        last_index[char] = index

    # TODO: create result, start, and end.
    # start: start index of the current partition.
    # end: furthest last position that the current partition must include.
    result = []
    start = 0
    end = 0

    # TODO: loop through text with enumerate.
    # - update end using the last index of the current character
    # - when index == end, the current partition can safely end here
    #   append its length, then move start to index + 1
    for i, char in enumerate(text):
        end = max(end, last_index[char])

        if i == end:
            result.append(i - start + 1)
            start = i + 1

    return result


if __name__ == "__main__":
    print(partition_labels(""))
    # Expected: []

    print(partition_labels("eccbbbbdec"))
    # Expected: [10]

    print(partition_labels("ababcbacadefegdehijhklij"))
    # Expected: [9, 7, 8]

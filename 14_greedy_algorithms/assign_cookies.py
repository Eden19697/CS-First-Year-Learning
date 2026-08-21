"""Greedy practice 3: assign cookies to content children."""


def find_content_children(greed, cookies):
    """
    Return the maximum number of children who can be satisfied.

    greed[i] is the smallest cookie size child i will accept.
    Each cookie can be assigned to at most one child.

    Example:
    find_content_children([1, 2, 3], [1, 1]) returns 1.
    find_content_children([1, 2], [1, 2, 3]) returns 2.

    Greedy idea:
    Give the smallest available cookie to the least demanding child
    who can accept it. Do not waste a large cookie on an easy-to-satisfy child.
    """
    # TODO: sort greed and cookies from small to large.
    # TODO: create child_index and cookie_index, both starting at 0.
    # TODO: while both indexes are in range:
    # - if cookies[cookie_index] >= greed[child_index], satisfy this child
    #   and move child_index forward
    # - always move cookie_index forward because this cookie is now considered
    # TODO: return child_index; it equals the number of satisfied children.
    sorted_kid = sorted(greed)
    sorted_cookie = sorted(cookies)

    cookie_index = 0
    child_index = 0

    for i in range(min(len(sorted_cookie),len(sorted_kid))):
        if sorted_cookie[cookie_index] >= sorted_kid[child_index]:
            child_index += 1
        cookie_index += 1
    return child_index


if __name__ == "__main__":
    print(find_content_children([1, 2, 3], [1, 1]))
    # Expected: 1

    print(find_content_children([1, 2], [1, 2, 3]))
    # Expected: 2

    print(find_content_children([2, 3, 4], [1, 2, 3]))
    # Expected: 2

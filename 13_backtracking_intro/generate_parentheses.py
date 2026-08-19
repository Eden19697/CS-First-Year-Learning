"""Backtracking practice 5: generate valid parentheses."""


def generate_parentheses(n):
    """
    Return every valid string made from n pairs of parentheses.

    Example:
    generate_parentheses(2) returns ["(())", "()()"]

    State:
    - path: parentheses chosen so far
    - open_count: how many "(" have been used
    - close_count: how many ")" have been used

    Rules:
    - add "(" only when open_count < n
    - add ")" only when close_count < open_count
      (A closing bracket cannot appear before its matching opening bracket.)
    - a completed answer has length 2 * n
    """
    # TODO: handle n < 0 if you choose to support it.
    if n < 0:
        return False
    # TODO: create result and path.
    result = []
    path = []

    # TODO: define backtrack(open_count, close_count).
    # Base case: len(path) == 2 * n.
    # Save "".join(path), then return.
    def backtrack(open_count, close_count):
        if len(path) == 2 * n:
            result.append("".join(path))
            return
    # Choice 1: append "(" if open_count < n.
    # Recurse with open_count + 1, then pop.
        if open_count < n:
            path.append("(")
            backtrack(open_count +1, close_count)
            path.pop()


    # Choice 2: append ")" if close_count < open_count.
    # Recurse with close_count + 1, then pop.
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count+1)
            path.pop()

    # TODO: call backtrack(0, 0), then return result.
    backtrack(0,0)
    return result


if __name__ == "__main__":
    print(generate_parentheses(0))
    # Expected: [""]

    print(generate_parentheses(1))
    # Expected: ["()"]

    print(generate_parentheses(2))
    # Expected: ["(())", "()()"]

    print(generate_parentheses(3))
    # Expected: ["((()))", "(()())", "(())()", "()(())", "()()()"]

"""Backtracking practice 7: search for a word in a grid."""


def exists_word(grid, word):
    """
    Return True if word can be formed from adjacent cells in grid.

    Moves are allowed up, down, left, and right.
    A cell may not be used twice on the same path.

    Example grid:
    [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    exists_word(grid, "ABCCED") returns True.

    State:
    - row, col: current cell position
    - index: which character of word we need to match now
    - visited: cells used on the current path only
    """
    # TODO: choose how to handle an empty word and an empty grid.
    # TODO: create visited = set().
    visited = set()
    rows = len(grid)
    cols = len(grid[0])

    # TODO: define dfs(row, col, index).
    def dfs(row, col, index):
    # Suggested checking order:
    # 1. if index == len(word), return True
        if index == len(word):
            return True
    # 2. if row/col is outside grid, return False
        if row >= rows or row < 0 or col >= cols or col < 0:
            return False
    # 3. if (row, col) is visited, return False
        if (row, col) in visited:
            return False
    # 4. if grid[row][col] != word[index], return False
        if grid[row][col] != word[index]:
            return False
    # 5. add (row, col) to visited
        visited.add((row, col))
    # 6. try the four directions with index + 1
        found = ( dfs(row+1, col, index+1)
        or dfs(row-1, col, index+1)
        or dfs(row, col+1, index+1)
        or dfs(row, col-1, index+1)
        )
    # 7. remove (row, col) from visited before returning False
        visited.remove((row, col))
        return found

    # TODO: try dfs(row, col, 0) from every cell in grid.
    # Return True as soon as one starting cell finds the whole word.
    # Return False if every starting cell fails.
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]

    print(exists_word(board, "ABCCED"))  # Expected: True
    print(exists_word(board, "SEE"))     # Expected: True
    print(exists_word(board, "ABCB"))    # Expected: False

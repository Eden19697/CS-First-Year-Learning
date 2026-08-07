"""
Graph Practice: Island Count
============================

Goal:
Practice graph traversal on a 2D grid.


Problem
-------

You are given a grid:

    L means land
    W means water

Example:

    grid = [
        ["W", "L", "W", "W"],
        ["W", "L", "L", "W"],
        ["W", "W", "L", "W"],
        ["L", "W", "W", "L"],
    ]


Connection rule
---------------

Land cells are connected only in four directions:

    up
    down
    left
    right

Diagonal does not count.


Task
----

Write:

    count_islands(grid)
    minimum_island(grid)


Return the number of islands.

An island is a connected group of land cells.

minimum_island(grid) should return the size of the smallest island.

If there is no island, return 0.


Graph idea
----------

Each land cell is like a graph node.

Its neighbors are nearby land cells:

    (row - 1, col)
    (row + 1, col)
    (row, col - 1)
    (row, col + 1)


Important
---------

Use a visited set.

Store positions as tuples:

    visited.add((row, col))


Expected output
---------------

3
0
1
1
0
4
"""


def count_islands(grid):
    # TODO: Create visited set.
    visited = set()
    # TODO: Create island count.
    island_count = 0

    rows = len(grid)
    cols = len(grid[0])

    # TODO: Loop through every row and col.
    def explore(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 
        
        if grid[row][col] == "W":
            return
        
        if (row, col) in visited:
            return 
        
        visited.add((row, col))

        explore(row + 1, col)  # 下
        explore(row - 1, col)  # 上
        explore(row, col + 1)  # 右
        explore(row, col - 1)  # 左

        # TODO: If this cell starts a new island, increase count.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "L" and (row, col) not in visited:
                island_count += 1
                explore(row, col)

        # TODO: Use DFS to mark the whole island visited.

    # TODO: Return island count.
    return island_count


def minimum_island(grid):
    # TODO: Create visited set.
    visited = set()
    # TODO: Track smallest island size.
    smallest = None
    rows = len(grid)
    cols = len(grid[0])
    # TODO: Write helper that returns island size.
    def explore(row, col):
        # TODO: If out of bounds, return 0.
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 0
        # TODO: If water, return 0.
        if grid[row][col] == "W":
            return 0
        # TODO: If already visited, return 0.
        if (row, col) in visited:
            return 0
        # TODO: Mark visited.
        visited.add((row,col))
        # TODO: Return 1 plus sizes from four directions.
        return (1 + explore(row + 1, col) + # 下
        explore(row - 1, col) + # 上
        explore(row, col + 1) + # 右
        explore(row, col - 1)  )# 左 
    # TODO: Loop through every row and col.
    for row in range(rows):
        for col in range(cols):
        # TODO: If cell is land and not visited, explore size.
            if grid[row][col] == "L" and (row, col) not in visited:
                size = explore(row,col)
        # TODO: Update smallest.
                if smallest is None or size < smallest:
                    smallest = size
    # TODO: If no island was found, return 0.
    if smallest == None:
        return 0
    # TODO: Return smallest.
    return smallest


def main():
    grid1 = [
        ["W", "L", "W", "W"],
        ["W", "L", "L", "W"],
        ["W", "W", "L", "W"],
        ["L", "W", "W", "L"],
    ]

    grid2 = [
        ["W", "W"],
        ["W", "W"],
    ]

    grid3 = [
        ["L", "L"],
        ["L", "L"],
    ]

    print(count_islands(grid1))
    print(count_islands(grid2))
    print(count_islands(grid3))
    print(minimum_island(grid1))
    print(minimum_island(grid2))
    print(minimum_island(grid3))


if __name__ == "__main__":
    main()

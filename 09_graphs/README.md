# Chapter 09: Graphs

This chapter practices graph representation and traversal: adjacency lists, DFS, BFS, directed graphs, grid-based
"island" problems, and topological sort.

## Core ideas

| Concept | What it means here | Example |
| --- | --- | --- |
| Adjacency list | Each node maps to a list of its neighbors | `{"Alice": ["Bob", "Charlie"]}` |
| Visited set | Prevents infinite loops on graphs with cycles | `if neighbor not in visited:` |
| DFS | Go deep before coming back (recursion or a stack) | `helper(neighbor)` |
| BFS | Visit level by level (a queue) | `queue.pop(0)` |
| Directed edge | One-way only — only add `graph[a].append(b)`, never the reverse | course prerequisites, web links |
| Topological sort (Kahn's algorithm) | Process nodes whose indegree is 0 first, peeling the graph layer by layer | course scheduling |

## Practice files

| File | Main pattern |
| --- | --- |
| `graph_traversal.py` | DFS, BFS, path existence, connected components, shortest path, building a graph from edges, largest component |
| `directed_graph.py` | Build a directed adjacency list, check reachability following edge direction only |
| `island_count.py` | DFS on a 2D grid, treating each land cell as a graph node connected to its 4 neighbors |
| `topological_sort.py` | Kahn's algorithm: indegree counting + a queue of ready nodes |

## A useful problem-solving template

Before writing code, ask:

1. Is the graph undirected or directed? That decides whether an edge gets added to both nodes' lists or just one.
2. Do I need every node visited (DFS/BFS/components), or just "is there a path" (early return once found)?
3. Does the problem ask for order with dependencies? That's topological sort, not plain DFS/BFS.
4. Is the "graph" secretly a grid? Each cell is a node; its 4 (or 8) neighbors are its edges.

## Run a practice file

From the repository root:

```bash
python3 09_graphs/graph_traversal.py
python3 09_graphs/directed_graph.py
python3 09_graphs/island_count.py
python3 09_graphs/topological_sort.py
```

## Common reminders

- When building an adjacency list, mutate the dictionary itself (`graph[node_a].append(node_b)`), not a
  same-named local variable — assigning `a = []` inside an `if` block creates a throwaway local, and the graph
  never actually gets populated even though the function looks like it's building one.
- For a directed graph, only add the edge in one direction. Undirected graphs need both `graph[a].append(b)`
  and `graph[b].append(a)`.
- A visited set is required any time the graph (or grid) can revisit the same node — without it, a cycle causes
  infinite recursion or an infinite loop.
- Topological sort only works cleanly on a DAG (a directed graph with no cycle); there can be more than one
  valid ordering, so compare against "does this respect dependencies," not an exact list match.

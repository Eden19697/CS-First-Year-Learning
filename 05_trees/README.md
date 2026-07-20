# Trees and Binary Search Trees

This chapter practices recursive tree algorithms and the ordering rules that make a binary search tree efficient.

## Binary Tree Structure

```text
        10
       /  \
      5    20
     / \
    3   7
```

Each `TreeNode` stores a value plus references to `left` and `right` children. Every recursive function treats `root is None` as its base case.

## Binary Tree Operations

| Operation | Main idea | Time complexity |
| --- | --- | --- |
| Preorder | root, left, right | O(n) |
| Inorder | left, root, right | O(n) |
| Postorder | left, right, root | O(n) |
| Count nodes | current node + two subtree counts | O(n) |
| Height | 1 + maximum subtree height | O(n) |
| Search | current node or either subtree | O(n) |
| Level order | process nodes breadth-first with a queue | O(n) with `deque` |
| Balance check | compare subtree heights at every node | O(n^2) in this introductory implementation |

The educational `level_order` implementation uses a Python list with `pop(0)`. For a large production queue, `collections.deque` would avoid the cost of removing from the front.

## Binary Search Tree Operations

A binary search tree (BST) maintains this invariant:

```text
left subtree values < node value < right subtree values
```

The implementation includes:

- insertion and value-guided search
- inorder traversal, which produces sorted values for a valid BST
- minimum and maximum lookup
- full BST validation with lower and upper bounds
- deletion for zero, one, and two-child nodes

Average-case BST search, insertion, and deletion are O(log n). In a highly unbalanced BST, they can become O(n).

## Edge Cases Practiced

- an empty tree
- a single-node tree
- searching for a missing value
- an unbalanced tree
- an invalid BST with a value in the wrong subtree
- deleting a leaf, a one-child node, and a two-child node

## Run

From the repository root:

```bash
python3 05_trees/binary_tree_traversal.py
python3 05_trees/binary_search_tree.py
python3 05_trees/tree_review_drill.py
```

## Learning Reflection

This chapter reinforced that recursive functions need a precise base case and an operator that matches the question: `+` for counts, `or` for existence, and `max` for height. The BST exercises added an important invariant: a valid tree must respect lower and upper bounds across entire subtrees, not just at direct children.

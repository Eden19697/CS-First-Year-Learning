"""
Tree Practice: Binary Tree Traversal
====================================

Goal:
Practice the basic idea of a binary tree and recursive traversal.


Linked list vs binary tree
--------------------------

A linked list node has one next pointer:

    value
    next

A binary tree node has two child pointers:

    value
    left
    right


TreeNode example
----------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


Example tree
------------

We will manually create this tree:

        10
       /  \
      5    20
     / \
    3   7


Vocabulary
----------

root:
    The first node of the tree.

left child:
    The node on the left side.

right child:
    The node on the right side.

leaf:
    A node with no children.


Task
----

Write three traversal functions:

    preorder(root)
    inorder(root)
    postorder(root)

Then write two basic tree analysis functions:

    count_nodes(root)
    tree_height(root)

Then write one tree search function:

    search_tree(root, target)

Then write one BFS traversal function:

    level_order(root)

Then write one balance-checking function:

    is_balanced(root)


1. Preorder traversal
---------------------

Order:

    root -> left -> right

Expected result:

    [10, 5, 3, 7, 20]


2. Inorder traversal
--------------------

Order:

    left -> root -> right

Expected result:

    [3, 5, 7, 10, 20]


3. Postorder traversal
----------------------

Order:

    left -> right -> root

Expected result:

    [3, 7, 5, 20, 10]


4. Count nodes
--------------

Return how many nodes are in the tree.

For this tree:

        10
       /  \
      5    20
     / \
    3   7

There are 5 nodes.

Recursive idea:

    count_nodes(root) = 1 + count_nodes(root.left) + count_nodes(root.right)

Base case:

    if root is None:
        return 0


5. Tree height
--------------

Return the height of the tree.

Definition for this exercise:

- Empty tree height is 0.
- A tree with only root has height 1.

For this tree:

        10        level 1
       /  \
      5    20     level 2
     / \
    3   7         level 3

The height is 3.

Recursive idea:

    tree_height(root) = 1 + max(tree_height(root.left), tree_height(root.right))

Base case:

    if root is None:
        return 0


6. Search tree
--------------

Return True if target exists anywhere in the tree.
Return False if target does not exist.

Example:

    search_tree(root, 7)
    # True

    search_tree(root, 99)
    # False

Recursive idea:

    if root.value == target:
        return True

    return search_tree(root.left, target) or search_tree(root.right, target)

Base case:

    if root is None:
        return False


7. Level order traversal
------------------------

This is also called BFS, breadth-first search.

It visits the tree level by level.

For this tree:

        10
       /  \
      5    20
     / \
    3   7

The result should be:

    [10, 5, 20, 3, 7]

Core idea:

Use a queue.

Start:

    queue = [root]

Repeat:

    remove the first node from queue
    add its value to result
    add its left child to queue if it exists
    add its right child to queue if it exists


8. Balanced tree
----------------

Return True if the tree is balanced.
Return False if the tree is not balanced.

Definition for this exercise:

A tree is balanced if every node's left subtree height and right subtree height
differ by no more than 1.

Example balanced tree:

        10
       /  \
      5    20
     / \
    3   7

Example unbalanced tree:

        10
       /
      5
     /
    3
   /
  1

Simple recursive idea:

    if root is None:
        return True

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)


Important recursion idea
------------------------

Base case:

    if root is None:
        return []

Recursive case:

    combine current root value with traversal result from left and right.


Expected output
---------------

[10, 5, 3, 7, 20]
[3, 5, 7, 10, 20]
[3, 7, 5, 20, 10]
5
3
True
False
[10, 5, 20, 3, 7]
True
False
"""


class TreeNode:
    def __init__(self, value):
        # TODO: Store the node value.
        self.value = value

        # TODO: Store the left child.
        self.left = None

        # TODO: Store the right child.
        self.right = None


def preorder(root):
    # TODO: Base case. If root is None, return [].
    if root == None:
        return []
    # TODO: Return root value, then preorder left, then preorder right.
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    # TODO: Base case. If root is None, return [].
    if root == None:
        return []
    # TODO: Return inorder left, then root value, then inorder right.
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    # TODO: Base case. If root is None, return [].
    if root == None:
        return []
    # TODO: Return postorder left, then postorder right, then root value.
    return postorder(root.left) + postorder(root.right) + [root.value] 


def count_nodes(root):
    # TODO: Base case. If root is None, return 0.
    if root == None:
        return 0
    # TODO: Count current node + nodes in left subtree + nodes in right subtree.
    return len(preorder(root))


def tree_height(root):
    # TODO: Base case. If root is None, return 0.
    if root == None:
        return 0
    # TODO: Return 1 + max height of left and right subtree.
    return 1 + max(tree_height(root.left), tree_height(root.right))


def search_tree(root, target):
    # TODO: Base case. If root is None, return False.
    if root == None:
        return False
    # TODO: If root.value equals target, return True.
    if root.value == target:
        return True
    # TODO: Search left subtree or right subtree.
    return search_tree(root.left, target) or search_tree(root.right, target)
#问“有几个”用 +
#问“有没有”用 or


def level_order(root):
    # TODO: If root is None, return [].
    if root is None:
        return []
    # TODO: Create result list.
    result= []
    # TODO: Create queue with root inside.
    queue = [root]
    # TODO: While queue is not empty:
    while len(queue) > 0:
        # TODO: Remove the first node from queue.
        node = queue.pop(0)
        # TODO: Add node.value to result.
        result.append(node.value)
        # TODO: If node.left exists, append it to queue.
        if node.left is not None:
            queue.append(node.left)
        # TODO: If node.right exists, append it to queue.
        if node.right is not None:
            queue.append(node.right)

    # TODO: Return result.
    return result


def is_balanced(root):
    # TODO: If root is None, return True.
    if root is None:
        return True
    # TODO: Calculate left height and right height.
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    # TODO: If the difference is greater than 1, return False.
    if abs(left_height-right_height) > 1:
        return False
    # TODO: Check whether left subtree and right subtree are also balanced.
    return is_balanced(root.left) and is_balanced(root.right)


def build_sample_tree():
    # TODO: Create root node with value 10.
    root = TreeNode(10)
    # TODO: Add left child 5 and right child 20.
    left_child = TreeNode(5)
    right_child = TreeNode(20)
    root.left = left_child
    root.right = right_child
    # TODO: Add 3 and 7 under node 5.
    left_child_G2 = TreeNode(3)
    right_child_G2 = TreeNode(7)
    left_child.left = left_child_G2
    left_child.right = right_child_G2
    # TODO: Return root.
    return root


def build_unbalanced_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(1)
    return root


def main():
    root = build_sample_tree()
    unbalanced_root = build_unbalanced_tree()

    print(preorder(root))
    print(inorder(root))
    print(postorder(root))
    print(count_nodes(root))
    print(tree_height(root))
    print(search_tree(root, 7))
    print(search_tree(root, 99))
    print(level_order(root))
    print(is_balanced(root))
    print(is_balanced(unbalanced_root))


if __name__ == "__main__":
    main()

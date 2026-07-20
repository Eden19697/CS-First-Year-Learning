r"""
Tree Practice: Binary Search Tree
=================================

Goal:
Practice binary search tree insertion and search.


Binary tree vs binary search tree
---------------------------------

A normal binary tree only means:

    each node has left and right children

A binary search tree, also called BST, has an extra rule:

    left subtree values < root value
    right subtree values > root value


Example BST
-----------

        10
       /  \
      5    20
       / \\   /
    3   7 15


Why this matters
----------------

In a normal binary tree search, you may need to search both sides:

    search left OR search right

In a BST, you can use value comparison:

    if target < root.value:
        only search left

    if target > root.value:
        only search right


Task
----

Write:

    bst_insert(root, value)
    bst_search(root, target)
    inorder(root)
    find_min(root)
    find_max(root)
    is_valid_bst(root)
    bst_delete(root, value)


1. bst_insert(root, value)
--------------------------

Insert value into the BST and return the root.

Rules:

- If root is None:
      create and return a new TreeNode

- If value < root.value:
      insert into root.left

- If value > root.value:
      insert into root.right

- If value == root.value:
      do nothing for this exercise


2. bst_search(root, target)
---------------------------

Return True if target exists in the BST.
Return False if target does not exist.

Rules:

- If root is None:
      return False

- If target == root.value:
      return True

- If target < root.value:
      search left only

- If target > root.value:
      search right only


3. inorder(root)
----------------

Return inorder traversal as a list.

For a valid BST, inorder traversal should return values in sorted order.


4. find_min(root)
-----------------

Return the smallest value in the BST.

BST rule:

    smaller values are always on the left

So the minimum value is the leftmost node.

Rules:

- If root is None:
      return None

- Otherwise:
      start from root
      keep moving left while current.left is not None
      return current.value


5. find_max(root)
-----------------

Return the largest value in the BST.

BST rule:

    larger values are always on the right

So the maximum value is the rightmost node.

Rules:

- If root is None:
      return None

- Otherwise:
      start from root
      keep moving right while current.right is not None
      return current.value


6. is_valid_bst(root)
---------------------

Return True if the tree is a valid BST.
Return False if it is not.

Important:

It is not enough to only check:

    root.left.value < root.value
    root.right.value > root.value

You must make sure:

- every value in the left subtree is smaller than root.value
- every value in the right subtree is bigger than root.value

Example invalid tree:

        10
       /  \
      5    20
          /
         6

This is invalid because 6 is in the right subtree of 10,
but 6 is smaller than 10.

Common idea:

Use lower and upper limits.

For every node:

    lower < node.value < upper

When going left:

    upper becomes root.value

When going right:

    lower becomes root.value


7. bst_delete(root, value)
--------------------------

Delete a value from the BST and return the root.

There are three main cases after you find the node:

Case 1: The node has no children.

    return None

Case 2: The node has only one child.

    return that child

Case 3: The node has two children.

    Find the smallest value in the right subtree.
    Replace current node's value with that smallest value.
    Delete that smallest value from the right subtree.

Example:

        10
       /  \
      5    20
     / \   /
    3   7 15

Delete 5:

        10
       /  \
      7    20
     /    /
    3    15


Expected output
---------------

[3, 5, 7, 10, 15, 20]
True
False
3
20
True
False
[3, 7, 10, 15, 20]
True
"""


class TreeNode:
    def __init__(self, value):
        # TODO: Store value.
        self.value = value

        # TODO: Store left child.
        self.left = None

        # TODO: Store right child.
        self.right = None


def bst_insert(root, value):
    # TODO: If root is None, return a new TreeNode.
    if root == None:
        return TreeNode(value)
    # TODO: If value is smaller than root.value, insert into left subtree.
    if value < root.value:
        root.left = bst_insert(root.left, value)
    # TODO: If value is bigger than root.value, insert into right subtree.
    if value > root.value:
        root.right = bst_insert(root.right, value)
    # TODO: Return root.
    return root


def bst_search(root, target):
    # TODO: If root is None, return False.
    if root == None:
        return False
    # TODO: If target equals root.value, return True.
    if target == root.value:
        return True
    # TODO: If target is smaller, search left only.
    if target < root.value:
        return bst_search(root.left, target)
    # TODO: If target is bigger, search right only.
    if target > root.value:
        return bst_search(root.right, target)


def inorder(root):
    # TODO: Base case. If root is None, return [].
    if root == None:
        return []
    # TODO: Return inorder left + root value + inorder right.
    return inorder(root.left) + [root.value] + inorder(root.right)


def find_min(root):
    # TODO: If root is None, return None.
    if root == None:
        return None
    # TODO: Start from root.
    if root.left != None:
    # TODO: Keep moving left while possible.
        return find_min(root.left)
    # TODO: Return the leftmost value.
    return root.value


def find_max(root):
    # TODO: If root is None, return None.
    if root == None:
        return None
    # TODO: Start from root.
    while root.right != None:
    # TODO: Keep moving right while possible.
        root = root.right
    # TODO: Return the rightmost value.
    return root.value


def is_valid_bst(root, lower=None, upper=None):
    # TODO: If root is None, return True.
    if root == None:
        return True
    # TODO: If lower exists and root.value <= lower, return False.
    if lower is not None and root.value <= lower:
        return False
    # TODO: If upper exists and root.value >= upper, return False.
    if upper is not None and root.value >= upper:
        return False
    # TODO: Check left subtree with upper changed to root.value.
    # TODO: Check right subtree with lower changed to root.value.
    return (
        is_valid_bst(root.left, lower, root.value)
        and is_valid_bst(root.right, root.value, upper)
        )


def bst_delete(root, value):
    # TODO: If root is None, return None.
    if root == None:
        return None
    # TODO: If value is smaller than root.value, delete from left subtree.
    if value < root.value:
        root.left = bst_delete(root.left, value)
    # TODO: If value is bigger than root.value, delete from right subtree.
    elif value > root.value:
        root.right = bst_delete(root.right, value)
    # TODO: Otherwise, this is the node to delete.
    else: 
        # TODO: Case 1 and 2: If there is no left child, return right child.
        if root.left == None:
            return root.right#有一个孩子顶上来和空是可以一起实现的
        # TODO: Case 1 and 2: If there is no right child, return left child.
        if root.right == None:
            return root.left#有一个孩子顶上来和空是可以一起实现的
        # TODO: Case 3: Node has two children.
        # Find the smallest value in the right subtree.
        successor_value = find_min(root.right)
        # TODO: Replace root.value with that smallest value.
        root.value = successor_value
        # TODO: Delete that smallest value from the right subtree.
        root.right = bst_delete(root.right, successor_value)
    # TODO: Return root.
    return root


def build_bst(values):
    root = None

    for value in values:
        root = bst_insert(root, value)

    return root


def main():
    values = [10, 5, 20, 3, 7, 15]
    root = build_bst(values)

    print(inorder(root))
    print(bst_search(root, 7))
    print(bst_search(root, 99))
    print(find_min(root))
    print(find_max(root))
    print(is_valid_bst(root))

    invalid_root = TreeNode(10)
    invalid_root.left = TreeNode(5)
    invalid_root.right = TreeNode(20)
    invalid_root.right.left = TreeNode(6)

    print(is_valid_bst(invalid_root))

    root = bst_delete(root, 5)
    print(inorder(root))
    print(is_valid_bst(root))


if __name__ == "__main__":
    main()

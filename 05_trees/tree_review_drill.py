"""
Tree Review Drill
=================

Goal:
Practice rewriting common binary tree functions from memory.

This file gives you only short hints.
Try to write each function without looking at the full solution first.


Sample tree
-----------

        10
       /  \
      5    20
     / \
    3   7


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
        # TODO: Store value, left child, and right child.
        self.value = value
        self.left = None
        self.right = None


def build_sample_tree():
    # TODO: Build the sample tree shown above and return root.
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    return root


def build_unbalanced_tree():
    # TODO: Build this tree and return root:
    #
    #       10
    #      /
    #     5
    #    /
    #   3
    #  /
    # 1
    list = [10,5,3,1]
    root = TreeNode(list[0])
    current = root   

    for value in list[1:]:
        current.left = TreeNode(value)
        current = current.left

    return root


def preorder(root):
    # Hint: root -> left -> right
    if root == None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    # Hint: left -> root -> right
    if root == None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    # Hint: left -> right -> root
    if root == None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


def count_nodes(root):
    # Hint: current node + left count + right count
    if root == None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right) 


def tree_height(root):
    # Hint: 1 + max(left height, right height)
    if root == None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


def search_tree(root, target):
    # Hint: target is in current node OR left subtree OR right subtree
    if root == None:
        return False
    if root.value == target:
        return True
    return search_tree(root.left, target) or search_tree(root.right, target)


def level_order(root):
    # Hint: BFS uses a queue.
    #BFS，Breadth-First Search，广度优先遍历。
    if root is None:
        return []
    list = []
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        list.append(node.value)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return list



def is_balanced(root):
    # Hint: compare left height and right height at every node.
    if root == None:
        return True
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    if abs(left_height-right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


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

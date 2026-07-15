"""
Linked List Practice: Basic Singly Linked List
==============================================

Goal:
Practice the basic idea of a linked list.

You will practice:
- class
- object references
- Node
- head
- next
- traversal
- append
- prepend
- contains
- delete
- reverse
- display
- length


Concept
-------

A normal Python list looks like this:

    [10, 20, 30]

A linked list is different.

It is made of nodes:

    10 -> 20 -> 30 -> None

Each node stores:

1. value
2. next

The value is the data.
The next points to the next node.


Node example
------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


If you create:

    node = Node(10)

Then:

    node.value is 10
    node.next is None


Task
----

Create two classes:

    Node
    LinkedList


LinkedList should support:

1. append(value)
2. display()
3. length()
4. prepend(value)
5. contains(value)
6. delete(value)
7. reverse()


1. append(value)
----------------

Add a new value to the end of the linked list.

Example:

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

The linked list should become:

    10 -> 20 -> 30 -> None


2. display()
------------

Return all values as a normal Python list.

Example:

    linked_list.display()

Should return:

    [10, 20, 30]


3. length()
-----------

Return how many nodes are in the linked list.

Example:

    linked_list.length()

Should return:

    3


4. prepend(value)
-----------------

Add a new value to the beginning of the linked list.

Example:

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)

The linked list should become:

    5 -> 10 -> 20 -> 30 -> None

Important idea:

    new_node.next = self.head
    self.head = new_node


5. contains(value)
------------------

Return True if the linked list contains the value.
Return False if it does not.

Example:

    linked_list.contains(20)
    # True

    linked_list.contains(99)
    # False


6. delete(value)
----------------

Delete the first node whose value equals value.

Example:

    5 -> 10 -> 20 -> 30 -> None

    linked_list.delete(20)

The linked list should become:

    5 -> 10 -> 30 -> None

Return rules:

- If the value is deleted, return True.
- If the value is not found, return False.

Important cases:

1. Empty linked list:

       self.head is None

2. The value is in the head node:

       self.head = self.head.next

3. The value is in the middle or tail:

       current.next = current.next.next


7. reverse()
------------

Reverse the linked list in place.

Example:

    5 -> 10 -> 30 -> None

    linked_list.reverse()

The linked list should become:

    30 -> 10 -> 5 -> None

Important idea:

You need to change the direction of each next pointer.

Before:

    5 -> 10 -> 30 -> None

After:

    None <- 5 <- 10 <- 30

Then move head to 30.

The common variables are:

    prev
    current
    next_node

Meaning:

- prev: the node before current in the reversed part
- current: the node you are processing now
- next_node: the original next node, saved before changing current.next


Important hints
---------------

The linked list starts with:

    self.head = None


If the linked list is empty:

    self.head is None


To walk through a linked list:

    current = self.head

    while current is not None:
        # use current.value
        current = current.next


For append(value):

1. Create a new node.
2. If self.head is None:
       self.head = new_node
3. Otherwise:
       start from self.head
       keep moving until current.next is None
       set current.next = new_node


For prepend(value):

1. Create a new node.
2. Make new_node.next point to the old head.
3. Make self.head point to new_node.


For contains(value):

1. Start from self.head.
2. Walk through the linked list.
3. If current.value == value, return True.
4. If you reach None, return False.


For delete(value):

1. If self.head is None, return False.
2. If self.head.value == value:
       self.head = self.head.next
       return True
3. Otherwise, start from self.head.
4. While current.next is not None:
       if current.next.value == value:
           current.next = current.next.next
           return True
       current = current.next
5. If you reach the end, return False.


For reverse():

1. Start with:

       prev = None
       current = self.head

2. While current is not None:

       save current.next into next_node
       make current.next point to prev
       move prev to current
       move current to next_node

3. After the loop:

       self.head = prev


Expected output
---------------

[]
0
[5]
1
False
False
[5, 10, 20, 30]
4
True
False
[5, 10, 30]
3
False
[30, 10, 5]
"""


class Node:
    def __init__(self, value):
        # TODO: Store the value.
        self.value = value
        self.next = None
        # TODO: Store the next node.
        


class LinkedList:
    def __init__(self):
        # TODO: Create head.
        self.head = None
        

    def append(self, value):
        # TODO: Create a new node.
        New_node = Node(value)
        # TODO: If the list is empty, make head point to the new node.
        if self.head is None:
            self.head = New_node
            return
        # TODO: Otherwise, walk to the end and attach the new node.
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = New_node

    def display(self):
        # TODO: Walk through the linked list and collect values into a list.
        list_print = []
        current = self.head

        while current is not None:
            list_print.append(current.value)
            current = current.next
        
        return list_print

    def length(self):
        # TODO: Count how many nodes are in the linked list.
        Count = 0
        current = self.head
        while current is not None:
            Count += 1
            current = current.next
        return Count

    def prepend(self, value):
        # TODO: Create a new node.
        New_Node = Node(value)
        # TODO: Make the new node point to the current head.
        New_Node.next = self.head
        # TODO: Move head to the new node.
        self.head = New_Node

    def contains(self, value):
        # TODO: Walk through the linked list.
        current = self.head
        while current is not None:
            if current.value == value:
        # TODO: If you find value, return True.
                return True
            current = current.next
        # TODO: If you reach the end, return False.    
        return False

    def delete(self, value):
        # TODO: If the linked list is empty, return False.
        current = self.head
        if self.head is None:
            return False
        # TODO: If the head node has the target value, move head to head.next.
        if self.head.value == value:
            self.head = self.head.next
            return True
        # TODO: Otherwise, walk through the list and find the node before the target.
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return True

            current = current.next

        # TODO: If not found, return False.
        return False

    def reverse(self):
        # TODO: Create prev and current.
        prev = None
        current = self.head
        # TODO: Walk through the linked list.
        while current != None:
        
        # TODO: Save the original next node before changing current.next.
            next_node = current.next
        # TODO: Make current.next point backward to prev.
            current.next = prev
        # TODO: Move prev and current forward.
            prev = current
        # TODO: Move head to the new first node.
            current = next_node 
        self.head = prev


def main():
    linked_list = LinkedList()

    print(linked_list.display())
    print(linked_list.length())

    linked_list.prepend(5)

    print(linked_list.display())
    print(linked_list.length())

    print(linked_list.contains(20))
    print(linked_list.contains(99))

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print(linked_list.display())
    print(linked_list.length())

    print(linked_list.delete(20))
    print(linked_list.display())
    print(linked_list.length())
    print(linked_list.delete(99))

    linked_list.reverse()
    print(linked_list.display())


if __name__ == "__main__":
    main()

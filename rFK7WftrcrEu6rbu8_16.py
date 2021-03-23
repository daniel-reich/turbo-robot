"""


Given a **Binary Search Tree** (BST) implementation, complete the traverse
function which is present in the BST class. Here you have to perform the
level-order traversal on BST which is another term for **Breadth First
Traversal**.

### Examples

    traverse() ➞  [10, 4, 20, 1, 5]
    
          10
          /   \
        4    20
      /  \
    1    5
    
    traverse() ➞ [100, 70, 200, 34, 80, 300]
    
           100
           /    \
        70    200
      /    \          \
    34   80      300

### Notes

Make sure you don't modify the code that is already in the **Code** tab. Only
complete the `traverse()` function and return an array.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
​
​
class BST:
    def __init__(self):
        self.head = None
​
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while True:
                if data > current.data and current.right:
                    current = current.right
                elif data < current.data and current.left:
                    current = current.left
                elif data > current.data:
                    current.right = new_node
                    break
                else:
                    current.left = new_node
                    break
        return self.head
​
    def traverse(self):
        lst_data = []
        level_nods = [self.head]
        while level_nods:
            next_level = []
            for node in level_nods:
                lst_data.append(node.data)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level_nods = next_level
        return lst_data


"""


Binary Search Tree is a node-based binary tree data structure which has the
following properties:

  * The left subtree of a node contains only nodes with keys lesser than the node's key.
  * The right subtree of a node contains only nodes with keys greater than the node’s key.
  * The left and right subtree each must also be a binary search tree.

Create a class that converts the number into a node in the tree (every node
should have left child, right child and the value of the node "child can be
none"). The class should have a function that inserts a new node to the binary
tree. And another function that prints the final binary tree (tree should be
printed from left to the write {left-root-right}).

### Examples

              10                                                           15
           5     11 ➞ [3, 5, 6, 10, 11]                               7          18        ➞  [5, 9, 7, 15, 17, 18, 19]
       3     6                                                     5     9     17     19
    
    root()=Node(10) ➞ 10 is the root of the tree (first node in the top)
    root.insert(5)
    root.insert(11)
    root.insert(3)
    root.insert(6)
    root.PrintTree() ➞ [3, 5, 6, 10, 11]
    root.data ➞ 10
    root.left.data ➞ 5
    root.right.data ➞ 11

### Notes

N/A

"""

class Node:
    tree=[]
​
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # Hint this line to clear the list for every object
        Node.tree.clear()
​
    def insert(self, val):
        if val >= self.data:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        else:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
​
    def PrintTree(self):
        if self.left is not None:
            self.left.PrintTree()
        Node.tree.append(self.data)
        if self.right is not None:
            self.right.PrintTree()
        return Node.tree


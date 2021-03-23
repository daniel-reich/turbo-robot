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
​
  tree_lst = []
​
  def __init__(self, num):
    self.data = num
    self.left = None
    self.right = None
    self.tree_lst.clear()
​
  def insert(self, num):
    if not self.left and num <= self.data:
      node = Node(num)
      self.left = node
    elif not self.right and num > self.data:
      node = Node(num)
      self.right = node
    elif num <= self.data:
      self.left.insert(num)
    else:
      self.right.insert(num)
​
  def PrintTree(self):
    if self.left:
      self.tree_lst = self.left.PrintTree()
    self.tree_lst.append(self.data)
    if self.right:
      self.tree_lst = self.right.PrintTree()
    return self.tree_lst


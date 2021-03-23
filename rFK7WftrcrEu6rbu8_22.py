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
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
class BST:
  def __init__(self):
    self.head = None
  def insert(self,data):
    node = Node(data)
    if not self.head:
      self.head = node
    else:
      current = self.head
      while True:
        if data < current.data:
          if current.left:
            current = current.left
          else:
            current.left = node
            break
        elif current.right:
          current = current.right
        else:
          current.right = node
          break
  def traverse(self):
    path = []
    queue = [self.head]
    while queue:
      current = queue[0]
      path.append(current)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
      queue.pop(0)
    return list(map(lambda x: x.data,path))


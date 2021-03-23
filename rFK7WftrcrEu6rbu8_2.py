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
  def __init__(self,d):
    self.d=d
    self.l=self.r=None
class BST:
  def __init__(self):self.h=None
  def insert(self,d):
    n=Node(d)
    if self.h==None:self.h=n
    else:
      c=self.h
      while 1:
        if d>c.d and c.r:c=c.r
        elif d<c.d and c.l:c=c.l
        elif d>c.d:c.r=n;break
        else:c.l=n;break
    return self.h
  def traverse(self):
    r,v=[],[]
    o=self.h
    if o:v.append(o);r.append(o.d)
    c=o
    while c:
        if c.l:r.append(c.l.d);v.append(c.l)
        if c.r:r.append(c.r.d);v.append(c.r)
        v.pop(0)
        if not v:break
        c=v[0]
    return r


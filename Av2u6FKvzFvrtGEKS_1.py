"""


Given a linked list class, implement a method called `reverse()` that reverses
the linked list.

### Examples

    Input: 10 -> 20 -> 30 -> 40 -> None
    
    Output: 40 -> 30 -> 20 -> 10 -> None

### Notes

Just implement the `reverse()` function and DO NOT modify any other code in
the **Code** tab, which has nothing but the starter code.

"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def reverse(self):
    if self.next:
      self.next.reverse()
      self.next.next= self
      self.next = None      
​
class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
​
  def insert(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
​
  def traverse(self):
    if self.head == None:
      return []
    temp = self.head
    result = []
    while temp!=None:
      result.append(temp.data)
      temp = temp.next
    return result
    
  def reverse(self):
    self.head.reverse()
    self.head, self.tail = self.tail, self.head
    # Basically implemented reverse at node level

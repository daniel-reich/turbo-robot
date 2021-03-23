"""


This classic problem dates back to Roman times. There are 41 soldiers arranged
in a circle. Every third soldier is to be killed by their captors, continuing
around the circle until only one soldier remains. He is to be freed. Assuming
you would like to stay alive, at what position in the circle would you stand?

Generalize this problem by creating a function that accepts the number of
soldiers `n` and the interval at which they are killed `i`, and returns the
position of the fortunate survivor.

### Examples

    josephus(41, 3) ➞ 31
    
    josephus(35, 11) ➞ 18
    
    josephus(11, 1) ➞ 11
    
    josephus(2, 2) ➞ 1

### Notes

  * Assume the positions are numbered 1 to `n` going **clockwise** around the circle.
  * If the interval is 3, the first soldiers to die are at positions 3, 6, and 9.

"""

class Node:
​
    def __init__(self, value):
        self.value = value
        self.next = None
​
​
class CircularLinkedList:
​
    def __init__(self):
        self.head = None
    
    def __str__(self):
        arr = []
​
        current = self.head
        
        if self.head:
            while True:
                if current.next == self.head:
                    arr.append(current.value)
                    break
                arr.append(current.value)
                current = current.next
                
​
        return ' -> '.join(map(str, arr))
​
​
​
    
    def push(self, value):
        node = Node(value)
        
        if not self.head:
            self.head = node
            self.head.next = self.head
            return
        
        current = self.head
​
        while current.next != self.head:
            current = current.next
        # print(current.value, node.value)
        node.next = self.head        
        current.next = node
​
        
    
    def push_array(self, array):
        for x in array:
            self.push(x)
​
​
​
def josephus(n, k):
    a = CircularLinkedList()
    a.push_array(range(1,n+1))
​
    killer = a.head
    prev = a.head
​
    if not n:
        return False
    
    while killer.next != killer:
​
        count = 1
        while count != k:
            prev = killer
            killer = killer.next
            count += 1
        
        prev.next = killer.next
        killer = prev.next
    
    return killer.value if killer.value != 1 else n


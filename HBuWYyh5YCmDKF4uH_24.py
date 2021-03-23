"""


An **almost-sorted sequence** is a sequence that is **strictly increasing** or
**strictly decreasing** if you remove a **single element** from the list (no
more, no less). Write a function that returns `True` if a list is **almost-
sorted** , and `False` otherwise.

For example, if you remove `80` from the first example, it is perfectly sorted
in ascending order. Similarly, if you remove `7` from the second example, it
is perfectly sorted in descending order.

### Examples

    almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True
    
    almost_sorted([6, 5, 4, 7, 3]) ➞ True
    
    almost_sorted([6, 4, 2, 0]) ➞ False
    // Sequence is already sorted.
    
    almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
    // Requires removal of more than 1 item.

### Notes

  * Completely sorted lists should return `False`.
  * Lists will always be **> 3** in length (to remove ambiguity).
  * Numbers in each input list will be unique - don't worry about "ties".

"""

def almost_sorted(lst):
    for i in range(2):
        x = is_inc(lst)
        if x == -1:
            return False
        # try removing item at index x+1
        y = is_inc(lst[:x+1] + lst[x+2:])
        if y == -1:
            return True
        # try removing item at index x
        z = is_inc(lst[:x] + lst[x+1:])
        if z == -1:
            return True
        # check if desc by using reversed list
        lst = lst[::-1] 
    return False
​
def is_inc(a):
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            return i
    return -1


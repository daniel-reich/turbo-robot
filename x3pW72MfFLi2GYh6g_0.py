"""


Given a list of numbers, representing the height of a mountain in certain
intervals, return whether this mountain is **scalable**.

A mountain can be considered _scalable_ if each number is within **5** units
of the next number in either direction.

### Examples

    is_scalable([1, 2, 4, 6, 7, 8]) ➞ True
    
    is_scalable([40, 45, 50, 45, 47, 52]) ➞ True
    
    is_scalable([2, 9, 11, 10, 18, 21]) ➞ False

### Notes

The list may start at any number and can be any length.

"""

def is_scalable(lst):
  return all(abs(a-b) <= 5 for a, b in zip(lst, lst[1:]))


"""


A number is considered _slidey_ if for every digit in the number, the next
digit from that has an absolute difference of one. Check the examples below.

### Examples

    is_slidey(123454321) ➞ True
    
    is_slidey(54345) ➞ True
    
    is_slidey(987654321) ➞ True
    
    is_slidey(1123) ➞ False
    
    is_slidey(1357) ➞ False

### Notes

  * A number cannot slide properly if there is a "flat surface" (example #4), or has gaps (example #5).
  * All single digit numbers can be considered _slidey numbers_!

"""

def is_slidey(n):
  n = list(map(int, list(str(n))))
  is_differ_by_one = [True if abs(x - y) == 1 else False for x, y in zip(n[:-1], n[1:])]
  return all(is_differ_by_one)


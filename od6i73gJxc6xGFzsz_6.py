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
  
  Text = str(n)
  
  Previous = 0
  Current = 1
  Length = len(Text)
  
  while (Current < Length):
    Value_A = int(Text[Previous])
    Value_B = int(Text[Current])
    Difference = int(abs(Value_A - Value_B))
    
    if (Difference == 1):
      Previous += 1
      Current += 1
    else:
      return False
  
  return True


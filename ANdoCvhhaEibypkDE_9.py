"""


Create a function that returns the sum of the digits formed from the first and
last digits, all the way to the center of the number.

### Worked Example

    closing_in_sum(2520) ➞ 72
    
    # The first and last digits are 2 and 0.
    # 2 and 0 form 20.
    # The second and second to last digits are 5 and 2.
    # 5 and 2 form 52.
    
    # 20 + 52 = 72

### Examples

    closing_in_sum(121) ➞ 13
    # 11 + 2
    
    closing_in_sum(1039) ➞ 22
    # 19 + 3
    
    closing_in_sum(22225555) ➞ 100
    # 25 + 25 + 25 + 25

### Notes

  * If the number has an **odd** number of digits, simply add on the single-digit number in the center (see example #1).
  * Any number which is **zero-padded** counts as a single digit (see example #2).

"""

def closing_in_sum(n):
  s = str(n)
  extra = int(s[len(s)//2]) if len(s)%2==1 else 0
  return sum(int(s[i]+s[-i-1]) for i in range(len(s)//2))+extra


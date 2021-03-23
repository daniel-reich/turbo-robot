"""
A number has a **breakpoint** if it can be split in a way where the digits on
the left side and the digits on the right side sum to the same number.

For instance, the number _35190_ can be sliced between the digits _351_ and
_90_ , since _3 + 5 + 1 = 9_ and _9 + 0 = 9_. On the other hand, the number
_555_ does **not** have a **breakpoint** (you must split **between** digits).

Create a function that returns `True` if a number has a breakpoint, and
`False` otherwise.

### Examples

    break_point(159780) ➞ True
    
    break_point(112) ➞ True
    
    break_point(1034) ➞ True
    
    break_point(10) ➞ False
    
    break_point(343) ➞ False

### Notes

  * Read each digit as only one number.
  * Check the **Resources** tab for a hint.

"""

def accumulate(nums):
    accumulate = []
    total = 0
    for i in nums:
        total += i
        accumulate.append(total)
    return accumulate
​
​
def break_point(num):
    lst = [int(i) for i in ' '.join(str(num)).split()]
    x = accumulate(lst)
    y = list(reversed(accumulate(reversed(lst))))
    guess = []
    for index, i in enumerate(x):
        if i >= y[index + 1]:
            if i == y[index + 1]:
                return True
            return False


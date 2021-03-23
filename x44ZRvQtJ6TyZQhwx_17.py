"""


A **pandigital** number contains all digits (0-9) at least once. Write a
function that takes an integer, returning `True` if the integer is pandigital,
and `False` otherwise.

### Examples

    is_pandigital(98140723568910) ➞ True
    
    is_pandigital(90864523148909) ➞ False
    # 7 is missing.
    
    is_pandigital(112233445566778899) ➞ False

### Notes

Think about the properties of a pandigital number when all duplicates are
removed.

"""

def is_pandigital(n):
    a=[]
    b=[]
    for i in str(n):
        if i not in a:
            a.append(int(i))
    for i in range(0,10):
        if i not in a:
            b.append(i)
    if len(b)>=1:
        return False
    else:
        return True


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

def break_point(num):
    l = []
    i = 0
    s1 = 0
    s2 = 0
    for a in str(num):
        l.append(a)
    while i < len(l) :
        s1 ,s2 = 0, 0
        for a in l[:i]:
            s1 += int(a)
        for b in l[i:]:
            s2 += int(b)
        i+=1
        if s1 == s2:
            return True
    return False


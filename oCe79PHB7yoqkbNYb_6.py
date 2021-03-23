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
    num_str = str(num)
    for i in range(len(num_str)):
        lst1 = list(num_str[0:i])
        lst2 = list(num_str[i::])
        num1 = 0
        for j in range(len(lst1)):
            num1 += int(lst1[j])
        
        num2=0
        for j in range(len(lst2)):
            num2 += int(lst2[j])
        if num1 == num2:
            return True
    return False


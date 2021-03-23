"""


A repdigit is a positive number composed out of the same digit. Create a
function that takes an integer and returns whether it's a repdigit or not.

### Examples

    is_repdigit(66) ➞ True
    
    is_repdigit(0) ➞ True
    
    is_repdigit(-11) ➞ False

### Notes

  * The number `0` should return `True` (even though it's not a positive number).
  * Check the **Resources** tab for more info on repdigits.

"""

def is_repdigit(num):
    num = list(str(num))
    lis = []
    for i in range(len(num)):
        if i >= len(num)-1:
            break
        elif num[i] == num[i+1]:
            lis.append(True)
        else: lis.append(False)
    return False if False in lis else True


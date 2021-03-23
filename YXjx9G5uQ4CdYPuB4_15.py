"""


 **Mubashir** needs your help to compare two lists.

First list `lst1` contains some numbers and second list `lst2` contains
**squared values of numbers given in the first list**.

Create a function which takes these two lists and returns `True` if all square
values are available, `False` otherwise.

    lst1 = [121, 144, 19, 161, 19, 144, 19, 11]  
    lst2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

Returns `True` because **121 is square of 11, 14641 is square of 121, 20736 is
square of 144, 361 is square of 19, 25921 the square of 161, and so on...**

    lst1 = [121, 144, 19, 161, 19, 144, 19, 11] 
    lst2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

### Examples

    simple_comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) ➞ True
    
    simple_comp([4, 4], [1, 31]) ➞ False
    
    simple_comp([2, 2, 3], [4, 4, 9]) ➞ True

### Notes

Numbers can be in any order.

"""

def simple_comp(lst1, lst2):
    if lst1 is None or lst2 is None or len(lst1) != len(lst2):
        return False
    lst1.sort(key=abs)
    lst2.sort()
    for i in range(len(lst1)):
        if lst1[i] ** 2 != lst2[i]:
            return False
    return True


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

def simple_comp(ls1, ls2):
    if ls1 is None or ls2 is None:
        return False
    ls1.sort(key=abs)
    ls2.sort(key=abs)
    return (all(a * a == b for a, b in zip(ls1, ls2))
            if len(ls1) == len(ls2) else False)


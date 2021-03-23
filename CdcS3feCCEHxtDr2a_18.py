"""


Create a function that returns `True` if an array of pairs are sufficient for
a clear ordering of all items.

To illustrate:

    clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]) ➞ True
    # Since unequivocally: "D" < "A" < "C" < "B"

On the other hand:

    clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]) ➞ False
    # Since we know that "C" < "D" < "A", and we know "B" < "A"
    # but we don't know anything about "B"s relationship with "C" or "D".

### Examples

    clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]) ➞ True
    
    clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]) ➞ False

### Notes

See Comments for a good visualization of the question.

"""

from collections import Counter
from operator import itemgetter
def clear_ordering(lst):
    bb=[x for row in lst for x in row]
    cc=Counter(bb)
    tt=[k for k, v in cc.items() if v ==1]
    dic={x:row.index(x) for row in lst for x in row if x in tt}
    if min(list(dic.values())) != 0:
        return False
    sd=list(dic.keys())[list(dic.values()).index(0)]
    n=len(lst)
    for j in range(0,n):
        if sd == [row for row in lst if sd in row][0][0]:
            r = [row for row in lst if sd in row][0]
            sd = [row for row in lst if sd in row][0][1]
            lst.remove(r)
            if len(lst) == 0:
                return True
        else:
            return False


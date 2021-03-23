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

def clear_ordering(lst):
    while len(lst) > 1:
        removed = False
        for p in lst[1:]:
            if lst[0][0] == p[1]:
                lst[0][0] = p[0]
                lst.remove(p)
                removed = True
            elif lst[0][1] == p[0]:
                lst[0][1] = p[1]
                lst.remove(p)
                removed = True
        if not removed:
            return False
    return True


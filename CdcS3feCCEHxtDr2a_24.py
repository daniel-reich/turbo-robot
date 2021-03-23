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
  l1=[]
  l3=[]
  for c in lst:
    c=tuple(c)
    l1.append(c)
  l2=zip(*l1)
  for i in l2:
    i=list(i)
    l3.append(i)
  x=len(set(l3[0]))
  return all(x==len(set(m)) for m in l3)


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
  order = {}
  
  for l in lst:
    first = l[0]
    second = l[1]
    
    order[second] = True
    if not first in order.keys():
      order[first] = False
    else:
      if order[first] == False:
        return False
  
  count = 0
  
  for key in order.keys():
    if order[key] == False:
      count += 1
  
  if count > 1:
    return False
  else:
    return True


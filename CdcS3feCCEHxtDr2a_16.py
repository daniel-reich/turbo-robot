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
  t1 = []
  t2 = []
  for i in range(len(lst)):
    t1.append(lst[i][0])
    t2.append(lst[i][1])
  c1 = 0
  for i in range(len(t1)):
    if t1[i] not in t2:
      c1 += 1
  c2 = 0
  for i in range(len(t2)):
    if t2[i] not in t1:
      c2 += 1
  if c1 > 1 or c2 > 1:
    return False
  else:
    return True


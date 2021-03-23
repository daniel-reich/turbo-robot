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

def clear_ordering(lista):
  sup = {}
  for i in range(len(lista)):
    if lista[i][0] not in sup.keys():
      sup[lista[i][0]] = [lista[i][1]]
    else:
      sup[lista[i][0]].append(lista[i][1])
  print(sup)
  n = 0
  for valor in sup.values():
    if valor[0] not in list(sup.keys()):
      n += 1
      print(valor[0])
  
  if n != 1:
    return False
  else:
    return True


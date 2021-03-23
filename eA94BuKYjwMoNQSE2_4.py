"""


Create a function that returns `True` if a given inequality expression is
correct and `False` otherwise.

### Examples

    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

### Notes

N/A

"""

def correct_signs(txt):
  l, op, r, *rest = txt.split()
  if   op == '<' and not (int(l) < int(r)): return False
  elif op == '>' and not (int(l) > int(r)): return False
  l = r
  
  while rest:
    op, r, *rest = rest
    if   op == '<' and not (int(l) < int(r)): return False
    elif op == '>' and not (int(l) > int(r)): return False
    l = r
    
  return True


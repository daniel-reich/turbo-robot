"""


Write a function that returns `True` if the binary string can be rearranged to
form a string of alternating `0`s and `1`s.

### Examples

    can_alternate("0001111") ➞ True
    # Can make: "1010101"
    
    can_alternate("01001") ➞ True
    # Can make: "01010"
    
    can_alternate("010001") ➞ False
    
    can_alternate("1111") ➞ False

### Notes

  * No substring of the output may contain more than one consecutive repeating character (e.g. `00` or `11` are not allowed).
  * Return `False` if a string only contains `0`s or only contains `1`s.

"""

def can_alternate(s):
  a=0
  b=0
  
  for x in s:
    if x =='1':
      a+=1
    else:
      b+=1
  print(a,b)
  if a+1 == b or b+1 ==a or a== b:
    return True
  else:
    return False


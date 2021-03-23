"""


Create a function that returns the amount of duplicate characters in a string.
It will be case sensitive and spaces are included. If there are no duplicates,
return `0`.

### Examples

    duplicates("Hello World!") ➞ 3
    # "o" = 2, "l" = 3.
    # "o" is duplicated 1 extra time and "l" is duplicated 2 extra times.
    # Hence 1 + 2 = 3
    
    duplicates("foobar") ➞ 1
    
    duplicates("helicopter") ➞ 1
    
    duplicates("birthday") ➞ 0
    # If there are no duplicates, return 0

### Notes

Make sure to only start counting the second time a character appears.

"""

def duplicates(txt):
  c=0
  d=[]
  for i in txt:
    if i in d: pass
    else:
      a=0
      a=txt.count(i)
      if a>1:c=c+(a-1)
      d.append(i)
  return c


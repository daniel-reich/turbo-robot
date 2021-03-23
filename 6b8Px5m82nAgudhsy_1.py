"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
  s=list(str(num))
  i=len(s)-2
  while int(''.join(s))<=num and i>-1:
    if s[i:]==sorted(s[i:],reverse=True):
      i-=1
    else:
      tail=sorted(s[i:])
      s=s[:i] + [tail.pop(tail.index(s[i])+1)] + tail
  return int(''.join(s))


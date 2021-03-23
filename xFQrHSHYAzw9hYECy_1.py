"""


Someone is typing on the sticky keyboard. Occasionally a key gets stuck and
more than intended number of characters of a particular letter is being added
into the string. The function input contains `original` and `typed` strings.
Determine if the `typed` string has been made from the `original`. Return
`True` if it is and `False` if the typed string cannot have been made from the
`original`.

### Examples

    is_long_pressed("alex", "aaleex") ➞ True
    
    is_long_pressed("saeed", "ssaaedd") ➞ False
    
    is_long_pressed("leelee", "lleeelee") ➞ True
    
    is_long_pressed("Tokyo", "TTokkyoh") ➞ False
    
    is_long_pressed("laiden", "laiden") ➞ True

### Notes

N/A

"""

import re
def is_long_pressed(original, typed):
  opieces = [m.group(0) for m in re.finditer(r'(.)\1*', original)]
  tpieces = [m.group(0) for m in re.finditer(r'(.)\1*', typed)]
  
  return len(opieces)==len(tpieces) and \
      all(op[0]==tp[0] and len(op)<=len(tp) for op,tp in zip(opieces,tpieces))


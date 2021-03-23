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

from re import split
​
def is_long_pressed(o, t):
  count = lambda s: {c: s.count(c) for c in list(set(s))}
  chunk = lambda s: ''.join(filter(bool, split("(.)\\1+", s)))
  x, y = list(filter(bool, split("\\b", o))), list(filter(bool, split("\\b", t)))
  for i, k in enumerate(x):
    a, b, w, v = chunk(x[i]), chunk(y[i]), count(x[i]), count(y[i])
    if a != b or len(a) != len(b) or any(w[k] > v[k] for k in w.keys()): return False
  return True


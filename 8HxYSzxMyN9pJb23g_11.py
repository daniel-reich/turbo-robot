"""


Create a function that accepts `txt` and `cases` as parameters where the
string is split into **N distinct cases** of **equal length** as shown:

### Examples

    split_n_cases("Strengthened", 6) ➞ ["St", "re", "ng", "th", "en", "ed"]
    
    split_n_cases("Unscrupulous", 2) ➞ ["Unscru", "pulous" ]
    
    split_n_cases("Flavorless", 1) ➞ ["Flavorless" ]

### Notes

If it's not possible to split the string as described, return `["Error"]`.

"""

import textwrap as tw
def split_n_cases(t,c):
  l=len(t)
  if l/c != int(l/c) or l/c<1: return ['Error']
  return tw.TextWrapper(width=l//c).wrap(t)


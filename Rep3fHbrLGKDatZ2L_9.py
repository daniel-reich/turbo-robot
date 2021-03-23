"""


You will be given a string that is made up of some repeated pattern of
characters. However, one of the characters in the string will be missing and
replaced by an underscore. Write a function that returns the missing
character.

### Examples

    complete_pattern("ABCABCA_CAB") ➞ "B"
    
    complete_pattern("_ABAABAABA") ➞ "A"
    
    complete_pattern("X+X*X+X*X+X_") ➞ "*"

### Notes

  * The pattern will be repeated in full at least twice, though one of those repetitions may contain the missing character.
  * The string may end in the middle of a repetition of the pattern.
  * The pattern will never contain an underscore.

"""

from re import findall
​
def complete_pattern(p):
  c = list(set(p.replace('_', '')))
  n, x, y, k = len(c), 'x', 'y', 0
  while x != y:
    x, y = findall(r'(?:.{'+str(n)+'})', p.replace('_', c[k]))[:2]
    if x == y and 4 * len(x) <= len(p):
      if p.replace('_', c[k])[:4*len(x)] == 2 * (x + y): break
      x, y = 'x', 'y'
    k += 1
    if k == len(c): k, n = 0, n + 1
  return ((x+y)*(len(p)//len(x)))[p.index('_')]


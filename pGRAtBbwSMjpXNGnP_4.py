"""


The function is given a list of words and a new alphabet (English letters in
different order). Determine if the list of words is sorted lexicographically.
The words consist of lower case letters.

### Examples

    is_sorted(["hello", "edabitlot"], "hlabcdefgijkmnopqrstuvwxyz") ➞ True
    
    is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") ➞ False
    
    is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") ➞ False
    
    is_sorted(["deceased", "folks", "can", "vote"], "abdefghijklmnopqrstcuvwxyz") ➞ True

### Notes

N/A

"""

def is_sorted(w, l):
  for (x, y) in zip(w, w[1:]):
    if x == y or y.startswith(x): continue
    if x.startswith(y): return False
    for k in range(len(x)):
      a, b = l.index(x[k]), l.index(y[k])
      if a < b: break
      if a > b: return False
  return True


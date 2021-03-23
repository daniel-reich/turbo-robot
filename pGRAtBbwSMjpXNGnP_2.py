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

def is_sorted(w,l):
  def cmp(s,t):
    for x,y in zip(s,t):
      a,b=l.find(x),l.find(y)
      if a<b:return 1
      if a>b:return 0
    return len(s)<=len(t)
  return all(cmp(i,j)for i,j in zip(w,w[1:]))


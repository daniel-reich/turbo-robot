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

def is_sorted(words, alphabet):
  
  alph = dict()
  
  for i in range(0,len(alphabet)):
    alph[alphabet[i]]=i
    
    
  new_l = []
  
  for x in words:
    s=""
    for i in range(0,len(x)):
      s+=chr(alph[x[i]]+97)
    new_l.append(s)
  
  return sorted(new_l)==new_l


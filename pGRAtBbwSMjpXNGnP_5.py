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
  code = {ch: i for i, ch in enumerate(alphabet)}
  for i in range(len(words)-1):
    w2l = len(words[i+1])
    for j in range(len(words[i])):
      if j == w2l or code[words[i][j]] > code[words[i+1][j]]:
        return False
      if code[words[i][j]] < code[words[i+1][j]]:
        break
  return True

